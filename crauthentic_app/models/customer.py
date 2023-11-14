from crauthentic_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
BLANK_REGEX=re.compile(r'[\s]+$')
  

class Customer:
    def __init__(self, data):
        self.id=data['id']
        self.fname=data['fname']
        self.lname=data['lname']
        self.email=data['email']
        self.cellphone=data['cellphone']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def getAll (cls):
        query="SELECT * FROM customers;"
        results=connectToMySQL('crauthentic').query_db(query)
        customers=[]
        for customer in results:
            customers.append(cls(customer))
        return customers
        
    @classmethod
    def getId (cls,id):
        query="SELECT * FROM customers WHERE id = %(id)s"
        data={
            'id':id
        }
        result=connectToMySQL('crauthentic').query_db(query,data)
        print("Result", result)
        if len(result)>0:
            return cls(result[0])
        else:
            return None
    @classmethod
    def updateByID(cls,data):
        query = 'UPDATE customers SET fname=%(fname)s, lname=%(lname)s, cellphone=%(cellphone)s, updated_at=NOW() WHERE id = %(id)s;'
        mysql = connectToMySQL('crauthentic')
        result = mysql.query_db(query, data)
        return result
    @classmethod
    def save(cls, data):
        query = "INSERT INTO customers (id, fname, lname, email,cellphone, created_at, updated_at) VALUES (%(id)s,%(fname)s, %(lname)s, %(email)s, %(cellphone)s, NOW(),NOW());"
        mysql = connectToMySQL('crauthentic')
        result = mysql.query_db(query, data)
        print(result)
        data_usuario={'id':data['id']}
        print(data_usuario)
        return cls.getId(data_usuario['id'])
    @classmethod
    def getEmail (cls,email):
        query="SELECT * FROM customers WHERE email = %(email)s"
        data={
            'email':email
        }
        result=connectToMySQL('crauthentic').query_db(query,data)
        if len(result)>0:
            return cls(result[0])
        else:
            return None
    @staticmethod
    def validations(route):
        is_valid=True
        if route['fname'] == "" or   BLANK_REGEX.match(route['fname']) :
            flash('First Name is required')
            is_valid=False
        if route['lname'] == "" or  BLANK_REGEX.match(route['lname']):
            flash('Last Name is required')
            is_valid=False
        if route['cellphone'] == "":
            flash('Specify a cellphone')
            is_valid=False
        if len(route['fname']) < 2 or len(route['lname']) < 2:
            flash ("First name and last name must be at least of 2 characters.")
            is_valid=False
        if not EMAIL_REGEX.match(route['email']) or route['email'] == "": 
            flash("Invalid email address")
            is_valid = False
        return is_valid