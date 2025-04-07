import psycopg2

def process_log(logs):
    with psycopg2.connect("dbname=test user=postgres password=salux host=localhost port=5432") as conn:
        with conn.cursor() as cursor:
            query = "INSERT INTO logs (timestamp, level, message) VALUES (%s, %s, %s)"
            valores = [(log['timestamp'], log['level'], log['message']) for log in logs]
            cursor.executemany(query, valores)
