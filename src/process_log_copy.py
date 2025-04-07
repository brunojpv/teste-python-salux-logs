import psycopg2
import io

def process_log(logs):
    with psycopg2.connect("dbname=test user=postgres password=salux host=localhost port=5432") as conn:
        with conn.cursor() as cursor:
            buffer = io.StringIO()
            for log in logs:
                buffer.write(f"{log['timestamp']}\t{log['level']}\t{log['message']}\n")
            buffer.seek(0)
            cursor.copy_from(buffer, 'logs', sep='\t', columns=('timestamp', 'level', 'message'))
