// bronze
// 일곱 난쟁이
#include<bits/stdc++.h>
#define fastio ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
using namespace std;

typedef long long int ll;

int main()
{
  fastio;
  int K[9],sum_temp=0,i,j;
  for(int i=0;i<9;i++)
  {
    cin>>K[i];
    sum_temp+=K[i];
  }
  sort(K,K+9);
  const int sum=sum_temp;
  for(i=0;i<8;i++)
  {
    int B=0;
    for(j=i+1;j<9;j++)
    {
      if(sum-(K[i]+K[j])==100)
      {
        B=1;
        break;
      }
    }
    if(B) break;
  }
  for(int l=0;l<9;l++)
  {
    if(i==l or j==l) continue;
    else cout<<K[l]<<"\n";
  }
}