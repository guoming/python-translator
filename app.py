import requests
import random
import string
import hashlib
import config
from configparser import ConfigParser
import argparse
import os

def generate_random_string(length):
    # 使用 string.ascii_letters 包含所有字母（大小写）
    # 你还可以使用 string.digits 包含数字
    characters = string.ascii_letters + string.digits

    # 生成随机字符串
    random_string = ''.join(random.choice(characters) for _ in range(length))

    return random_string

def baidu_translate(text, from_lang='auto', to_lang='auto'):
    base_url = 'https://fanyi-api.baidu.com/api/trans/vip/translate'

    appid = config.BAIDU_APP_ID
    secret_key = config.BAIDU_APP_SECRET_KEY

    # 构建签名
    salt = generate_random_string(10)
    sign_str = appid + text + salt + secret_key
    sign = hashlib.md5(sign_str.encode()).hexdigest()

    # 构建请求参数
    params = {
        'q': text,
        'from': from_lang,
        'to': to_lang,
        'appid': appid,
        'salt': salt,
        'sign': sign
    }

    # 发送请求
    response = requests.get(base_url, params=params)
    result = response.json()

    # 解析翻译结果
    if 'trans_result' in result:
        translation = result['trans_result'][0]['dst']
        return translation
    else:
        return None


def main():

    # 解析命令行参数
    parser = argparse.ArgumentParser(description='Replace variables in JSON file using values from a config file.')
    parser.add_argument('--to', required=True, help='翻译后的语言')
    parser.add_argument('--text', required=True, help='待翻译的文本')

    args = parser.parse_args()

    translation = baidu_translate(args.text, from_lang='auto', to_lang=args.to)

    print(f'{translation}')


if __name__ == '__main__':
    main()
