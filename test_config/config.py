import os

LOGIN_USER = "super"
LOGIN_PWD = "Connext@0101"
LOGIN_PATH = "backend/user/login"
HOST = "10.128.0.150"
PORT = "8002"
PROTOCOL = "http"
# HEADER = {'Content-Type': 'application/json'}
HEADER = { 'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36', 'Content-Type': 'application/json'} 
HTTP_STATUS_OK = 200
HTTP_SUCCESS_CODE = 0


BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTCASE_PATH =  os.path.join(BASE_PATH,'test_case')
REPORT_PATH =  os.path.join(BASE_PATH,'report/')
LOG_PATH = os.path.join(BASE_PATH,'log/log.txt')

DB_USER = 'connextpaas'
DB_PASSWORD = 'connext@0101'
DB_HOST = '10.128.0.180'
DB_PORT = 3306
DB_CLOUD = "cloudproject"
DB_VM = "vmwareproject"

MailUser = 'kakaliush@163.com'
MailPwd = '31415926kakaliu'
