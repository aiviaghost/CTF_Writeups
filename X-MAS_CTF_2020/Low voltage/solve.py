from pwn import remote
from binascii import hexlify, unhexlify
from math import gcd
from Crypto.Util.number import inverse
import os

def solve_PoW(target):
    from hashlib import sha256
    from uuid import uuid4
    while True:
        x = uuid4().hex.encode("utf-8") # http://hkopp.github.io/2019/08/writeup-crypto-ctf
        hash_string = sha256(unhexlify(x)).hexdigest()[-5 : ]
        if hash_string == target:
            return x.decode("utf-8")

def bin_exp(base, exp):
    res = 1
    while (exp > 0):
        if (exp & 1) == 1:
            res *= base
        base *= base
        exp >>= 1
    return res

r = remote("challs.xmas.htsp.ro", "1006")

# PoW
PoW = r.recvline().decode("utf-8").strip()
r.recvline()
target = PoW[PoW.find("=") + 2 : ]
r.sendline(solve_PoW(target))
print("Solved PoW")

print(r.recvuntil("that!\n"))
N = int(r.recvline().decode("utf-8").strip()[2 : ], 16)
e = 65537

m = b'aaaaaaaa'
hex_m = hexlify(m)
p, q = -1, -1
for i in range(63):
    print(i + 1)
    r.recvuntil("3. exit\n\n")
    r.sendline("1")
    r.recvuntil("you.\n\n")
    r.sendline(hex_m)
    signature = r.recvline().decode("utf-8").strip()[len("Here's the signature: ") : ]
    int_signature = int(signature, 16)
    t_p = gcd(bin_exp(int_signature, e) - int(hexlify(m), 16), N)
    t_q = N // t_p

    if t_p * t_q == N:
        phi = (t_p - 1) * (t_q - 1)
        d = inverse(e, phi)
        msg = int(hexlify(os.urandom(64)), 16)
        if msg == pow(pow(msg, d, N), e, N):
            p = t_p
            q = t_q
            break
        print("Failed signing!")
    else:
        print("Incorrect p and q", t_p, t_q)

assert(p * q == N)

print("Found!")
phi = (p - 1) * (q - 1)
d = inverse(e, phi)

r.recvuntil("3. exit\n\n")
r.sendline("2")
message = int(r.recvline().decode("utf-8").strip()[len("Give me the signature for this following message: b'") : -1], 16)

enc = pow(message, d, N)

assert(message == pow(enc, e, N))

r.sendline(hex(enc)[2 : ])

r.interactive()
# X-MAS{Oh_CPU_Why_h4th_th0u_fors4k3n_u5_w1th_b3llc0r3__th3_m4th_w45_p3rf3c7!!!_2194142af19aeea4}
