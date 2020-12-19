from pwn import remote

def get_pairs(a, b):
    if b % a != 0:
        return 0
    
    n = b // a
    count = 0
    if (n & 1) == 0:
        count += 1
        while (n & 1) == 0:
            n //= 2
    
    i = 3
    while (i * i <= n):
        if n % i == 0:
            count += 1
            while n % i == 0:
                n //= i
        i += 2
    
    if n > 2:
        count += 1
    
    return 1 << count

r = remote("challs.xmas.htsp.ro", "6050")
r.recvuntil("90 seconds.\n\n")
for _ in range(100):
    print(r.recvline())
    l1 = r.recvline().decode("utf-8")
    l2 = r.recvline().decode("utf-8")
    a = int(l1[l1.find("=") + 2 : ])
    b = int(l2[l2.find("=") + 2 : ])
    r.sendline(str(get_pairs(a, b)))
    r.recvline()

print(r.recvline())
print(r.recvline())
