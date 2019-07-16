import urllib
import json

from test_config import config

def http_post(url, header, data):
    request = urllib.request.Request(url=url, headers=config.HEADER, data=bytes(json.dumps(data), 'utf-8'))
    try:
        response = urllib.request.urlopen(request)
        status = response.status
        if config.HTTP_STATUS_OK == status:
            data = response.read().decode('utf8')
            res_dict = json.loads(data)
            if res_dict["code"] == config.HTTP_SUCCESS_CODE:
                return res_dict["data"]
            else:
                raise Exception(res_dict["error"])
            return data
        else:
            raise Exception("http call error, status:" + status)
    except Exception as ex:
        raise ex
        



    