#include<iostream>
#include<stdlib.h>
#include<stdio.h>
using namespace std;
string encrypt(string str,int shift)
{
    char ch=' ';
    string result="";
    int len=str.length();
    for(int i=0;i<len;i++)
    {
        if(isspace(str[i]))
            result+=ch;
        else if(isupper(str[i]))
            result+=char(int(str[i]+shift-65)%26+65);
        else
            result+=char(int(str[i]+shift-97)%26+97);
    }
    return result;
}
string decrypt(string str,int shift)
{
    string result="";
    char ch=' ';
    int len=str.length();
    for(int i=0;i<len;i++)
    {
        if(isspace(str[i]))
            result+=ch;
        else if(isupper(str[i]))
            result+=char(int(str[i]-shift-65)%26+65);
        else
            result+=char(int(str[i]-shift-97)%26+97);
    }
    return result;
}

int main()
{
    string s;
    cout<<"enter the string-";
    getline(cin,s);
    int num;
    cout<<endl<<"Enter the number of bits to shift-";
    cin>>num;
    string cipher=encrypt(s,num);
    cout<<endl;
    cout<<cipher<<endl<<endl;
    cout<<"The decrypted text is-"<<decrypt(cipher,num);
    return 0;
}
