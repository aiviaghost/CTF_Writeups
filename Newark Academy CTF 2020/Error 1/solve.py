from functools import reduce


with open("enc.txt", "r") as f:
    enc = f.readline()
    enc = [enc[i : i + 15] for i in range(0, len(enc), 15)]
    print(enc[0])
    fixed = []
    for e in enc:
        grid = [[0] * 4 for _ in range(4)]
        for i in range(1, 16):
            grid[int(i / 4)][i % 4] = e[i - 1]
        
        col, row = -1, -1

        # column 1
        valid1 = True
        parity = int(grid[0][3])
        for i in range(1, 4):
            parity += int(grid[i][1])
            parity += int(grid[i][3])
        if parity % 2 != int(grid[0][1]):
            valid1 = False
        
        # column 2
        valid2 = True
        parity = int(grid[0][3])
        for i in range(1, 4):
            parity += int(grid[i][2])
            parity += int(grid[i][3])
        if parity % 2 != int(grid[0][2]):
            valid2 = False
        
        if valid1 and valid2:
            col = 0
        elif valid1 and not valid2:
            col = 2
        elif not valid1 and valid2:
            col = 1
        else:
            col = 3

        # row 1
        valid3 = True
        parity = int(grid[3][0])
        for i in range(1, 4):
            parity += int(grid[1][i])
            parity += int(grid[3][i])
        if parity % 2 != int(grid[1][0]):
            valid3 = False

        # row 2
        valid4 = True
        parity = int(grid[3][0])
        for i in range(1, 4):
            parity += int(grid[2][i])
            parity += int(grid[3][i])
        if parity % 2 != int(grid[2][0]):
            valid4 = False

        if valid3 and valid4:
            row = 0
        elif valid3 and not valid4:
            row = 2
        elif not valid3 and valid4:
            row = 1
        else:
            row = 3

        grid[row][col] = str(1 - int(grid[row][col]))

        flat = []
        for sublist in grid:
            for item in sublist:
                flat.append(item)
        print(''.join(str(flat[i]) for i in range(1, len(flat)) if i not in [1, 2, 4, 8]))
        for i in range(1, 16):
            if i not in [1, 2, 4, 8]:
                fixed.append(flat[i])

    def binaryToAscii(s): # luckily I did cryptopals a while back so I have already made one of these functions
        return ''.join([chr(int(s[i : i + 8], base=2)) for i in range(0, len(s), 8)])

    print(binaryToAscii(''.join(map(str, fixed))))
