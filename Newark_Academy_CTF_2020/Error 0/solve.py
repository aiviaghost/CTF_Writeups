import binascii, base64

with open("enc.txt", "r") as f:
    stuff = f.readline()
    arr = []
    for i in range(232, len(stuff), 232):
        arr.append(stuff[i - 232 : i])
        last = i
    
    res = ""
    for i in range(len(arr[0])):
        ones = 0
        zeros = 0
        for j in range(len(arr)):
            if arr[j][i] == "1":
                ones += 1
            else:
                zeros += 1
        
        if zeros < ones:
            res += "1"
        else:
            res += "0"
    
    print(res)
    # res = 0110111001100001011000110111010001100110011110110110111000110000001100010111001101111001010111110110111000110000001100010011001101101010010111110111110001011100011111000010100000101001011111000010010000100111001011110111110100001010
    # use cyberchef "from binary" > nactf{n01sy_n013j_|\|()|$'/}