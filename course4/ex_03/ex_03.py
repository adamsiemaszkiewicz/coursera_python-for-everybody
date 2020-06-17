# Import XL ElementTree library
import xml.etree.ElementTree as ET
# Import SQLITE3 library
import sqlite3

# Establish a connection with the database file or create a new one
conn = sqlite3.connect('trackdb.sqlite')
# Create a database cursor (a file handle)
cur = conn.cursor()

# Drop tables if exist
cur.execute('DROP TABLE IF EXISTS Artist')
cur.execute('DROP TABLE IF EXISTS Genre')
cur.execute('DROP TABLE IF EXISTS Album')
cur.execute('DROP TABLE IF EXISTS Track')
# Make some fresh tables using executescript()
cur.executescript('''
CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

# Prompt for a filename or use default file when nothing specified
fname = input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'Library.xml'

# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>
def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None

# Create a file handle
fh = ET.parse(fname)
# Retrieve wanted data
all = fh.findall('dict/dict/dict')
# Print number of elements retrieved
print(len(all), ' records retrieved')

# Loop through the elements found
for entry in all:
    # Skip if no track ID
    if ( lookup(entry, 'Track ID') is None ) : continue

    # Assign entries into variables
    title = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    genre = lookup(entry, 'Genre')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')

    # Skip if variable is empty
    if title is None or artist is None or album is None or genre is None :
        continue
    # Print results
    print(title, artist, album, genre, count, rating, length)

    # Insert artist value into database or ignore if already exists
    cur.execute('''INSERT OR IGNORE INTO Artist (name)
        VALUES ( ? )''', ( artist, ) )
    # Select artist's foreign key (id)
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    # Assign the first record to aritst_id
    artist_id = cur.fetchone()[0]

    # Insert genre value into database or ignore if already exists
    cur.execute('''INSERT OR IGNORE INTO Genre (name)
        VALUES ( ? )''', ( genre, ) )
    # Select album's foreign key (id)
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
    # Assign the first record to album_id

    genre_id = cur.fetchone()[0]

    # Insert album value into database or ignore if already exists
    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id)
        VALUES ( ?, ? )''', ( album, artist_id ) )
    # Select album's foreign key (id)
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    # Assign the first record to album_id
    album_id = cur.fetchone()[0]

    # Insert new or update existing track with values from variables
    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count)
        VALUES ( ?, ?, ?, ?, ?, ? )''',
        ( title, album_id, genre_id, length, rating, count ) )

    # Commit changes to a database file (inside loop - slow, outside loop - faster)
    conn.commit()


# Close connection with database file
cur.close()
