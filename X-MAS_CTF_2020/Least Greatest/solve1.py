from pwn import remote

r = remote("challs.xmas.htsp.ro", "6050")

r.interactive()
