#include <iostream>
#include <string>
using namespace std;

class Main_Class
{
  private:
    string name;
    string color;
  public:
    Main_Class()
    {
    }

    Main_Class(string data_name, string data_color)
    {
        name = data_name;
        color = data_color;
    }

    void message()
    {
        cout << "I'm a main class\n";
    }

    void setData(string data_name, string data_color)
    {
        name = data_name;
        color = data_color;
    }

    void getData()
    {
        cout << name << '\n' << color << '\n';
    }
  protected:
};

int main()
{
    Main_Class objMessage;
    objMessage.message();
    system("pause");
    return 0;
}
