校园论坛后端 School Forum Android Application
--
## 运行方法 How to run?
1. 进入venv环境 Enter virtual environment：
```
venv/Scripts/activate
```
2. 依次运行以下指令设置flask环境变量或直接运行run.bat Execute the following to setup Flask environment or execute run.bat：
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
3. 启动服务器 Start server：
```
flask run
```
4. 测试服务器是否启动成功 Test if server running：
```
访问localhost:8000，若显示Index则服务器启动成功
```

## 数据库 Database
1. 本地创建数据库（也可以在config.cfg中更改数据库用户名等）Create database locally (or change database usernames etc. in config.cfg)：
```
DBSM：MySQL
端口：3306
创建用户：forum，密码：123456
数据库名称：forum_app
```

2. 使用MySQLWorkBench或任意MySQL工具运行forum_app.sql导入数据库结构即可 Use MySQL WorkBench or any other MySQL tools to execute forum_app.sql script, in order to import the database structure

## 前后端接口文档 API Docs
[接口文档/API Docs](https://www.showdoc.com.cn/1931979514400970) 
