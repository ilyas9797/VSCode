using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Runtime.InteropServices;

namespace lab2_form
{
    public partial class FindForm : Form
    {
        BindingList<SampleRow> data;
        Form1 mainForm;

        public FindForm()
        {
            InitializeComponent();
        }

        public FindForm(Form1 f, string field, string value)
        {
            InitializeComponent();

            mainForm = f;
            int field_number;
            if (field == "Name")
                field_number = 1;
            else
                field_number = 2;

            int k = Logic.numberOfFindedBooks(field_number, value);

            data = new BindingList<SampleRow>();

            IntPtr p_bk = Logic.findByField(field_number, value, k);

            for (int i = 0; i < k; i++)
            {
                Logic.Book bk = (Logic.Book)Marshal.PtrToStructure(p_bk + i * Marshal.SizeOf<Logic.Book>(), typeof(Logic.Book));
                data.Add(new SampleRow(bk.name, bk.author, bk.numberofpage, bk.rating));
            }

            dataGridView1.DataSource = data;
            dataGridView1.ReadOnly = true;
            dataGridView1.AllowUserToAddRows = false;
        }
    }
}
