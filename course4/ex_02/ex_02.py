# Import SQLITE3 library
import sqlite3

# Establish connection with the database file, create file if non-existent
conn = sqlite3.connect('emaildb.sqlite')
# Create a cursor (database handle)
cur = conn.cursor()

# Drop table if it exists (optional) and create a new one
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

# Get a filename
fname = input('Enter file name: ')
# If none specified, choose a default one
if (len(fname) < 1): fname = 'mbox.txt'
# Create a file handle
fh = open(fname)
# Run a loop through the file
for line in fh:
    # Skip lines which don't start with 'From: '
    if not line.startswith('From: '): continue
    # Split lines into word lists
    pieces = line.split()
    # Choose second piece and assign it to email variable
    email = pieces[1]
    # Split the email with @
    email_s = email.split('@')
    # Choose second piece and assign it to an org variable
    org = email_s[1]
    # Select a table from database where ? is a placeholder replaced by org variable
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    # Grat the first row and assign it to row
    row = cur.fetchone()
    # If a row is not there insert a new org record and set count to 1
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
    # If a row exists update the count by 1
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))

# Commit changes to a database file (inside loop - slow, outside loop - faster)
conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC'
# For each selected row print its contents touple
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
# Close connection with database file
cur.close()
