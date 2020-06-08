import mysql.connector
from difflib import get_close_matches
con = mysql.connector.connect(
        user = 'ardit700_student',
        password = 'ardit700_student',
        host = '108.167.140.122',
        database = 'ardit700_pm1database')

word = input('Enter a word: ')

def clmatch():
    cursor = con.cursor()
    matches = cursor.execute("SELECT DISTINCT Expression FROM Dictionary")
    db = []
    result = cursor.fetchall()
    for i in result:
        db.append(i[0])
    dym = get_close_matches(word, db)[0]
    print('Did you mean %s ?' % dym)
    
def search():
    cursor = con.cursor()
    query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word)
    result = cursor.fetchall()
    if result:
        for i in result:
            print(i[0])
    else:
        clmatch()
search()
