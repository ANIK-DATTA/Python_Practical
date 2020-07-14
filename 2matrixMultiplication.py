X= [[1,2], [4,5]]
Y= [[4,7], [6,9]]
Z= [[0,0], [0,0]]
for i in range(len(X)):
	for j in range(len(Y[0])):
		for k in range(len(Y)):
			Z[i][j]+=X[i][k]*Y[k][j]

for r in Z:
	print(r)