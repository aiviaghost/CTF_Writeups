from pwn import remote


def M_mult(N, a, b):
	res = [[0] * N for _ in range(N)]
	for i in range(N):
		for j in range(N):
			for k in range(N):
				res[i][j] = (res[i][j] + a[i][k] * b[k][j]) % 666013
	return res

def M_exp(N, M, L):
	res = [[0] * N for _ in range(N)]
	for i in range(N):
		res[i][i] = 1
	
	while (L > 0):
		if (L & 1) == 1:
			res = M_mult(N, res, M)
		M = M_mult(N, M, M)
		L >>= 1
	return res


r = remote("challs.xmas.htsp.ro", "6053")

r.recvuntil("mean!?\n\n")

for _ in range(40):
	# r.recvline()
	print(r.recvline())

	N = int(r.recvline().decode("utf-8")[4 : ])
	r.recvline()

	adj = []
	for _ in range(N):
		adj.append([int(j) for j in r.recvline().decode("utf-8").split(",")])

	forbidden_line = r.recvline().decode("utf-8").strip()[len("forbidden nodes: [") : -1]
	# forbidden = [int(i) - 1 for i in forbidden_line.split(",")] if (len(forbidden_line) > 0) else []

	L = int(r.recvline().decode("utf-8")[4 : ])
	r.recvline()
	'''
	for i in range(N):
		for j in range(N):
			if i in forbidden or j in forbidden:
				adj[i][j] = 0
	'''
	res = M_exp(N, adj, L)
	path_count = res[0][N - 1]
	r.sendline(str(path_count))
	r.recvline()

# flag: X-MAS{n0b0dy_3xp3c73d_th3_m47r1x_3xp0n3n71a7i0n}
print(r.recvline())
print(r.recvline())
