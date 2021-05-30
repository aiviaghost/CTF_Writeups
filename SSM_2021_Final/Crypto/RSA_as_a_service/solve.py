from pwn import remote
from Crypto.Util.number import long_to_bytes

"""
Overview:
    - We can send a ciphertext C and get the corresponding plaintext m % 10000 (last 4 digits)
    - We can view this as a parity oracle, i.e. whether m is even or odd

Solution:
RSA has an interesting property, the homomorphic property that multiplication of the message m is the same as multiplication of the ciphertext, like this:
    RSA(m1) * RSA(m2) = (m1 ^ e mod n) * (m2 ^ e mod n) = (m1 * m2) ^ e mod n = RSA(m1 * m2)

If we send 2 * C to the server we will get the parity of 2 * m. 
Suppose 0 <= m <= N / 2:
    This case implies 0 <= 2 * m <= N which is an even number
Suppose N / 2 < m < N:
    This case implies N < 2 * m < 2 * N, which simplifies to 0 < 2 * m - N < N (we want to stay between 0 and N because everything is mod N)
    2 * m - N is odd because N is odd. (N is the product of 2 primes which is odd as long as neither of the primes are 2)

We can use the above mentioned cases to binary search for m. 
"""

N = 2067870294958011057055285955402906046606048790411055875169573453537686332172209267408004747919606628058370206526960367880892445668185569509285031022814760278300660074538992941238982588619494964193409210892923688858242586013830561156541927776274966180885997095053592128354967440372151112352802070424021271867709873
e = 65537

C = 830144780125940486197043594519402775647010555742811842359207814917520372239224390038268506983945590914017447501759733518435739075026545060636422666418129968749711859639488111365290895840446401503036619441634142308550050624037073448524383606576227140182555712049129024301943559994704154884416671330162459299359164
c = pow(2, e, N)

itr = 0
lb, rb, mid = 0, N, -1
while lb < rb:
    mid = (lb + rb) // 2
    r = remote("35.217.51.136", "50000")
    r.sendline(str((C * c) % N))
    r.recvuntil("Message to decrypt (decimal): ")
    r.recvuntil("Decrypted message: \n")
    lsb = int(r.recvline().decode().strip().replace("#", ""))
    r.close()
    c = (c * pow(2, e, N)) % N
    if lsb % 2 == 0:
        rb = mid
    else:
        lb = mid
    itr += 1

print(f"Queries: {itr}")
print(f"Flag: {long_to_bytes(mid)}")

# SSM{n0_n33d_f0r_pr3m1um_m3mb3r5hip}
