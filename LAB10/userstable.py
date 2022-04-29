import psycopg2

config = psycopg2.connect(
    host='localhost', 
    database='postgres',
    port=5432,
    user='postgres',
    password='e!_sUltan747'
)

current = config.cursor()

current.execute(
    '''
    CREATE TABLE users_snake2(
        username VARCHAR(20) PRIMARY KEY,
        score INTEGER,
        highscore INTEGER,
        level INTEGER
    )
    '''
)

config.commit()
current.close()
config.close()