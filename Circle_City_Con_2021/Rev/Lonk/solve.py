from functools import reduce

"""
Solution:
I started off by reversing the simplest function in the lib-file, the ones that didn't call other functions. 
I noticed "非" contained a "normal" number and given the code I figured that it just created an instance 
representing the argument-number. (I figured the 我-class was some sort of recursive structure given the 
context it was used in). Now things start to become clear quite quickly, especially since we can test functions 
with the knowledge that the inputs are just numbers in a weird format. It was pretty clear that 常 did the opposite 
of 非, it converted the recursive structure to a number. After 要 (add) and 放 (subtract) one can guess, and correctly do so, 
that the rest of the functions implement multiplication, modulo, exponentiation and modular exponentiation. Finally it 
is clear what flag.py does. The smart thing to do now is to just replace the function calls with reasonable functions 
but for some reason I didn't realize this during the CTF, I just "parsed" the flag-file by hand as seen below. 
"""

def P(n):
    print(chr(n), end="")

P(67)
P(34 + 33)
P(105 - 58 + 20)
P(3 * 41)
P(811 % 234)
P(pow(3, 5, 191))
P(((2 ** 12) % 1337) - 1)
P(((pow(3, 9, 555) * 2) - 464) * 2)
P(pow(2020, 451813409, 2350755551))
P(pow(1234567890, 9431297343284265593, 119 + 17017780892086357584))
P(pow(3, 60437 - 1024, 151553) * pow(3, 54103 + 5 * (10 * 10 * 10 * 10 * 10 % 1337), 151553))
P(pow(111111111111111111111111111111111111, 222222222222222222222222222222222222, 333333333333333333333333333333333333) + 2 * 2 * 29)
P((((1 + 1) * (1 + 1)) ** 2 - 8) * pow(2, 7262490, 98444699))
P(1337 * 1337 * 1337 * 1337 - 3195402929666)
P(((1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 - 1) % 100) - 23)
P(((pow(100, 100, 100) - 1) % 100) - 50)
P((1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 13 + 14 + 15 + 16 + 17 + 18 + 19 + 20) % 132)
P((pow(1337, 1337, 1337 + 1337) - 1336) + 106)
P(50 + 1)
P(((pow(pow(pow(10, 10, 100), 10, 100), 10, 100) - 1) % 100) + 1)
P(((55555 ** 5 - reduce(lambda x, y: (x * y) % 1337, range(1, 24))) % 1337) - 200 + 45)
P(pow(6, 11333, 29959))
P(4 * 4 * 4 * 4 * 4 - 975)
P((3 + 3 - 1 + 4 - 3) ** 2)
P(pow(pow(12345, 12345, 54321), 12345, 54321) - 3037)
P(50 + 3)
P(125)
# CCC{m4Th_w1tH_L1Nk3d_l1$t5}
