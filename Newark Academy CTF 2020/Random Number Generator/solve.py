'''
# nc challenges.ctfd.io 30264
'''

from pwn import connect
import time, random, numpy as np

r = connect("challenges.ctfd.io", "30264")
r.recvuntil("Quit\n\n")

r.sendline("r")
line = r.recvline().strip()
r.recvline()
target = int(line[2 : ].decode('utf-8'))
for t in np.arange((time.time() / 100) - 0.1, (time.time() / 100) + 0.1, 1e-5):
    random.seed(round(t, 5))
    rand = random.randint(1, 100000000)
    if rand == target:
        break

r.sendline("r")
test = r.recvline().strip()
r.recvline()
assert(int(test[2 : ].decode('utf-8')) == random.randint(1, 100000000))

r.sendline("g")
r.recvuntil("Enter your first guess:")
r.recvline()
r.sendline(str(random.randint(1, 100000000)))
print(r.recvline())
print(r.recvline())
r.sendline(str(random.randint(1, 100000000)))
print(r.recvline())
print(r.recvline())
