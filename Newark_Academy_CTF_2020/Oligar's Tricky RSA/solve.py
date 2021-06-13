from factordb.factordb import FactorDB as FDB
from Crypto.Util.number import inverse, long_to_bytes


c = 97938185189891786003246616098659465874822119719049
e = 65537
n = 196284284267878746604991616360941270430332504451383

f = FDB(n)
f.connect()
factors = f.get_factor_list()

phi = 1
for factor in factors:
    phi *= factor - 1

d = inverse(e, phi)

m = pow(c, d, n)

print(long_to_bytes(m))

# nactf{sn3aky_c1ph3r}
