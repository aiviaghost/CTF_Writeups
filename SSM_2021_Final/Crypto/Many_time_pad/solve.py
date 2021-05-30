
"""
Solution:
Main goal is to figure out what the key is because then we can just ask for the encrypted flag and xor it with the key. 
One thing to note about the encrypt() function is that is uses zip() which will stop at the length of the shortest of the two supplied sequences. 
Suppose we send a REALLY long string that we know, say s = "a" * 512. We will then get back s[ : len(key)] xor key. 
We can then xor again with s and now we have the key!
"""

def encrypt(msg, key):
    return bytes([a^b for a,b in zip(list(msg),list(key))])

enc = bytes.fromhex("d3e62ead7e34cc149b1915e1075bd0e81e32715e08aa95606ecedbd3eebce4f44ad735fee5ff97cde406f97539f19620e258de9e58d30129f867b81b287c4d6c9d60254a7d837d4f1cbbcac88eb53aa79c76598ebb1a960506f1688bb5558f6a5f1a6b1742d75273a6b869e6dc4365562dcbb928d424d3b50f12ee0efd0a11aef712543102c003e4a05fa05e4a8f342f073307e51f4aba5aa2214126e14ccdb178d7f49fe20e3e3adc0dfa6a6e7f6a4235a651c12221cf46647d06a5247bd3d0e67b8392dff25a1b25a86a1ba0af9ba4521ed4b903e3efce6e3fb8c895e354d754f4501d36bf389ce5f98b4b1e1650b00c2952ec4091e99cec771f04b61f7bf5")
msg = b"a" * 512

key = encrypt(enc, msg)

enc_flag = bytes.fromhex("e1d402b76665d82a994c1adf0809c7ba0d0c644d1cfe805e789ed183ffeee1a41fcb")

print(encrypt(enc_flag, key))
