# newfile = open('newfile.txt', 'w+')

# string = 'this is the content that will be written to the text file'

# newfile.write(string)

# THE TOP IS HOW TO WRITE TO A BASIC TEXT FILE

# WE THEN INSTALLED A NEW PACKAGE - SIMPLEJSON

import simplejson as json
import os

if os.path.isfile('./ages.json') and os.stat('./ages.json').st_size != 0:
    old_file = open('./ages.json', 'r+')
    data = json.loads(old_file.read())
    print('Current age is ', data['age'], '--adding a year')
    data['age'] = data['age'] + 1
    print('New age ', data['age'])
else:
    old_file = open('./ages.json', 'w+')
    data = { 'name': 'Jonny', 'age': 32 }
    print('No file found, setting default to ', data['age'])

old_file.seek(0)
old_file.write(json.dumps(data))

