import mysql.connector
from difflib import get_close_matches


con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)

def db_query(flg, word):
    if flg == 1:
        cursor = con.cursor()
        query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word)
        results = cursor.fetchall()
    else: 
        cursor = con.cursor()
        keys = cursor.execute("SELECT Expression FROM Dictionary")
        results = cursor.fetchall()

def usr_input():
    while True:
        word=input("Enter the word: ")
        if word == "**q":
            break
        elif len(get_close_matches(word, keys)) > 0:
            yn = input("Did you mean %s instead? Y for yes and N for no: " % get_close_matches(word, keys)[0])
            if yn.lower() == "y":
                return keys[get_close_matches(word, keys)[0]]
            elif yn.lower() == "n":
                return "The word does not exist. Please try again."
            else:
                return "Your query is BS."
        elif results:
            for result in results:
                print(result[0])
            break  
        else:
            print("No word found!")

usr_input()
