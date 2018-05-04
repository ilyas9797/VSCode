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
    public partial class Form1 : Form
    {
        int n;
        BindingList<SampleRow> data;

        public BindingList<SampleRow> Data { get => data; set => data = value; }
        public int N { get => n; set => n = value; }

        public Form1()
        {
            InitializeComponent();

            n = Logic.numberOfBooks();
            data = new BindingList<SampleRow>();
            UpdateData();

            dataGridView1.DataSource = data;
            dataGridView1.ReadOnly = true;
            dataGridView1.AllowUserToAddRows = false;
        }

        private void buttonAdd_Click(object sender, EventArgs e)
        {
            AddForm addForm = new AddForm(this);
            addForm.ShowDialog();
        }

        private void buttonSortByName_Click(object sender, EventArgs e)
        {
            Logic.sortBookByField(1);
            UpdateData();
        }

        private void buttonSortByRating_Click(object sender, EventArgs e)
        {
            Logic.sortBookByField(2);
            UpdateData();
        }

        private void buttonDel_Click(object sender, EventArgs e)
        {
            DeleteForm delForm = new DeleteForm(this);
            delForm.ShowDialog();
        }
        private void buttonFind_Click(object sender, EventArgs e)
        {
            if (comboBoxFindField.Text.Length > 0 && textBoxFindValue.TextLength > 0)
            {
                FindForm findForm = new FindForm(this, comboBoxFindField.Text, textBoxFindValue.Text);
                findForm.ShowDialog();
            }
            else
            {
                MessageBox.Show("Выберите поля для поиска\nЗадайте значение поля");
            }
        }

        private void buttonDelByNum_Click(object sender, EventArgs e)
        {
            if ((int)numericUpDownDelNumber.Value > n)
            {
                MessageBox.Show("Превышение числа книг в базе");
            }
            else
            {
                n = Logic.deleteBookByNumber((int)numericUpDownDelNumber.Value);
                UpdateData();
            }
        }

        private void buttonChangeBook_Click(object sender, EventArgs e)
        {
            if ((int)numericUpDownChangeBook.Value > n)
            {
                MessageBox.Show("Превышение числа книг в базе");
            }
            else
            {
                AddForm addForm = new AddForm(this, (int)numericUpDownDelNumber.Value);
                addForm.ShowDialog();
            }
        }

        public void UpdateData()
        {
            data.Clear();

            IntPtr p_bk = Logic.output();

            for (int i = 0; i < n; i++)
            {
                Logic.Book bk = (Logic.Book)Marshal.PtrToStructure(p_bk + i * Marshal.SizeOf<Logic.Book>(), typeof(Logic.Book));
                data.Add(new SampleRow(bk.name, bk.author, bk.numberofpage, bk.rating));
            }
        }

    }

    public static class Logic
    {
        [DllImport("logic\\lab2dll.dll", CallingConvention = CallingConvention.Cdecl)]
        public static extern int numberOfBooks();

        [DllImport("logic\\lab2dll.dll", CallingConvention = CallingConvention.Cdecl)]
        public static extern int addBook(string name, string author, string numberofpage, string rating);

        //field == 1 => sort by name
        //field == 2 => sort by rating
        [DllImport("logic\\lab2dll.dll", CallingConvention = CallingConvention.Cdecl)]
        public static extern void sortBookByField(int field);

        [DllImport("logic\\lab2dll.dll", CallingConvention = CallingConvention.Cdecl)]
        public static extern int deleteBookByAuthor(string author);

        [StructLayout(LayoutKind.Sequential, CharSet = CharSet.Ansi)]
        public struct Book
        {
            /// char[256]
            [MarshalAsAttribute(UnmanagedType.ByValTStr, SizeConst = 256)]
            public string name;
            /// char[256]
            [MarshalAsAttribute(UnmanagedType.ByValTStr, SizeConst = 256)]
            public string author;
            /// char[8]
            [MarshalAsAttribute(UnmanagedType.ByValTStr, SizeConst = 8)]
            public string numberofpage;
            /// char[8]
            [MarshalAsAttribute(UnmanagedType.ByValTStr, SizeConst = 8)]
            public string rating;
        }

        [DllImport("logic\\lab2dll.dll", CallingConvention = CallingConvention.Cdecl)]
        public static extern IntPtr output();

        //field == 1 => поиск по названию
        //field == 2 => поиск по автору
        [DllImport("logic\\lab2dll.dll", CallingConvention = CallingConvention.Cdecl)]
        public static extern int numberOfFindedBooks(int field, string value);

        //field == 1 => поиск по названию
        //field == 2 => поиск по автору
        [DllImport("logic\\lab2dll.dll", CallingConvention = CallingConvention.Cdecl)]
        public static extern IntPtr findByField(int field, string value, int k);

        [DllImport("logic\\lab2dll.dll", CallingConvention = CallingConvention.Cdecl)]
        public static extern int deleteBookByNumber(int k);

        [DllImport("logic\\lab2dll.dll", CallingConvention = CallingConvention.Cdecl)]
        public static extern void changeBook(int k, string name, string author, string numberofpage, string rating);
    }

    public class SampleRow
    {
        public string Name { get; set; }
        public string Author { get; set; }
        public string Numberofpages { get; set; }
        public string Rating { get; set; }

        public string Hidden = "";

        public SampleRow(string name, string author, string numberofpages, string rating)
        {
            Name = name;
            Author = author;
            Numberofpages = numberofpages;
            Rating = rating;
        }
    }
}
