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
    public partial class DeleteForm : Form
    {

        Form1 mainForm;
        public DeleteForm()
        {
            InitializeComponent();
        }

        public DeleteForm(Form1 f)
        {
            InitializeComponent();
            mainForm = f;
        }

        private void buttonDel_Click(object sender, EventArgs e)
        {
            if (textBoxAuthor.TextLength > 0)
            {
                mainForm.N = Logic.deleteBookByAuthor(textBoxAuthor.Text);
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
