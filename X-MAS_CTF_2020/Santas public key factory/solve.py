from pwn import remote
from math import gcd
from Crypto.Util.number import inverse


def solve_PoW(target):
    from hashlib import sha256
    from binascii import hexlify, unhexlify
    from uuid import uuid4
    while True:
        x = uuid4().hex.encode("utf-8") # http://hkopp.github.io/2019/08/writeup-crypto-ctf
        hash_string = sha256(unhexlify(x)).hexdigest()[-5 : ]
        if hash_string == target:
            return x.decode("utf-8")


r = remote("challs.xmas.htsp.ro", "1000")

# PoW
PoW = r.recvline().decode("utf-8").strip()
r.recvline()
target = PoW[PoW.find("=") + 2 : ]
r.sendline(solve_PoW(target))
print("Solved PoW")


ii, jj = -1 , -1
seen = []
for i in range(255):
    print(i + 1)
    r.recvuntil("3. exit\n\n")
    r.sendline("1")
    secret = r.recvline().decode("utf-8").strip()
    r.recvline()
    # pubkey:
    n = int(r.recvline().decode("utf-8")[3 : ])
    r.recvline()
    seen.append((n, secret))
    should_break = False
    for j in range(len(seen)):
        if i != j and gcd(seen[i][0], seen[j][0]) != 1:
            print("Found a non coprime pair!")
            ii = i
            jj = j
            should_break = True
            break
    if should_break:
        break

n = seen[ii][0]
p = gcd(n, seen[jj][0])
q = n // p

assert(p * q == n)

e = 65537
phi = (p - 1) * (q - 1)
d = inverse(e, phi)
c = int(seen[ii][1][38 : -1], 16)
m = pow(c, d, n)

hex_m = hex(m)[2 : ]

r.recvuntil("3. exit\n\n")
r.sendline("2")
r.recvuntil("got.\n\n")

r.sendline(hex_m)

r.interactive()
