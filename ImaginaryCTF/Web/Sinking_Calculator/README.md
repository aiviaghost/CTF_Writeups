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

