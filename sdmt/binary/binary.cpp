#include<iostream>
#include<algorithm>

using namespace std;
int binarys(int arr[],int l,int r,int num)
{
    if(r>=l)
    {
        int mid=(l+r)/2;
        if(arr[mid]==num)
            return mid;
        if(arr[mid]>num)
            return binarys(arr,l,mid-1,num);
        return binarys(arr,mid+1,r,num);
    }
    return -1;
}
void sortb(int a[],int n)
{
    for(int i=0;i<n-1;i++)
    {
        for(int j=i+1;j<n;j++)
        {
            if(a[i]>a[j])
            {
                int temp=a[i];
                a[i]=a[j];
                a[j]=temp;
            }
        }
    }
}
void disp(int arr[],int n)
{
    for(int i=0;i<n;i++)
        cout<<arr[i];
    cout<<endl;
}
int main()
{
    int n;
    cout<<"Enter the size of the array-";
    cin>>n;
    int a[n];
    for(int i=0;i<n;i++)
        cin>>a[i];
    int num;
    // use sort(a,a+n)  to simply sort without writing sort function
    disp(a,n);
    sortb(a,n);
    disp(a,n);
    cout<<endl<<"Enter the number to be searched-";
    cin>>num;
    int res=binarys(a,0,n-1,num);
    if(res==-1)
        cout<<endl<<"Element not found";
    else
        cout<<endl<<"Element found at index "<<res;
    return 0;
}
