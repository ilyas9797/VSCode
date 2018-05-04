using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace lab2_form
{
    public partial class AddForm : Form
    {
        Form1 mainForm;
        int k = 0;

        public AddForm()
        {
            InitializeComponent();
        }

        public AddForm(Form1 f)
        {
            InitializeComponent();
            mainForm = f;
        }

        public AddForm(Form1 f, int k)
        {
            InitializeComponent();
            mainForm = f;
            button1.Text = "Изменить";
            this.k = k;
        }

        private void buttonAdd_Click(object sender, EventArgs e)
        {
            int numberofpages = (int) numericUpDownNp.Value;
            int rating = (int)numericUpDownRating.Value;
            if (textBoxName.TextLength > 0 && textBoxAuthor.TextLength > 0 && numberofpages > 0 && rating > 0)
            {
                if (k == 0)
                {
                    mainForm.N = Logic.addBook(textBoxName.Text, textBoxAuthor.Text, numberofpages.ToString(), rating.ToString());
                }
                else
                {
                    Logic.changeBook(k, textBoxName.Text, textBoxAuthor.Text, numberofpages.ToString(), rating.ToString());
                }
                mainForm.UpdateData();
                Close();
            }
            else
            {
                MessageBox.Show("Заполните поля");
            }
        }
    }
}
