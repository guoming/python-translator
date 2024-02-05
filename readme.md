# 翻译器

## 1.简介
基于百度翻译接口Python翻译

## 2. 如何安装

创建虚拟环境
``` sh
pip install virtualenv
virtualenv .env
source .venv/bin/activate
```

安装依赖
``` sh
pip install -r requirements.txt
```

## 3. 如何使用

文本翻译成中文
```sh
python app.py --to=zh --text="hello"
```

文本翻译成英文
``` sh
python app.py --to=en --text="你好"
```
