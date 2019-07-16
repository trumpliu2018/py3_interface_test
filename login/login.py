import urllib
from urllib import request
import json
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
