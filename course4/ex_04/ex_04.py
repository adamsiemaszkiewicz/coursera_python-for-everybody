# Import JSON library
import json
# Import SQLITE library
import sqlite3

# Establish a connection to a database file or create a new file
conn = sqlite3.connect('rosterdb.sqlite')
# Create a connection curson
cur = conn.cursor()

# Drop the database tables if exist and create new ones
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

# Prompt for a file name
fname = input('Enter file name: ')
# Use default file if none specified
if len(fname) < 1:
    fname = 'roster_data.json'

# [
#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],

# Read JSON file and load the content
str_data = open(fname).read()
json_data = json.loads(str_data)

# Run through entires of JSON file
for entry in json_data:

    # Assign 1st, 2nd and 3rd lsit positions to respective variables
    name = entry[0]
    title = entry[1]
    role = entry[2]

    # Print the variables
    print((name, title, role))

    # Insert 'name' value into User table
    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES ( ? )''', ( name, ) )
    # Select id of a certain name (auto-generated)
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    # Assign the user id found to the variable
    user_id = cur.fetchone()[0]

    # Insert 'title' value into Course table
    cur.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES ( ? )''', ( title, ) )
    # Select id of a certain title (auto-generated)
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    # Assign the title id found to the variable
    course_id = cur.fetchone()[0]

    # Insert new or update existing user-course touple
    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role) VALUES ( ?, ?, ? )''',
        ( user_id, course_id, role ) )

# Commit changes
conn.commit()
# Close connection with database file
cur.close()
