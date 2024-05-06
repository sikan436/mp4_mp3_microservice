import jwt,datetime,os
from flask import Flask,request
from flask_mysqldb import MySQL

server=Flask(__name__)
mysql=MySQL(server)
server.config["MYSQL_HOST"]=os.environ.get("MYSQL_HOST")
server.config["MYSQL_USER"]=os.environ.get("MYSQL_USER")
server.config["MYSQL_PASSWORD"]=os.environ.get("MYSQL_PASSWORD")
server.config["MYSQL_PORT"]=os.environ.get("MYSQL_PORT")
server.config["MYSQL_DB"]=os.environ.get("MYSQL_DB")
#3306 , 33060
@server.route("/login",method=["POST"])
def login():
    auth=request.authorization
    if not auth:
        return "missing credentials",401

    cur=mysql.connection.cursor()
    res=cur.execute("select email,password from user where email=%s",(auth.username,))

    if res>0:
        user_row=cur.fetchone()
        email=user_row[0]
        password=user_row[1]

        if auth.username !=email or auth.password != password:
            return "invalid credentials", 401
        else:
            return CreateJWT(auth.username,os.environ.get("JWT_SECRET"),True)
    else:
        return "invalid credentials",401
    