from base64 import b64encode, b64decode
from pwn import remote
from itertools import product

'''
Solution:
We notice that each block that gets encrypted using AES-ECB only contains 2 characters from the flag, the other 14 are null-bytes.
This means each ciphertext block only depends on those 2 characters in the corresponding plaintext. 
There are 128 characters in ASCII implying there are only 128^2 = 16384 different ciphertext blocks (and plaintext "blocks").
We can just send a giant request with all the combinations in sequence and the map each ciphertext block to the corresponding pair of characters.
Now we have a lookup table to decrypt the flag with. (Keep in mind each ciphertext block is 4 characters in this case but that doesn't change our strategy)
'''

FLAG = b64decode("2j0Rmerz7qZFLkTPXXJPt+OCyTB3vfN37R4Gh/VhRKVFLkTPXXJPt5XA3etzMeV+JkMPlPFVKYU=")

r = remote("35.217.22.54", "50000")
r.recvuntil("here is flag:")
r.recvline()

s = b"".join(bytes(list(pair)) for pair in product(range(128), range(128)))

r.recvuntil(">")
r.sendline(b64encode(s))
res = b64decode(r.recvline().decode().strip())

res = [res[i : i + 4] for i in range(0, len(res), 4)]

lookup = {res[i] : bytes(list(pair)) for i, pair in enumerate(product(range(128), range(128)))}

dec_flag = b""
for i in range(0, len(FLAG), 4):
    dec_flag += lookup[FLAG[i : i + 4]]

print(dec_flag.decode())
