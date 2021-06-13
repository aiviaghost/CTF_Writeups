from pwn import remote
from binascii import hexlify, unhexlify


def solve_PoW(target):
    from hashlib import sha256
    from binascii import hexlify, unhexlify
    from uuid import uuid4
    while True:
        x = uuid4().hex.encode("utf-8") # http://hkopp.github.io/2019/08/writeup-crypto-ctf
        hash_string = sha256(unhexlify(x)).hexdigest()[-5 : ]
        if hash_string == target:
            return x.decode("utf-8")


r = remote("challs.xmas.htsp.ro", "1004")


# PoW
PoW = r.recvline().decode("utf-8").strip()
r.recvline()
target = PoW[PoW.find("=") + 2 : ]
r.sendline(solve_PoW(target))
print("Solved PoW")


print(r.recvuntil("Choose what you want to do:\n"))
r.sendline("1")
r.recvuntil("Give me a message.\n")
r.sendline(hexlify(b'a' * 32)) # m || m
res = unhexlify(r.recvline().decode("utf-8").strip()[len("Here is your hash: b'") : -2])

def xor(a, b):
	return bytes([x ^ y for x, y in zip(a, b)])

xored = xor(res, b'a' * 16) # MAC ^ m

r.sendline("2")
r.recvuntil("Give me a message.\n")
r.sendline(hexlify(b'a' * 32)) # m || m
r.recvuntil("Give me a message.\n")
r.sendline(hexlify(b'a' * 32 + xored + xored + b'a' * 32)) # m || m || MAC ^ m || MAC ^ m || m || m
print(r.recvline())
print(r.recvline())
# X-MAS{C0l1i5ion_4t7ack5_4r3_c0o1!_4ls0_ch3ck_0u7_NSUCRYPTO_fda233}
