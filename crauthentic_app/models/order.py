from crauthentic_app.config.mysqlconnection import connectToMySQL
from flask import flash
 
class Order:
    def __init__(self, data):
        self.id=data['id']
        self.pickup_details=data['pickup_details']
        self.dropoff_details=data['dropoff_details']
        self.passengers=data['passengers']
        self.suitcases=data['suitcases']
        self.date=data['date']
        self.hour=data['hour']
        self.prices_idprices=data['prices_idprices']
        self.prices_routes_id=data['prices_routes_id']
        self.customers_id=data['customers_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def getAll (cls):
        query="SELECT * FROM orders;"
        results=connectToMySQL('crauthentic').query_db(query)
        orders=[]
        for order in results:
            orders.append(cls(order))
        return orders
        
    @classmethod
    def getId (cls,id):
        query="SELECT * FROM orders WHERE id = %(id)s"
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
    def save(cls, data):
        query = "INSERT INTO orders (id, pickup_details,dropoff_details,passengers,suitcases,date,hour,prices_idprices,prices_routes_id,customers_id, created_at, updated_at) VALUES (%(id)s,%(pickup_details)s, %(dropoff_details)s, %(passengers)s, %(suitcases)s,%(date)s,%(hour)s,%(prices_idprices)s,%(prices_routes_id)s,%(customers_id)s, NOW(),NOW());"
        mysql = connectToMySQL('crauthentic')
        result = mysql.query_db(query, data)
        print(result)
        data_usuario={'id':data['id']}
        print(data_usuario)
        return cls.getId(data_usuario['id'])
    @staticmethod
    def validations(route):
        is_valid=True
        if route.get('to') == "" or route.get('to') == None:
            flash('Destination location is required')
            is_valid=False
        if route.get('from') == "" or route.get('from')== None:
            flash('Departure location is required')
            is_valid=False
        if route['passengers'] == "":
            flash('Specify number of passengers')
            is_valid=False
        if route['suitcases'] == "":
            flash('Specify number of suitcases')
            is_valid=False
        if route['date'] == "":
            flash('Specify date of shuttle')
            is_valid=False
        if route['hour'] == "":
            flash('Specify hour of shuttle')
            is_valid=False
        return is_valid
