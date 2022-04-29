# Implement deleting data from tables by username of phone

import psycopg2

config = psycopg2.connect(
    host='localhost',
    database='postgres',
    user='postgres',
    password='e!_sUltan747'
)

current = config.cursor()

sql = '''
      DELETE FROM phonebook WHERE username = 'Allara';
'''


        
current.execute(sql)


current.close()
config.commit()
config.close()

  