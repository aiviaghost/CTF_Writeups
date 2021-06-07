import re

"""
The challenge itself is very simple, just create a string that matches all the requirements in the keygen.py file. 
I decided to automate this process to get some regex practice. 
"""

with open("keygen.py") as f:
    FLAG = list("SHELL{") + [""] * 100
    code = "".join(f.readlines()).replace("\n", "")
    reqs = re.compile('\[[0-9]{1,}\] {1,}== {1,}"[a-z0-9{}_]{1,}"').findall(code)
    for req in reqs:
        pos = int(req[req.find("[") + 1 : req.find("]")])
        c = req[-2]
        FLAG[pos] = c
    print("".join(FLAG))

# SHELL{s3nb0nzakur4_k4g3y05h1}
