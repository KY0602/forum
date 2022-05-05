## 运行方法
1. 进入venv环境：
```
venv/Scripts/activate
```
2. 依次运行以下指令设置flask环境变量：
```
Powershell: 
$env:FLASK_APP="__init__.py"
$env:FLASK_RUN_HOST="0.0.0.0"
$env:FLASK_RUN_PORT=8000

CMD:
set FLASK_APP=__init__.py
set FLASK_RUN_HOST=0.0.0.0
set FLASK_RUN_PORT=8000
```
3. 启动服务器：
```
flask run
```
4. 测试服务器是否启动成功：
```
访问localhost:8000，若显示Index则服务器启动成功
```

## 登录
```
email: admin@gmail.com
password: Abc123456
```