from crauthentic_app.config.mysqlconnection import connectToMySQL
from crauthentic_app.models.location import Location
from flask import flash
import datetime

class Route:
    def __init__(self, data):
        self.id=data['id']
        self.duration=data['duration']
        self.from_location_id=data['from_location_id']
        self.to_location_id=data['to_location_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.prices=[]

    @classmethod
    def getAll (cls):
        query="SELECT * FROM routes;"
        results=connectToMySQL('crauthentic').query_db(query)
        routes=[]
        for route in results:
            routes.append(cls(route))
        return routes
        
    @classmethod
    def getId (cls,id):
        query="SELECT * FROM routes WHERE id = %(id)s"
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
    def getByLocationsId (cls,data):
        query="SELECT * FROM routes WHERE from_location_id = %(from_location_id)s AND to_location_id = %(to_location_id)s"
        result=connectToMySQL('crauthentic').query_db(query,data)
        print("Result", result)
        if len(result)>0:
            return cls(result[0])
        else:
            return None
    @classmethod
    def getFullRoutes(cls):
        query='SELECT r.id, r.duration, r.from_location_id,r.to_location_id, l1.id as from_location_id, l1.location as from_location,l2.id as to_location_id, l2.location as to_location from routes r LEFT JOIN locations l1 ON l1.id=r.from_location_id LEFT JOIN locations l2 ON l2.id=r.to_location_id;'
        results=connectToMySQL('crauthentic').query_db(query)
        routes=[]
        for route in results:
            routes.append(cls(route))
        return routes
    
    @classmethod
    def getFullRoutesById(cls,id):
        query=f'SELECT r.id, r.duration, r.from_location_id,r.to_location_id, l1.id as from_location_id, l1.location as from_location,l2.id as to_location_id, l2.location as to_location from routes r LEFT JOIN locations l1 ON l1.id=r.from_location_id LEFT JOIN locations l2 ON l2.id=r.to_location_id WHERE r.id = {id};'
        result=connectToMySQL('crauthentic').query_db(query)
        print("Result", result)
        if len(result)>0:
            return cls(result[0])
        else:
            return None
    @staticmethod
    def validations(route):
        is_valid=True
        if route.get('to') == None:
            flash('Destination location is required')
            is_valid=False
        if route.get('from') == None:
            flash('Departure location is required')
            is_valid=False
        if route['passengers'] == "" or int(route['passengers']) < 1:
            flash('Specify number of passengers')
            is_valid=False
        date=datetime.date.fromisoformat(route['date'])
        if route['date'] == "" or date<datetime.date.today():
            flash('Specify a valid date')
            is_valid=False
        return is_valid