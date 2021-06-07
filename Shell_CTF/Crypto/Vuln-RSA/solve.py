from pwn import remote
from base64 import b64decode

"""
Standard byte-at-a-time ECB decryption. 
See https://github.com/Bumbodosan/tenable2021/blob/main/Netrunner-Encryption/solve.py for a decent explanation. 
Keep in mind that the ciphertext has the format E("sixteen byte AES") || E("shell{...}") so we need to skip the first 16 bytes. 
"""

def create_lookup(known_msg):
    lookup = {}
    for i in range(128):
        r = remote("34.92.214.217", "8885")
        r.sendline("a" * (15 - len(known_msg)) + known_msg + chr(i))
        enc = b64decode(r.recvline()[len("Crewmate! enter your situation report: ") : ].decode().strip())[16 : 32]
        lookup[enc] = chr(i)
        r.close()
    return lookup


with open("flag.txt", "a") as f:
    FLAG = ""
    for i in range(0, 1000, 16):
        for j in range(16):
            r = remote("34.92.214.217", "8885")
            r.sendline("a" * (15 - j))
            enc = b64decode(r.recvline()[len("Crewmate! enter your situation report: ") : ].decode().strip())[16 + i : 16 + i + 16]
            lookup = create_lookup(FLAG[-15 : ])
            FLAG += lookup[enc]
            f.write(lookup[enc])
            r.close()
