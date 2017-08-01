
import sys

N,L = [int(x) for x in input().split()]
m = []
D = []
for i in range(N):
    m.append(input().split())

for i in range(N):
    for j in range(N):
        if i == j:
            pass
        elif m[i][j] == m[j][i] and m[i][j] == '1':
            if not i+1 in D:
                D.append(int(i+1))
        elif m[i][j] != m[j][i]:
            print('Inconsistent')
            sys.exit()

if L == len(D):
    SD = sorted(D)
    for i in range(len(D)):
        sys.stdout.write(str(SD[i]) + ' ')
else:
    print('Ambiguous')
