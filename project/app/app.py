from flask import Flask
import redis
import socket
import os
import MySQLdb

app = Flask(__name__)
#连接redis
r = redis.Redis(host='redis',port=6379,db=0,decode_responses=True)
#连接mysql
def get_db_connection():
    return MySQLdb.connect(
            host="db",
            user="root",
            passwd=os.environ.get("MYSQL_ROOT_PASSWORD"),
            db="testdb"
            )
@app.route('/')
def hello():
    count = r.incr('hits')
    container_id = socket.gethostname()
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO access_log (container_id) VALUES (%s)",(container_id,))
        conn.commit()
        conn.close()
        db_status = "MySQL Write Success"
    except Exception as e:
        db_status = f"Mysql Error:{str(e)}"

    return f"Container: {container_id} | Redis Count: {count} | {db_status}\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8000)
