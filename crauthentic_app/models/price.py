from crauthentic_app.config.mysqlconnection import connectToMySQL
from crauthentic_app.models.location import Location
from flask import flash

class Price:
    def __init__(self, data):
        self.id=data['id']
        self.price=data['price']
        self.route_id=data['route_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def getAll (cls):
        query="SELECT * FROM prices;"
        results=connectToMySQL('crauthentic').query_db(query)
        prices=[]
        for price in results:
            prices.append(cls(price))
        return prices
        
    @classmethod
    def getId (cls,id):
        query="SELECT * FROM prices WHERE id = %(id)s"
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
    def getRoutesAndPrices(cls):
        query='SELECT r.id, r.duration, r.from_location_id,r.to_location_id, l1.id as from_location_id, l1.location as from_location,l2.id as to_location_id, l2.location as to_location, p.id as price_id, p.price as price from routes r LEFT JOIN locations l1 ON l1.id=r.from_location_id LEFT JOIN locations l2 ON l2.id=r.to_location_id LEFT JOIN prices p ON p.route_id=r.id;'
        results=connectToMySQL('crauthentic').query_db(query)
        routes=[]
        for route in results:
            routes.append(cls(route))
        return routes
    
    @classmethod
    def getRouteAndPriceById(cls,data):
        query='SELECT r.id, r.duration, r.from_location_id,r.to_location_id, l1.id as from_location_id, l1.location as from_location,l2.id as to_location_id, l2.location as to_location, p.id as price_id, p.price as price from routes r LEFT JOIN locations l1 ON l1.id=r.from_location_id LEFT JOIN locations l2 ON l2.id=r.to_location_id LEFT JOIN prices p ON p.route_id=r.id WHERE r.id = %(id)s;'
        result=connectToMySQL('crauthentic').query_db(query,data)
        print("Result", result)
        if len(result)>0:
            return cls(result[0])
        else:
            return None
    @classmethod
    def getLastPriceForRouteById(cls,id):
        query=f"SELECT r.id, r.duration, r.from_location_id,r.to_location_id, l1.id as from_location_id, l1.location as from_location,l2.id as to_location_id, l2.location as to_location, p.id as price_id, p.price as price from routes r LEFT JOIN locations l1 ON l1.id=r.from_location_id LEFT JOIN locations l2 ON l2.id=r.to_location_id LEFT JOIN prices p ON p.route_id=r.id WHERE r.id = {id} ORDER BY p.updated_at DESC LIMIT 1;"
        result=connectToMySQL('crauthentic').query_db(query)
        print("Result", result)
        if len(result)>0:
            return result[0]
        else:
            return None