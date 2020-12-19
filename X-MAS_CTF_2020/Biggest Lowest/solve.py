from pwn import remote

r = remote("challs.xmas.htsp.ro", "6051")
r.recvuntil("3; 10, 9, 8\n\n")

for _ in range(50):
    r.recvline()
    nums = [int(i) for i in r.recvline().decode("utf-8").strip()[len("array = [") : -1].split(", ")]
    k1 = int(r.recvline().decode("utf-8").strip()[len("k1 = ") : ])
    k2 = int(r.recvline().decode("utf-8").strip()[len("k2 = ") : ])
    sorted_array = sorted(nums)
    # print(nums, k1, k2)
    # print(", ".join(map(str, sorted_array[ : k1])) + "; " + ", ".join(map(str, reversed(sorted_array[-k2  : ]))))
    r.sendline(", ".join(map(str, sorted_array[ : k1])) + "; " + ", ".join(map(str, reversed(sorted_array[-k2 : ]))))
    r.recvline()

r.interactive()
