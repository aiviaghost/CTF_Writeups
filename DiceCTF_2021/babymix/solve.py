from z3 import *

vec = ""
for i in range(0, 0x16):
    vec += "pw[{}] ".format(i)

param_1 = BitVecs(vec, 8)

s = Solver()

s.add(param_1[8] + param_1[0xc] + (param_1[0xc] - param_1[0x11]) == 0x99)
s.add((param_1[2] ^ param_1[0x13]) + param_1[0x15] + param_1[10] == 0xd9)
s.add((param_1[0x10] ^ param_1[0]) + param_1[3] + param_1[0x10] + (param_1[0x10] ^ param_1[5]) == 0xe8)
s.add((param_1[0] ^ param_1[0x13]) + param_1[10] + param_1[3] + (param_1[3] - param_1[0x13]) == 0x148)
s.add((param_1[2] - param_1[0x13]) + (param_1[10] - param_1[8]) == 0x4a)
s.add((param_1[0x11] - param_1[9]) + param_1[4] + param_1[0xb] + (param_1[0x11] - param_1[1]) == 0xa6)
s.add(param_1[10] + param_1[5] + (param_1[0x12] - param_1[9]) + param_1[10] + param_1[0xe] == 0x19d)
s.add(param_1[0x15] + param_1[1] + (param_1[0xb] - param_1[2]) + (param_1[0x11] - param_1[0xd]) + (param_1[8] - param_1[0xc]) + (param_1[5] - param_1[0x10]) == 0x62)
s.add((param_1[0xc] ^ param_1[0x10]) + (param_1[6] - param_1[0xd]) + (param_1[0x11] - param_1[0xb]) + (param_1[0xd] ^ param_1[0x13]) == 0x55)
s.add((param_1[7] ^ param_1[2]) + (param_1[4] - param_1[0x10]) == 0x4d)
s.add(param_1[10] + param_1[7] + (param_1[0xe] ^ param_1[8]) + param_1[1] + param_1[5] + (param_1[0xe] - param_1[3]) + (param_1[8] - param_1[0x11]) == 0x180)
s.add(param_1[2] + param_1[0x11] + (param_1[0xf] - param_1[0x15]) + (param_1[2] - param_1[4]) + (param_1[4] - param_1[0]) == 0x109)
s.add(param_1[6] + param_1[7] + (param_1[0x15] - param_1[0x12]) + param_1[2] + param_1[0xf] + (param_1[0x11] - param_1[4]) + (param_1[5] - param_1[0x12]) == 0xfa)
s.add((param_1[0x12] ^ param_1[0xc]) + (param_1[7] - param_1[0x12]) + (param_1[0x15] - param_1[0x13]) + (param_1[0x10] - param_1[0x15]) == 0x4b)
s.add(param_1[6] + param_1[9] + (param_1[2] ^ param_1[10]) + param_1[7] + param_1[2] + param_1[0xd] + param_1[0x14] + (param_1[0x10] ^ param_1[3]) == 0x26d)
s.add((param_1[1] - param_1[0x13]) + (param_1[2] ^ param_1[0xe]) + param_1[0] + param_1[0xb] + (param_1[8] - param_1[3]) == 0x11b)
s.add((param_1[0xd] - param_1[0x13]) + (param_1[0xb] ^ param_1[0]) + (param_1[0xe] ^ param_1[0]) + (param_1[0x10] - param_1[0xe]) == 0x6a)
s.add((param_1[3] - param_1[0x12]) + (param_1[0] - param_1[0x14]) + param_1[0x13] + param_1[10] + param_1[10] + param_1[0x13] == 0x129)
s.add(param_1[0x12] + param_1[0x14] + (param_1[0] - param_1[0xf]) == 0x9c)
s.add((param_1[3] - param_1[0x11]) + (param_1[10] - param_1[0x14]) + (param_1[0xd] - param_1[8]) == 0x55)
s.add((param_1[10] - param_1[2]) + param_1[4] + param_1[0x13] + (param_1[0x11] ^ param_1[0xc]) + (param_1[3] - param_1[0x11]) == 0xa0)
s.add((param_1[0xc] - param_1[10]) + (param_1[0xb] - param_1[0x15]) == 0x24)
s.add((param_1[0x10] ^ param_1[5]) + (param_1[6] - param_1[0x10]) + (param_1[0x13] ^ param_1[0x12]) == 0x66)
s.add((param_1[0x15] - param_1[5]) + (param_1[6] - param_1[0xd]) + (param_1[0xf] ^ param_1[10]) == -0x30)
s.add((param_1[4] ^ param_1[6]) + (param_1[0xc] - param_1[0xb]) + (param_1[3] ^ param_1[5]) == 0x1d)
s.add((param_1[0x15] - param_1[0xb]) + (param_1[8] - param_1[0xf]) + (param_1[9] - param_1[2]) + (param_1[6] - param_1[0xe]) == -0x6d)
s.add(param_1[0x11] + param_1[0xb] + param_1[0] + param_1[0x10] + (param_1[0x13] - param_1[7]) == 0x169)
s.add((param_1[0x13] ^ param_1[0xf]) + param_1[0xf] + param_1[3] == 0x128)

print(s.check())
if (s.check() == sat):
    m = s.model()
    print(m)
    out = ""
    for i in param_1:
        if str(i):
            out += chr(m[i].as_long() % 128) # notice it is outside ascii range unless "% 128"
    print("dice{" + out + "}")

# dice{m1x_it_4ll_t0geth3r!1!}
