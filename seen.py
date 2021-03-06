#!/usr/bin/env python
"""
seen.py - Phenny Seen Module
Copyright 2008, Sean B. Palmer, inamidst.com
Modified by sfan5 2013
Licensed under the Eiffel Forum License 2.

http://inamidst.com/phenny/
"""

import time
from tools import deprecated
from thread import start_new_thread, allocate_lock
import sqlite3

updates = list()
update_l = allocate_lock()

def opendb():
    db = sqlite3.connect("seen.sqlite")
    return db

def updatethread():
    global updates, update_l
    db = opendb()
    c = db.cursor()
    while True:
        if len(updates) > 0:
            update_l.acquire()
            up = updates
            updates = list()
            update_l.release()
            for u in up:
                c.execute("SELECT * FROM seen WHERE nick = ?", (u[2],))
                if c.fetchone() != None:
                    d = (u[0], u[1], u[2])
                    c.execute('UPDATE seen SET channel = ?, time = ? WHERE nick = ?', d)
                else:
                    d = (u[2], u[0], u[1])
                    c.execute('INSERT INTO seen VALUES (?,?,?)', d)
            db.commit()
        else:
            time.sleep(5)

def pushupdate(sender, time, nick):
    update_l.acquire()
    updates.append((sender, time, nick))
    update_l.release()

def seen(phenny, input): 
    """.seen <nick> - Reports when <nick> was last seen."""
    for x in phenny.bot.commands["high"].values():
        if x[0].__name__ == "aa_hook":
            if x[0](phenny, input):
                return # Abort function
    nick = input.group(2)
    if not nick:
        return phenny.reply("Need a nickname to search for...")
    nick = nick.lower()

    print("[LOG]: %s queried Seen Result for %s" % (input.nick,nick))

    db = opendb()
    c = db.cursor()
    c.execute("SELECT channel, time FROM seen WHERE nick = ?", (nick,))
    r = c.fetchone()
    c.close()
    db.close()
    if r:
        channel, t = r[0], r[1]
        t = time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime(t))

        msg = "%s was last seen at %s on %s" % (nick, t, channel)
        phenny.reply(msg)
    else:
        phenny.reply("Sorry, I haven't seen %s around." % nick)

seen.rule = (['seen'], r'(\S+)')

def note(phenny, input):
    if input.sender.startswith('#'):
        pushupdate(input.sender, int(time.time()), input.nick.lower())

note.rule = r'.*'
note.priority = 'low'

def note_join(phenny, input):
    if input.sender.startswith('#'):
        pushupdate(input.sender, int(time.time()), input.nick.lower())

note_join.rule = r'.*'
note_join.event = 'JOIN'
note_join.priority = 'low'

def note_part(phenny, input):
    if input.sender.startswith('#'):
        pushupdate(input.sender, int(time.time()), input.nick.lower())

note_part.rule = r'.*'
note_part.event = 'PART'
note_part.priority = 'low'

db = sqlite3.connect("seen.sqlite")
c = db.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS seen (nick text, channel text, time int)''')
c.close()
db.close()

start_new_thread(updatethread, ())

if __name__ == '__main__': 
   print __doc__.strip()
