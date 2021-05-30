import itertools

"""
Solution:
First we notice that the supplied ciphertext actually is not just the ciphertext, 
it is the ciphertext appended to the IV. This is because stdout.write() doesn't write a "\n" by default.
Like so:
    0c4ddce2fb0bceda4fc0c63f688e95e946defc77242eb3e8c1b6fbd768c5163632c8fd1988f69c47c20285bcfdf061a45ef0cbe52e3df226912b0121e4246ac6
    --------------------------------
                ^
                |
        This is the IV (32 bytes in hex)

We also note that the mode of operation is CBC (xor with previous ciphertext block). 

All we have to do to is find the inverse function to all the parts of the algorithm and call them in reverse order. 
(The actual code is something like AES but the s-boxes are weird, we can just "manually" invert them all. )
Ez flag!
In the end this is just a somewhat tricky implementation task, not really anything crazy crypto-wise. 
"""

class Decryptor:
    from encryptor import Encryptor # this way we don't have to scroll through all the tables :brain:
    enc_tables = Encryptor.tables

    # invert lookup tables
    tables = [[[0] * 256 for _ in range(16)] for _ in range(11)]
    for i in range(11):
        for y in range(4):
            for x in range(4):
                for k in range(256):
                    tables[i] [y * 4 + x] [
                        enc_tables[i][y * 4 + x][k]
                    ] = k
    
    # verify reverse-lookup works
    for i in range(11):
        for y in range(4):
            for x in range(4):
                for k in range(256):
                    assert(tables[i][y * 4 + x][enc_tables[i][y * 4 + x][k]] == k)
    

    def decrypt(self, ciphertext):
        self.cipher_state = [[x for x in ciphertext[4 * i : 4 * (i + 1)]] for i in range(4)]

        self.__unapply_table(self.cipher_state, self.tables[10])
        self.__unshift_rows(self.cipher_state)
        self.__unapply_table(self.cipher_state, self.tables[9])

        for i in range(8, -1, -1):
            self.__round_decrypt(self.cipher_state, self.tables[i])

        return bytes(itertools.chain(*self.cipher_state))

    def __unapply_table(self, state_matrix, table): # same as for encryption but with different tables
        for i in range(4):
            for j in range(4):
                state_matrix[i][j] = table[i * 4 + j][state_matrix[i][j]]

    def __unshift_rows(self, s):
        s[0][1], s[1][1], s[2][1], s[3][1] = s[3][1], s[0][1], s[1][1], s[2][1]
        s[0][2], s[1][2], s[2][2], s[3][2] = s[2][2], s[3][2], s[0][2], s[1][2] # same code as for encryption, interestingly it is it's own inverse
        s[0][3], s[1][3], s[2][3], s[3][3] = s[1][3], s[2][3], s[3][3], s[0][3]

    def __round_decrypt(self, state_matrix, table):
        self.__unmix_columns(state_matrix)
        self.__unshift_rows(state_matrix)
        self.__unapply_table(state_matrix, table)

    def __xtime(self, a):
        return (((a << 1) ^ 0x1B) & 0xFF) if (a & 0x80) else (a << 1)

    def __mix_single_column(self, a):
        t = a[0] ^ a[1] ^ a[2] ^ a[3]
        u = a[0]
        a[0] ^= t ^ self.__xtime(a[0] ^ a[1])
        a[1] ^= t ^ self.__xtime(a[1] ^ a[2])
        a[2] ^= t ^ self.__xtime(a[2] ^ a[3])
        a[3] ^= t ^ self.__xtime(a[3] ^ u)

    def __mix_columns(self, s):
        for i in range(4):
            self.__mix_single_column(s[i])

    # luckily the column-mixing is the same as for AES so we can just use https://github.com/boppreh/aes/blob/master/aes.py#L104
    def __unmix_columns(self, s):
        for i in range(4):
            u = self.__xtime(self.__xtime(s[i][0] ^ s[i][2]))
            v = self.__xtime(self.__xtime(s[i][1] ^ s[i][3]))
            s[i][0] ^= u
            s[i][1] ^= v
            s[i][2] ^= u
            s[i][3] ^= v

        self.__mix_columns(s)


def xor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))


ciphertext = bytes.fromhex("46defc77242eb3e8c1b6fbd768c5163632c8fd1988f69c47c20285bcfdf061a45ef0cbe52e3df226912b0121e4246ac6")
IV = bytes.fromhex("0c4ddce2fb0bceda4fc0c63f688e95e9")

dec = Decryptor()
decrypted_flag = b""
prev = IV
for i in range(0, len(ciphertext), 16): # CBC mode decrypt
    curr = dec.decrypt(ciphertext[i : i + 16])
    decrypted_flag += xor(prev, curr)
    prev = ciphertext[i : i + 16]

print(decrypted_flag.decode())
