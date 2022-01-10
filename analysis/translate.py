import requests
import random
import json
from hashlib import md5

def translate_baidu_api(query):
    """
    1. 拼接请求参数: appid + query + salt + 密钥 = 字符串1
    2. 对字符串1做md5
    (1. 带翻文本query需为UTF-8编码)
    
    """    
    # Set your own appid/appkey.
    appid = '20210413000775736'    # 填写你的appid
    appkey = '0WQhk5ub_ORT0VI_GlQe'    # 填写你的密钥

    # For list of language codes, please refer to `https://api.fanyi.baidu.com/doc/21`
    from_lang = 'en'
    to_lang =  'zh'

    endpoint = 'http://api.fanyi.baidu.com'
    path = '/api/trans/vip/translate'
    url = endpoint + path

#     query = 'Hello World! This is 1st paragraph.\nThis is 2nd paragraph.'

    # Generate salt and sign
    def make_md5(s, encoding='utf-8'):
        return md5(s.encode(encoding)).hexdigest()

    salt = random.randint(32768, 65536)
    sign = make_md5(appid + query + str(salt) + appkey)

    # Build request
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'appid': appid, 'q': query, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}

    # Send request
    r = requests.post(url, params=payload, headers=headers)
    result = r.json()
    # Show response
#     print(json.dumps(result, indent=4, ensure_ascii=False))['trans_result'][0]['dst']
    return result['trans_result'][0]['dst']
#     return json.dumps(result, indent=4, ensure_ascii=False)
#     return chineses_text
