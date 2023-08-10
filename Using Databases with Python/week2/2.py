import sqlite3

conn = sqlite3.connect('orgdb.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Counts ')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')


fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox.txt"
fh = open(fname)
for line in fh:
    line = line.rstrip()
    if not line.startswith('From: '): continue
    words = line.split()
    email = words[1]
    domain = email.split('@')
    domains = domain[1]
    cur.execute('SELECT Count FROM Counts WHERE org = ?', (domains,))
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (domains,))
    else:
        cur.execute('UPDATE Counts SET Count = Count+1 WHERE org = ?', (domains,))
    conn.commit()

cur.close()






