#include <iostream>
#include <fstream>
#include <vector>
#include <utility>

using namespace std;

void sortare(vector<pair<int,char> > &v,int n)
{
    int i,j;
    pair <int,char> aux;
    for (i=0;i<n-1;i++)
        for (j=i+1;j<n;j++)
            if (v[i].first<v[j].first) {
                aux=v[i];
                v[i]=v[j];
                v[j]=aux;
    }
}

int main()
{
    int x,i,n,j;
    pair <int,char> p;
    pair <char,char> q;
    vector<pair<int,char> > v;
    vector<pair<char,char> > m;
    ifstream f("secventa.in");
    f>>n;
    for (i=0;i<n;i++) {
        f>>x;
        p.first=x;
        p.second=i+65;
        v.push_back(p);

    }
    
    sortare(v,n);
    for (i=0;i<n;i++)
    {
        j=i+1;
        while (v[i].first>0) {
            while (j<n && v[j].first==0) j++;
            if (j==n) {
                cout<<"Nu este secvente grafica";
                return 0;
            }
            v[j].first--;
            v[i].first--;
            q.first=v[i].second;
            q.second=v[j].second;
            m.push_back(q);
            j++;
        }
        j--;
        /* Explanation for below:
         There is a possibility that when we have two nodes with equal or Whitewood stables
         just one of them to be dropped
         and vector no longer be sortat.Pentru we could solve this sort again or we can apply vector
         the algorithm jos.Conditia v [j]! = 0 aims to not allow the program to move the last one left so
         i be higher than the position that if you are also acesta.De [j] == 0 is covered by the skip
         The above algorithm. */
        if (v[j].first!=0) while (j<n-1 && v[j].first<v[j+1].first) {
            p=v[j];
            v[j]=v[j+1];
            v[j+1]=p;
        }

    }
    ofstream g("secventa.out");
    for (i=0;i<m.size();i++) g<<"("<<m[i].first<<","<<m[i].second<<")"<<endl;
    cout<<"Secventa grafica(Muchiile sunt in fisierul secventa.out)";
    return 0;
}
