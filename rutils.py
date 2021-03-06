#!/usr/bin/env python
"""
rutils.py - Phenny Utility Module
Copyright 2012, Sfan5
"""
import base64, binascii, re, random, time, multiprocessing

def rs(s):
    return repr(s)[1:-1]

def rev(phenny, input): 
    """reverse string"""
    for x in phenny.bot.commands["high"].values():
       if x[0].__name__ == "aa_hook":
           if x[0](phenny, input):
               return # Abort function
    if not input.group(2):
        return phenny.reply("Nothing to reverse.")
    q = input.group(2).encode('utf-8')
    s = ""
    for i in range(1,len(q)):
        s += q[-i]
    s += q[0]
    return phenny.say(rs(s))

rev.commands = ['rev','reverse']
rev.priority = 'low'

def b64e(phenny, input): 
    """base64 encode"""
    for x in phenny.bot.commands["high"].values():
       if x[0].__name__ == "aa_hook":
           if x[0](phenny, input):
               return # Abort function
    if not input.group(2):
        return phenny.reply("Nothing to encode.")
    q = input.group(2).encode('utf-8')
    try:
        return phenny.say(rs(base64.b64encode(q)))
    except BaseException as e:
        return phenny.reply("Failed to handle data")
   
b64e.commands = ['b64e','base64encode']
b64e.priority = 'low'

def b64d(phenny, input): 
    """base64 decode"""
    for x in phenny.bot.commands["high"].values():
       if x[0].__name__ == "aa_hook":
           if x[0](phenny, input):
               return # Abort function
    if not input.group(2):
        return phenny.reply("Nothing to decode.")
    q = input.group(2).encode('utf-8')
    try:
        return phenny.say(rs(base64.b64decode(q)))
    except BaseException as e:
        return phenny.reply("Failed to handle data")
   
b64d.commands = ['b64d','base64decode']
b64d.priority = 'low'

def b32e(phenny, input): 
    """base32 encode"""
    for x in phenny.bot.commands["high"].values():
       if x[0].__name__ == "aa_hook":
           if x[0](phenny, input):
               return # Abort function
    if not input.group(2):
        return phenny.reply("Nothing to encode.")
    q = input.group(2).encode('utf-8')
    try:
        return phenny.say(rs(base64.b32encode(q)))
    except BaseException as e:
        return phenny.reply("Failed to handle data")
   
b32e.commands = ['b32e','base32encode']
b32e.priority = 'low'

def b32d(phenny, input): 
    """base32 decode"""
    for x in phenny.bot.commands["high"].values():
       if x[0].__name__ == "aa_hook":
           if x[0](phenny, input):
               return # Abort function
    if not input.group(2):
        return phenny.reply("Nothing to decode.")
    q = input.group(2).encode('utf-8')
    try:
        return phenny.say(rs(base64.b32decode(q)))
    except BaseException as e:
        return phenny.reply("Failed to handle data")
   
b32d.commands = ['b32d','base32decode']
b32d.priority = 'low'

def b16e(phenny, input): 
    """base16 encode"""
    for x in phenny.bot.commands["high"].values():
       if x[0].__name__ == "aa_hook":
           if x[0](phenny, input):
               return # Abort function
    if not input.group(2):
        return phenny.reply("Nothing to encode.")
    q = input.group(2).encode('utf-8')
    try:
        return phenny.say(rs(base64.b16encode(q)))
    except BaseException as e:
        return phenny.reply("Failed to handle data")
   
b16e.commands = ['b16e','base16encode']
b16e.priority = 'low'

def b16d(phenny, input): 
    """base16 decode"""
    if not input.group(2):
        return phenny.reply("Nothing to decode.")
    q = input.group(2).encode('utf-8')
    try:
        return phenny.say(rs(base64.b16decode(q)))
    except BaseException as e:
        return phenny.reply("Failed to handle data")
   
b16d.commands = ['b16d','base16decode']
b16d.priority = 'low'

def crc32(phenny, input): 
    """crc32 hash"""
    for x in phenny.bot.commands["high"].values():
       if x[0].__name__ == "aa_hook":
           if x[0](phenny, input):
               return # Abort function
    if not input.group(2):
        return phenny.reply("Nothing to hash.")
    q = input.group(2).encode('utf-8')
    h = binascii.crc32(q)
    return phenny.say(rs(str(h) + "(" + hex(h) + ")"))
   
crc32.commands = ['crc32']
crc32.priority = 'low'

def hex_(phenny, input): 
    """hexlify http://docs.python.org/2/library/binascii.html#binascii.hexlify"""
    for x in phenny.bot.commands["high"].values():
       if x[0].__name__ == "aa_hook":
           if x[0](phenny, input):
               return # Abort function
    if not input.group(2):
        return phenny.reply("Nothing to hexlify.")
    q = input.group(2).encode('utf-8')
    try:
        return phenny.say(rs(binascii.hexlify(q)))
    except BaseException as e:
        return phenny.reply("Failed to handle data")
   
hex_.commands = ['hex']
hex_.priority = 'low'

def unhex(phenny, input): 
    """unhexlify http://docs.python.org/2/library/binascii.html#binascii.unhexlify"""
    for x in phenny.bot.commands["high"].values():
       if x[0].__name__ == "aa_hook":
           if x[0](phenny, input):
               return # Abort function
    if not input.group(2):
        return phenny.reply("Nothing to unhexlify.")
    q = input.group(2).encode('utf-8')
    try:
        return phenny.say(rs(binascii.unhexlify(q)))
    except BaseException as e:
        return phenny.reply("Failed to handle data")
   
unhex.commands = ['unhex']
unhex.priority = 'low'

def uuencode(phenny, input): 
    """uuencode"""
    for x in phenny.bot.commands["high"].values():
       if x[0].__name__ == "aa_hook":
           if x[0](phenny, input):
               return # Abort function
    if not input.group(2):
        return phenny.reply("Nothing to encode.")
    q = input.group(2).encode('utf-8')
    try:
        return phenny.say(rs(binascii.b2a_uu(q)))
    except BaseException as e:
        return phenny.reply("Failed to handle data")
   
uuencode.commands = ['ue','uuencode']
uuencode.priority = 'low'

def uudecode(phenny, input): 
    """uudecode"""
    for x in phenny.bot.commands["high"].values():
       if x[0].__name__ == "aa_hook":
           if x[0](phenny, input):
               return # Abort function
    if not input.group(2):
        return phenny.reply("Nothing to decode.")
    q = input.group(2).encode('utf-8')
    try:
        return phenny.say(rs(binascii.a2b_uu(q + '\n')))
    except BaseException as e:
        return phenny.reply("Failed to handle data")
   
uudecode.commands = ['ud','uudecode']
uudecode.priority = 'low'

def regex(phenny, input): 
    """regex"""
    for x in phenny.bot.commands["high"].values():
       if x[0].__name__ == "aa_hook":
           if x[0](phenny, input):
               return # Abort function
    if not input.group(2):
        return phenny.reply("Give me a regex and a message seperated by `")
    q = input.group(2).encode('utf-8')
    rgx = q[:q.find("`")]
    txt = q[q.find("`")+1:]
    if rgx == "" or txt == "":
        return phenny.reply("Give me a regex and a message seperated by `")
    try:
        r = re.compile(rgx)
    except BaseException as e:
        return phenny.reply("Failed to compile regex: " + e.message)
    q = multiprocessing.Queue()
    def compute(q, re, rgx, txt):
        q.put(list(e.groups()[0] for e in list(re.finditer(rgx, txt))))
    t = multiprocessing.Process(target=compute, args=(q,re,rgx,txt))
    t.start()
    t.join(3.0)
    if t.is_alive():
        phenny.reply("Regex took to long to compute")
        t.terminate()
        return
    m = q.get()
    if m == []:
        return phenny.say("false")
    else:
        return phenny.say("true groups=[" + ', '.join((repr(e) for e in m)) + "]")

regex.commands = ['re','regex']
regex.priority = 'low'
regex.thread = True

def rand(phenny, input): 
    """Returns a random number"""
    for x in phenny.bot.commands["high"].values():
       if x[0].__name__ == "aa_hook":
           if x[0](phenny, input):
               return # Abort function
    if not input.group(2):
        return
    arg = input.group(2)
    if " " in arg:
        try:
            a = int(arg.split(" ")[0])
        except ValueError:
            return phenny.reply("Could not parse argument 1")
        try:
            b = int(arg.split(" ")[1]) + 1
        except ValueError:
            return phenny.reply("Could not parse argument 2")
        if b < a:
            tmp = a
            a = b
            b = tmp
            del tmp
        phenny.say(str(random.randrange(a, b)))
    else:
        try:
            a = int(arg.split(" ")[0]) + 1
        except ValueError:
            return phenny.reply("Could not parse argument 1")
        phenny.say(str(random.randrange(a)))

rand.commands = ['rand', 'random']
rand.priority = 'low'

if __name__ == '__main__': 
   print __doc__.strip()
