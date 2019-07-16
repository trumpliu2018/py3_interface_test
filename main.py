from login import login
from db import mysql

if __name__ == '__main__':
    # token = login.login()
    # logger.logging.info("login success and token is :", token)
    result = mysql.query_db("select * from amway_poc")
    print(result)
    
