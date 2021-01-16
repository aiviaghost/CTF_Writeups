# morsecode decoder from https://www.geeksforgeeks.org/morse-code-translator-python/

MORSE_CODE_DICT = { 'a':'.-', 'b':'-...', 'c':'-.-.', 
                    'd':'-..', 'e':'.', 'f':'..-.', 
                    'g':'--.', 'h':'....', 'i':'..', 
                    'j':'.---', 'k':'-.-', 'l':'.-..', 
                    'm':'--', 'n':'-.', 'o':'---', 
                    'p':'.--.', 'q':'--.-', 'r':'.-.', 
                    's':'...', 't':'-', 'u':'..-', 
                    'v':'...-', 'w':'.--', 'x':'-..-', 
                    'y':'-.--', 'z':'--..', '1':'.----', 
                    '2':'..---', '3':'...--', '4':'....-', 
                    '5':'.....', '6':'-....', '7':'--...', 
                    '8':'---..', '9':'----.', '0':'-----', 
                    ', ':'--..--', '.':'.-.-.-', '?':'..--..', 
                    '/':'-..-.', '-':'-....-', '(':'-.--.', 
                    ')':'-.--.-', '_':'..--.-', 
                    '{':'---...', 
                    '\'' : '.----.', '!' : '-.-.--', '@' : '.--.-.' # added manually via errors + https://morsecode.world/international/translator.html
                } 

def decrypt(message): 
    message += ' '
    decipher = '' 
    citext = '' 
    for letter in message: 
        if (letter != ' '): 
            i = 0
            citext += letter 
        else: 
            i += 1
            if i == 2 : 
                decipher += ' '
            else: 
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)] 
                citext = '' 
    return decipher 

# We figured it was some variation of morsecode. 
# Then we noticed that the characters "?M6" always came in sequence so this is either a "." or a "-" and "D" is the other one. 
# This was the correct mapping: 
weird_to_morse = { "?M6" : ".", "D" : "-" }

decoded = open("decoded.txt", "w")
f = open("flag.txt", "r")
for line in f:
    out = ""
    for i in range(len(line)):
        if line[i] == 'D':
            out += weird_to_morse[line[i]]
        elif line[i] == "?":
            out += weird_to_morse[line[i : i + 3]]
            i += 2
        elif line[i] == " ":
            out += " "
    decoded.write(decrypt(out) + "\n")

f.close()
decoded.close()

# cyctf{r3@d_b3tw33n_th3_l1n3s}
