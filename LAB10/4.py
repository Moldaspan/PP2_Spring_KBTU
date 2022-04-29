# Querying data from the tables (with different filters)

import psycopg2

config = psycopg2.connect(
    host='localhost',
    database='postgres',
    user='postgres',
    password='e!_sUltan747'
)

current = config.cursor()

sql = '''
    INSERT INTO phonebook VALUES (894, 'kenny', 'asd@gnai.com', 'fghj');
'''

sql2 = '''
    UPDATE phonebook SET username = 'allara' WHERE id = 894;
'''

current.execute(sql)
current.execute(sql2)

current.close()
config.commit()
config.close()