from crauthentic_app import app
from crauthentic_app.models.location import Location
from crauthentic_app.models.route import Route
from crauthentic_app.models.price import Price
from crauthentic_app.models.customer import Customer
from crauthentic_app.models.order import Order
from flask import render_template, redirect, request, session, jsonify
import requests
from requests.auth import HTTPBasicAuth
from . import send_email




@app.route("/", methods = ['GET'])
def index():
        locations=Location.getAll()
        return render_template("index.html",locations=locations)

@app.route('/shuttle', methods=['GET', 'POST'])
def shuttle():
    
    if request.method == "POST":
        session.clear()
        form=dict(request.form)
        if Route.validations(request.form):
            data={
                "from_location_id":form.get('from'),
                "to_location_id":form.get('to'),
            }
            
            route=Route.getByLocationsId(data)
            print('ID:', route.id)
            shuttle=Price.getLastPriceForRouteById(route.id)
            shuttle['passengers']=form.get('passengers')
            print(form.get('passengers'))
            shuttle['date']=form.get('date')
            print(shuttle)
            session['shuttle']=shuttle
            return redirect("/shuttle")
        else:
            return redirect ('/')
    else:
        locations=Location.getAll()
        shuttle=session['shuttle']
        print("Session Shuttle", shuttle)
        return render_template('shuttle.html',locations=locations, shuttle=shuttle)

@app.route("/checkout", methods = ['GET','POST'])
def checkout():
    if request.method == "POST":
        session.clear()
        form=dict(request.form)
        if Customer.validations(request.form) and Order.validations(request.form):
            print('todo bien con validaciones')
            session['shuttle']=request.form
            data={
                "from_location_id":form.get('from'),
                "to_location_id":form.get('to'),
            }
            route=Route.getByLocationsId(data).id
            session['prices_routes_id']=route
            
            price=Price.getLastPriceForRouteById(route)
            session['prices_idprices']=price['id']
            if Customer.getEmail(form['email']) == None:
                if Customer.getAll() == None:
                    form ['id']=1
                else:
                    form ['id']=len(Customer.getAll()) + 1
                Customer.save(form)
            else:
                customer=Customer.getEmail(form['email']) 
                form['id']=customer.id
                Customer.updateByID(form)
            session['customers_id']=form ['id']
            return redirect ('/checkout')
        else:
            locations=Location.getAll()
            data={
                "from_location_id":form.get('from'),
                "to_location_id":form.get('to'),
            }
            route=Route.getByLocationsId(data)
            shuttle=Price.getLastPriceForRouteById(route.id)
            shuttle['passengers']=form.get('passengers')
            shuttle['date']=form.get('date')
            session['shuttle']=shuttle
            return redirect("/shuttle")
    else:
        shuttle=session['shuttle']
        data={
                "from_location_id":shuttle.get('from'),
                "to_location_id":shuttle.get('to'),
            }
        
        route=Route.getByLocationsId(data)
        price=Price.getLastPriceForRouteById(route.id)
        print('price', price)
        return render_template('checkout.html', shuttle=shuttle, price=price )

@app.route("/payments/<order_id>/capture", methods=["POST"])
def capture_payment(order_id):  
    captured_payment = approve_payment(order_id)
    print(captured_payment) 
    return jsonify(captured_payment)
def approve_payment(order_id):
    api_link = f"https://api-m.sandbox.paypal.com/v2/checkout/orders/{order_id}/capture"
    client_id = "AdwxXELK5YJL6JSVoaHHof_oUmj-CdASKNWsjsRXX0AsXEeAan1HMQdZNsTYLUv3rc0DcArzKzgRrDSd"
    secret = "EDOV9Sh5N-squWUOR_NYeDCKXyO8bYKb4p8BUI8--jnfDdxhLqDdUJ7nfpg7Q-KiW0yp3U6HGx-qNDqK"
    basic_auth = HTTPBasicAuth(client_id, secret)
    headers = {
        "Content-Type": "application/json",
    }
    response = requests.post(url=api_link, headers=headers, auth=basic_auth)
    response.raise_for_status()
    json_data = response.json()
    return json_data

@app.route('/confirmation')
def confirmation():
    print(session)
    data={}
    if Order.getAll() == None:
        data ['id']=1
    else:
        data ['id']=len(Order.getAll()) + 1
    data['pickup_details']=session['shuttle']['pickup_details']
    data['dropoff_details']=session['shuttle']['dropoff_details']
    data['passengers']=session['shuttle']['passengers']
    data['suitcases']=session['shuttle']['suitcases']
    data['hour']=session['shuttle']['hour']
    data['date']=session['shuttle']['date']
    data['prices_routes_id']=session['prices_routes_id']
    data['customers_id']=session['customers_id']
    data['prices_idprices']=session['prices_idprices']
    data['from']=Location.getId(session['shuttle']['from']).location
    data['to']=Location.getId(session['shuttle']['to']).location
    data['fname']=session['shuttle']['fname']
    Order.save(data)
    recievers=[f"{Customer.getId(data['customers_id']).email}",'sofis64@developer.com']
    send_email.send_email(recievers, data)
    return render_template('confirmation.html', customer=session['shuttle']['fname'])