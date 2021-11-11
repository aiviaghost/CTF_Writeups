from Crypto.Util.number import getPrime, bytes_to_long
from secure_secrets import p, q

e = 3

n = p * q

m = bytes_to_long(b"XXXXXXXXXXXXXXXXXX")

c = pow(m, e, n)

print(f"c = {c}")
print(f"n = {n}")
