k, m, n = map(int, input().split(' '))

ans = (k*m + k*n + m*n/2 + k*(k-1)/2 + m*(m-1)/2*3/4) / ((k+m+n) * (k+m+n-1) / 2)

# print(ans)
print("%.5f"%ans)