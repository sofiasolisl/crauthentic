from crauthentic_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Location:
    def __init__(self, data):
        self.id=data['id']
        self.location=data['location']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

 
    @classmethod
    def getAll (cls):
        query="SELECT * FROM locations;"
        results=connectToMySQL('crauthentic').query_db(query)
        locations=[]
        for location in results:
            locations.append(cls(location))
        return locations
        
    @classmethod
    def getId (cls,id):
        query="SELECT * FROM locations WHERE id = %(id)s"
        data={
            'id':id
        }
        result=connectToMySQL('crauthentic').query_db(query,data)
        print("Result", result)
        if len(result)>0:
            return cls(result[0])
        else:
            return None