import sqlite3
import os
from flask import Flask
from flask import jsonify, abort, redirect
from flask_restful import Resource, Api
#import json, jwt
from flask import Blueprint, request, jsonify, current_app, Response
from flask_restful import Api, Resource # used for REST API building
#from datetime import datetime
#from auth_middleware import token_required

#from model.users import User




hello_api = Blueprint('hello_api', __name__,url_prefix='/api/hello')
app = Flask(__name__)
api = Api(app)
api = Api(hello_api)
        
class HelloWorld(Resource):
    def get(self):
        return {"hello" : "world"}

class LogIn(Resource):   
    def get(self):
        body = request.authorization
        password = body.get('password')
        username = body.get('username')
        print(username)
        print(password)
        con = sqlite3.connect("/home/nandanv/vscode/indicpt/data/users.db")
        cur = con.cursor()
        res = cur.execute("SELECT username FROM users where username = '"+username+"' AND password = '"+password+"'")
        #print(len(res.fetchall()))
        user_count=len(res.fetchall())
        print(user_count)
        if user_count == 0:
            abort(403, description=username + " user does not exist") 
        else:
            return redirect("/")
            #return jsonify({"message": "Login successful", "username": username})
        #return {"hello" : "nandan"}
        
class CreateUser(Resource):
    def get(self):
        body = request.authorization
        password = body.get('password')
        username = body.get('username')
        print(username)
        print(password)
        con = sqlite3.connect("/home/nandanv/vscode/indicpt/data/users.db")
        cur = con.cursor()
        res = cur.execute("SELECT username FROM users where username = '"+username+"' AND password = '"+password+"'")
        #print(len(res.fetchall()))
        user_count=len(res.fetchall())
        print(user_count)
        if user_count == 0:
            sql="INSERT INTO users VALUES (?,?)"
            cur.execute(sql,(username,password))
            con.commit()
            return username + " " + "user created." 
        else:
            return "user already exists"
        #return {"hello" : "nandan"}
        
class UpdateUser(Resource):
    def get(self):
        body = request.authorization
        password = body.get('password')
        username = body.get('username')
        print(username)
        print(password)
        con = sqlite3.connect("/home/nandanv/vscode/indicpt/data/users.db")
        cur = con.cursor()
        res = cur.execute("SELECT username FROM users where username = '"+username+"'")
        #print(len(res.fetchall()))
        user_count=len(res.fetchall())
        print(user_count)
        if user_count == 1:
            sql="UPDATE users SET password = ? WHERE username = ?"
            cur.execute(sql,(password,username))
            con.commit()
            return username + " " + "password updated." 
        else:
            return "user does not exist"
        #return {"hello" : "nandan"}

class DeleteUser(Resource):
    def get(self):
        body = request.authorization
        password = body.get('password')
        username = body.get('username')
        print(username)
        print(password)
        con = sqlite3.connect("/home/nandanv/vscode/indicpt/data/users.db")
        cur = con.cursor()
        res = cur.execute("SELECT username FROM users where username = '"+username+"'")
        #print(len(res.fetchall()))
        user_count=len(res.fetchall())
        print(user_count)
        if user_count == 1:
            sql="DELETE FROM users WHERE username = ?"
            cur.execute(sql,(username,))
            con.commit()
            return username + " " + "deleted" 
        else:
            return "user does not exist"
        #return {"hello" : "nandan"}

class ReadUsers(Resource):
    def get(self):
        body = request.authorization
        password = body.get('password')
        username = body.get('username')
        print(username)
        print(password)
        con = sqlite3.connect("/home/nandanv/vscode/indicpt/data/users.db")
        cur = con.cursor()
        res = cur.execute("SELECT username,password FROM users")
        #print(len(res.fetchall()))
        data = res.fetchall()
        user_count=len(data)
        print(user_count)
        if user_count == 0:
            return username + " " + "user does not exist" 
        else:
            return data
        #return {"hello" : "nandan"}
    
api.add_resource(HelloWorld, '/')
api.add_resource(LogIn, '/login')
api.add_resource(CreateUser, '/createuser')
api.add_resource(UpdateUser, '/updateuser')
api.add_resource(DeleteUser, '/deleteuser')
api.add_resource(ReadUsers, '/readusers')





#con = sqlite3.connect("/home/nandanv/vscode/indicpt/data/users.db")

#cur = con.cursor()

#cur.execute("CREATE TABLE users(username,password)")
#cur.execute("""INSERT INTO users VALUES ('naveenv','naveenv')""")

#con.commit()
#res = cur.execute("SELECT username,password FROM users")

#f = res.fetchall()

#print(f)

#Secret_key = os.getenv('SECRET_KEY')

#print(Secret_key)