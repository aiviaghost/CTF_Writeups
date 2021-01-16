org = "GTTAAAGTTTTCGGT{ACGACTTGCCCTACCTCTTTTATAGTGTCAACTAGGTGCGCATCCAGAATAACCACGATAACCTCTATAAAAACTCTGTCAATATTGTCTCGA}"

clean = "GTT AAA GTT TTC GGT { ACG ACT TGC CCT ACC TCT TTT ATA GTG TCA ACT AGG TGC GCA TCC AGA ATA ACC ACG ATA ACC TCT ATA AAA ACT CTG TCA ATA TTG TCT CGA }"

# googled for dna cryptography related things and found this
d = { # https://www.researchgate.net/publication/279978777_DNA_Cryptography
"A":"CGA", 
"K":"AAG", 
"U":"CTG", 
"0":"ACT", 
"B":"CCA", 
"L":"TGC", 
"V":"CCT", 
"1":"ACC", 
"C":"GTT", 
"M":"TCC", 
"W":"CCG", 
"2":"TAG", 
"D":"TTG", 
"N":"TCT", 
"X":"CTA", 
"3":"GCA", 
"E":"GGC", 
"O":"GGA", 
"Y":"AAA", 
"4":"GAG", 
"F":"GGT", 
"P":"GTG", 
"Z":"CTT", 
"5":"AGA", 
"G":"TTT", 
"Q":"AAC", 
" ":"ATA", 
"6":"TTA", 
"H":"ATG", 
"R":"TCA", 
",":"TCG", 
"7":"ACA", 
"I":"ATG", 
"S":"ACG", 
".":"GAT", 
"8":"AGG", 
"J":"AGT", 
"T":"TTC", 
":":"GCT" 
}

new_d = {v : k for k, v in d.items()}

out = ""
for c in clean.split():
    if c != "{" and c != "}":
        out += new_d[c]
    else:
        out += c
print(out)

# CYCTF{S0LV1NG PR08L3M5 1S 1N Y0UR DNA}
