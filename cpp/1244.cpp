#include <iostream>

using namespace std;

int rev(int i)
{
    if (i == 1) return 0;
    return 1;
}

void change(int** list_ptr, int b_g, int val, int len) 
{
    int* list = *list_ptr;
    int i;
    if (b_g == 1) 
    {
        for (i = 0 ; i <= len ; i += val)
        {
            list[i] = rev(list[i]);
        }
    }
    else {
        list[val] = rev(list[val]);
        for (i = 1 ; val - i > 0 && val + i < len + 1 ; i++)
        {
            if (list[val - i] != list[val + i])
            {
                break;
            }
            list[val - i] = rev(list[val - i]);
            list[val + i] = rev(list[val + i]);
        }
    }
}

int main() 
{
    int n,m, i,b_g,val;
    cin >> n;

    int * list = new int[n+1];

    list[0] = -1;
    list[n+1] = -1;

    for (i = 1 ; i < n+1 ; i++) 
    {
        cin >> list[i];
    }
    cin >> m;
    for (i = 0 ; i < m ; i++) 
    {
        cin >> b_g >> val;
        change(&list, b_g, val, n+2);
    }
    for (i = 1 ; i < n+1 ; i++) 
    {
        cout << list[i];
        if (i % 20 == 0)
        {
            cout << endl;
        }
    }

}