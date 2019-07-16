# python3 unit test 接口自动化框架 


## 1. Installation:

### 1.1 virtualenv
python3 环境
使用virtualenv 进行环境隔离.

pip3 install virtualenv

virtualenv --no-site-packages interface_test

### 1.2 dependency

pip3 isntall urllib
pip3 install pymysql


## 2. 功能实现

 基于python3， 实现了如下接口自动化功能
 
### 2.1 测试用例

目录：t/InterfaceTest/interface_test/test_suite
 
- TestSuite
      测试集或测试套件，测试用例的集合，用来组织用例，支持嵌套
- TestLoader
      用例加载器，用于向TestSuite中添加用例
- TestDiscover
     用例发现, 用于加载文件目录下的用例
   
### 2.2 测试报告
目录: /Users/trump/InterfaceTest/InterfaceTest/interface_test/test_report

- 文本报告: 
	 test_B (test_case.test1.TestClass1) ... ok
	test_a (test_case.test1.TestClass1) ... ok
	test_B2 (test_case.test2.TestClass2) ... ok
	test_a2 (test_case.test2.TestClass2) ... ok
	
	Ran 4 tests in 0.028s
	
	OK
	
- html 报告

### 2.3日志

目录：/Users/trump/InterfaceTest/InterfaceTest/interface_test/core/logger.py
usage:

``` python
from core import logger
logger.logging.info(login_url)
```

### 2.4邮件发送  

目录：/interface_test/core/send_mail.py

### 2.5读取excel

目录：/InterfaceTest/interface_test/core/read_xls.py

### 2.6 读取数据库

```python
/InterfaceTest/interface_test/db
from db import mysql

if __name__ == '__main__':
    result = mysql.query_db("select * from amway_poc")
    print(result)
    
```

### 2.7 网络请求

/InterfaceTest/interface_test/http_request

``` python
from http_request import post
from test_config import config
from core import logger

login_url = "{}://{}:{}/{}".format(config.PROTOCOL, config.HOST, config.PORT, config.LOGIN_PATH)
request_data = {
    "username": config.LOGIN_USER,
    "password": config.LOGIN_PWD,
}
def login():
    logger.logging.info(login_url)
    response = post.http_post(login_url, config.HEADER, request_data)
    token = response['token']
    return token
```
