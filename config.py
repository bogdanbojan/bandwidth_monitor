import psycopg2

connection = psycopg2.connect(
        database="bandwidth_monitor",
        user='postgres',
        password="password",
        host="localhost",
        port="5432")
print("Connected to the database successfully!")

cursor = connection.cursor()
