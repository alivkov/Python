import mysql.connector
from difflib import get_close_matches
    
# Storing the Connection return string
conn =''
# Storing the Dictionary word Expression in a list
expression = []
    
def db_connection():
    
    con = mysql.connector.connect(
        user = 'ardit700_student',
        password = 'ardit700_student',
        host = '108.167.140.122',
        database = 'ardit700_pm1database'
    )
    return con
    
def db_query(flg,word=None):
    
    cursor = conn.cursor()
    if flg == 1:
        query = cursor.execute(f'SELECT * FROM Dictionary WHERE EXPRESSION = "{word[0]}" OR EXPRESSION = "{word[1]}" OR EXPRESSION = "{word[2]}" ')
    else:
        query = cursor.execute('SELECT DISTINCT EXPRESSION FROM Dictionary ORDER BY EXPRESSION')
    return cursor.fetchall()
    
def get_close(word,word_list):
    new_word_lst = []
    for item in word_list:
        new_word_lst.append(item[0])
    
    get_close_word = get_close_matches(word,new_word_lst)
    return get_close_word
    
def dictionary_sql(word):
    word_lst = [word.lower(), word.title(), word.upper()]
    
    result = db_query(1, word_lst)  # Sending flag 1 for the Word dictionary values
    
    if len(result) == 0:
    
        close_word = ','.join(get_close(word, expression))
        yn = input(f'Did you mean the below word/words \n{close_word}. \nEnter the correct word from the above list ')
        if yn != '':
            result = db_query(1, yn)
    return result
    
def user_input():
    while True:
        try:
            inp = input('Please enter a word for displaying the meaning or Press CTRL+D for EXIT: ')
            if not isinstance(inp, str):
                raise ValueError
            results = dictionary_sql(inp)
        except ValueError:
            print('Kindly enter the valid word')
            continue
        except EOFError:
            print('Thank you for using the Dictionary App')
            break
        else:
            if results:
                for result in results:
                    print(result[1])
            else:
                print('Not found')
    
conn = db_connection()
expression = db_query(0)
user_input()
