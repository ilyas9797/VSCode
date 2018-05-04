namespace lab2_form
{
    partial class Form1
    {
        /// <summary>
        /// Обязательная переменная конструктора.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Освободить все используемые ресурсы.
        /// </summary>
        /// <param name="disposing">истинно, если управляемый ресурс должен быть удален; иначе ложно.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Код, автоматически созданный конструктором форм Windows

        /// <summary>
        /// Требуемый метод для поддержки конструктора — не изменяйте 
        /// содержимое этого метода с помощью редактора кода.
        /// </summary>
        private void InitializeComponent()
        {
            this.dataGridView1 = new System.Windows.Forms.DataGridView();
            this.button1 = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.button3 = new System.Windows.Forms.Button();
            this.button4 = new System.Windows.Forms.Button();
            this.button5 = new System.Windows.Forms.Button();
            this.comboBoxFindField = new System.Windows.Forms.ComboBox();
            this.textBoxFindValue = new System.Windows.Forms.TextBox();
            this.numericUpDownDelNumber = new System.Windows.Forms.NumericUpDown();
            this.buttonDelByNum = new System.Windows.Forms.Button();
            this.buttonChangeBook = new System.Windows.Forms.Button();
            this.numericUpDownChangeBook = new System.Windows.Forms.NumericUpDown();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownDelNumber)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownChangeBook)).BeginInit();
            this.SuspendLayout();
            // 
            // dataGridView1
            // 
            this.dataGridView1.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridView1.Location = new System.Drawing.Point(13, 13);
            this.dataGridView1.Name = "dataGridView1";
            this.dataGridView1.Size = new System.Drawing.Size(495, 198);
            this.dataGridView1.TabIndex = 0;
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(13, 226);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(75, 23);
            this.button1.TabIndex = 1;
            this.button1.Text = "Добавить";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.buttonAdd_Click);
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(94, 226);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(130, 23);
            this.button2.TabIndex = 2;
            this.button2.Text = "Сортировать по имени";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.buttonSortByName_Click);
            // 
            // button3
            // 
            this.button3.Location = new System.Drawing.Point(230, 226);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(144, 23);
            this.button3.TabIndex = 3;
            this.button3.Text = "Сортировать по рейтингу";
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.buttonSortByRating_Click);
            // 
            // button4
            // 
            this.button4.Location = new System.Drawing.Point(380, 226);
            this.button4.Name = "button4";
            this.button4.Size = new System.Drawing.Size(111, 23);
            this.button4.TabIndex = 4;
            this.button4.Text = "Удалить по автору";
            this.button4.UseVisualStyleBackColor = true;
            this.button4.Click += new System.EventHandler(this.buttonDel_Click);
            // 
            // button5
            // 
            this.button5.Location = new System.Drawing.Point(349, 254);
            this.button5.Name = "button5";
            this.button5.Size = new System.Drawing.Size(159, 23);
            this.button5.TabIndex = 5;
            this.button5.Text = "Поиск по выбранному полю";
            this.button5.UseVisualStyleBackColor = true;
            this.button5.Click += new System.EventHandler(this.buttonFind_Click);
            // 
            // comboBoxFindField
            // 
            this.comboBoxFindField.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.comboBoxFindField.FormattingEnabled = true;
            this.comboBoxFindField.Items.AddRange(new object[] {
            "Name",
            "Author"});
            this.comboBoxFindField.Location = new System.Drawing.Point(13, 256);
            this.comboBoxFindField.Name = "comboBoxFindField";
            this.comboBoxFindField.Size = new System.Drawing.Size(75, 21);
            this.comboBoxFindField.TabIndex = 6;
            // 
            // textBoxFindValue
            // 
            this.textBoxFindValue.Location = new System.Drawing.Point(94, 255);
            this.textBoxFindValue.Name = "textBoxFindValue";
            this.textBoxFindValue.Size = new System.Drawing.Size(249, 20);
            this.textBoxFindValue.TabIndex = 7;
            // 
            // numericUpDownDelNumber
            // 
            this.numericUpDownDelNumber.Location = new System.Drawing.Point(192, 283);
            this.numericUpDownDelNumber.Maximum = new decimal(new int[] {
            9999,
            0,
            0,
            0});
            this.numericUpDownDelNumber.Minimum = new decimal(new int[] {
            1,
            0,
            0,
            0});
            this.numericUpDownDelNumber.Name = "numericUpDownDelNumber";
            this.numericUpDownDelNumber.Size = new System.Drawing.Size(94, 20);
            this.numericUpDownDelNumber.TabIndex = 8;
            this.numericUpDownDelNumber.Value = new decimal(new int[] {
            1,
            0,
            0,
            0});
            // 
            // buttonDelByNum
            // 
            this.buttonDelByNum.Location = new System.Drawing.Point(13, 280);
            this.buttonDelByNum.Name = "buttonDelByNum";
            this.buttonDelByNum.Size = new System.Drawing.Size(173, 23);
            this.buttonDelByNum.TabIndex = 9;
            this.buttonDelByNum.Text = "Удалить книгу под номером";
            this.buttonDelByNum.UseVisualStyleBackColor = true;
            this.buttonDelByNum.Click += new System.EventHandler(this.buttonDelByNum_Click);
            // 
            // buttonChangeBook
            // 
            this.buttonChangeBook.Location = new System.Drawing.Point(13, 310);
            this.buttonChangeBook.Name = "buttonChangeBook";
            this.buttonChangeBook.Size = new System.Drawing.Size(173, 23);
            this.buttonChangeBook.TabIndex = 10;
            this.buttonChangeBook.Text = "Изменить книгу под номером";
            this.buttonChangeBook.UseVisualStyleBackColor = true;
            this.buttonChangeBook.Click += new System.EventHandler(this.buttonChangeBook_Click);
            // 
            // numericUpDownChangeBook
            // 
            this.numericUpDownChangeBook.Location = new System.Drawing.Point(192, 313);
            this.numericUpDownChangeBook.Maximum = new decimal(new int[] {
            9999,
            0,
            0,
            0});
            this.numericUpDownChangeBook.Minimum = new decimal(new int[] {
            1,
            0,
            0,
            0});
            this.numericUpDownChangeBook.Name = "numericUpDownChangeBook";
            this.numericUpDownChangeBook.Size = new System.Drawing.Size(94, 20);
            this.numericUpDownChangeBook.TabIndex = 11;
            this.numericUpDownChangeBook.Value = new decimal(new int[] {
            1,
            0,
            0,
            0});
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(520, 339);
            this.Controls.Add(this.numericUpDownChangeBook);
            this.Controls.Add(this.buttonChangeBook);
            this.Controls.Add(this.buttonDelByNum);
            this.Controls.Add(this.numericUpDownDelNumber);
            this.Controls.Add(this.textBoxFindValue);
            this.Controls.Add(this.comboBoxFindField);
            this.Controls.Add(this.button5);
            this.Controls.Add(this.button4);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.dataGridView1);
            this.Name = "Form1";
            this.Text = "Form1";
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownDelNumber)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownChangeBook)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.DataGridView dataGridView1;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.Button button4;
        private System.Windows.Forms.Button button5;
        private System.Windows.Forms.ComboBox comboBoxFindField;
        private System.Windows.Forms.TextBox textBoxFindValue;
        private System.Windows.Forms.NumericUpDown numericUpDownDelNumber;
        private System.Windows.Forms.Button buttonDelByNum;
        private System.Windows.Forms.Button buttonChangeBook;
        private System.Windows.Forms.NumericUpDown numericUpDownChangeBook;
    }
}

