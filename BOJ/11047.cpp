// silver 4
// 11047번, 동전 0
#include<bits/stdc++.h>
#define fastio ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
using namespace std;

int coin[11];

int main()
{
	fastio;
	int N, K, need_coin=0;
	cin >> N >> K;
	for (int i = 0; i < N; i++)
		cin >> coin[i];

	while (K != 0)
	{
		for (int i = N-1; i >=0; i--)
		{
			if (K >= coin[i])
			{
				K = K - coin[i];
				need_coin++;
				break;
			}
		}
	}
	cout << need_coin;
}