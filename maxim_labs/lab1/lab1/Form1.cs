using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace lab1
{
    public partial class Form1 : Form
    {
        bool ready_for_calculating;
        Calculator calculator;

        public Form1()
        {
            InitializeComponent();
            calculator = new Calculator();
            ready_for_calculating = true;
        }

        private void bNumber_Click(object sender, EventArgs e)
        {
            if (ready_for_calculating == false)
            {
                Screen.Text = "";
                ready_for_calculating = true;
            }

            string number = (sender as Button).Text;

            if (number != "0" && number != ",")
            {
                if (Screen.Text == "0")
                    Screen.Text = "";
                Screen.Text += number;
            }
            else if (number == "0")
            {
                if (Screen.Text.Length > 1 || Screen.Text.Length == 0)
                {
                    Screen.Text += number;
                }
                else if (Screen.Text.Length == 1 && Screen.Text != "0")
                {
                    Screen.Text += number;
                }
            }
            else
            {
                if (Screen.Text.Length > 0 && !Screen.Text.Contains("."))
                {
                    Screen.Text += number;
                }
            }
        }

        private void bBinaryOperation_Click(object sender, EventArgs e)
        {
            if (ready_for_calculating)
            {
                if (Screen.Text.Length > 0)
                {
                    ready_for_calculating = false;
                    string operation = (sender as Button).Text;
                    if (calculator.Current_number == "")
                    {
                        calculator.Current_number = Screen.Text;
                        calculator.Current_operation = operation;
                    }
                    else
                    {
                        try
                        {
                            Screen.Text = calculator.Calculate(Screen.Text);
                            calculator.Current_operation = operation;
                        }
                        catch (DivideByZeroException)
                        {
                            Screen.Text = "Деление на ноль не возможно";
                        }
                        catch (MyException err)
                        {
                            Screen.Text = err.Message;
                        }
                    }
                }
            }
        }

        private void bUnaryOperation_Click(object sender, EventArgs e)
        {
            if (ready_for_calculating)
            {
                if (calculator.Current_number == "")
                {
                    if (Screen.Text.Length > 0)
                    {
                        try
                        {
                            calculator.Current_number = Screen.Text;
                            calculator.Current_operation = (sender as Button).Text;
                            Screen.Text = calculator.Calculate();
                        }
                        catch (MyException err)
                        {
                            Screen.Text = err.Message;
                            ready_for_calculating = false;
                        }
                    }
                }
            }
        }

        private void bEq_Click(object sender, EventArgs e)
        {
            if (calculator.Current_number != "")
            {
                if (ready_for_calculating)
                {
                    if (Screen.Text.Length > 0)
                    {
                        try
                        {
                            Screen.Text = calculator.Calculate(Screen.Text);
                            calculator.Current_number = "";
                        }
                        catch (DivideByZeroException)
                        {
                            Screen.Text = "Деление на ноль не возможно";
                            ready_for_calculating = false;
                        }
                    }
                }
            }
        }

        private void bClean_Click(object sender, EventArgs e)
        {
            Screen.Text = "";
            calculator.Current_number = "";
            calculator.Current_operation = "";
        }

        private void bDelete_Click(object sender, EventArgs e)
        {
            if (ready_for_calculating)
            {
                if (Screen.Text.Length > 0)
                {
                    Screen.Text = Screen.Text.Substring(0, Screen.Text.Length - 1);
                    if (Screen.Text == "-")
                    {
                        Screen.Text = "";
                    }
                }
            }
        }

        private void bChangeSign_Click(object sender, EventArgs e)
        {
            if (ready_for_calculating)
            {
                if (Screen.Text.Length > 0)
                {
                    if (Convert.ToDouble(Screen.Text) != 0)
                    {
                        if (Screen.Text.Contains("-"))
                        {
                            Screen.Text = Screen.Text.Substring(1);
                        }
                        else
                        {
                            Screen.Text = "-" + Screen.Text;
                        }
                    }
                }
            }
        }
    }

    public class Calculator
    {
        string current_number;
        string current_operation;

        public Calculator()
        {
            current_number = "";
            current_operation = "";
        }

        void Plus(string arg)
        {
            current_number = (Convert.ToDouble(current_number) + Convert.ToDouble(arg)).ToString();
        }

        void Minus(string arg)
        {
            current_number = (Convert.ToDouble(current_number) - Convert.ToDouble(arg)).ToString();
        }

        void Multiplication(string arg)
        {
            current_number = (Convert.ToDouble(current_number) * Convert.ToDouble(arg)).ToString();
        }

        void Division(string arg)
        {
            if (Convert.ToDouble(arg) != 0)
            {
                current_number = (Convert.ToDouble(current_number) / Convert.ToDouble(arg)).ToString();
            }
            else
            {
                throw new DivideByZeroException();
            }
        }

        public string Calculate(string arg)
        {
            try
            {
                switch (current_operation)
                {
                    case "+":
                        Plus(arg);
                        break;
                    case "-":
                        Minus(arg);
                        break;
                    case "*":
                        Multiplication(arg);
                        break;
                    case "/":
                        Division(arg);
                        break;
                    default:
                        throw new MyException("Такой бинарной операции не предусмотрено");
                }
            }
            catch (DivideByZeroException)
            {
                current_number = "";
                throw new DivideByZeroException();
            }
            catch (Exception err)
            {
                current_number = "";
                throw new MyException(err.Message);
            }
            finally
            {
                current_operation = "";
            }
            return current_number;
        }

        string Sqrt()
        {
            if (current_number.Contains("-"))
            {
                throw new MyException("Нельзя взять корень из отрицательного числа");
            }
            return (Math.Sqrt(Convert.ToDouble(current_number))).ToString();
        }

        string Square()
        {
            return (Convert.ToDouble(current_number) * Convert.ToDouble(current_number)).ToString();
        }

        public string Calculate()
        {
            string result;
            try
            {
                switch (current_operation)
                {
                    case "√":
                        result = Sqrt();
                        break;
                    case "x²":
                        result = Square();
                        break;
                    default:
                        throw new MyException("Такой унарной операции не предусмотрено");
                }
            }
            catch (DivideByZeroException)
            {
                throw new DivideByZeroException();
            }
            catch (Exception err)
            {
                throw new MyException(err.Message);
            }
            finally
            {
                current_number = "";
                current_operation = "";
            }
            return result;
        }

        public string Current_operation { get => current_operation; set => current_operation = value; }
        public string Current_number { get => current_number; set => current_number = value; }
    }

    public class MyException : Exception
    {
        public MyException()
        {
        }

        public MyException(string message) : base(message)
        {
        }
    }
}
