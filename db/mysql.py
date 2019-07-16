import pymysql
from test_config import config

def get_db_conn():
    conn = pymysql.connect(host = config.DB_HOST, port = config.DB_PORT,user = config.DB_USER,passwd = config.DB_PASSWORD, db = config.DB_CLOUD)
    return conn

def query_db(sql):
    conn = get_db_conn()
    cur = conn.cursor() 
    cur.execute(sql)
    result = cur.fetchall() 
    cur.close() 
    conn.close()
    return result

def query_db_error_rollback(sql):
    conn = get_db_conn() 
    cur = conn.cursor()
    try:
        cur.execute(sql)
        conn.commit()
    except Exception as e:
        conn.rollback()
    finally:
        cur.close()
        conn.close()
