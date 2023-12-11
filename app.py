from flask import Flask,request, Response
from flask_mqtt import Mqtt
import domain.domain_logic as dl
import config
from domain.order import Order
import requests
import uuid



app = Flask(__name__)
app.config['MQTT_BROKER_URL'] = config.mqtt_host  # use the free broker from HIVEMQ
app.config['MQTT_BROKER_PORT'] = config.mqtt_port  # default port for non-tls connection
app.config['MQTT_USERNAME'] = config.mqtt_username  # set the username here if you need authentication for the broker
app.config['MQTT_PASSWORD'] = config.mqtt_password  # set the password here if the broker demands authentication
app.config['MQTT_KEEPALIVE'] = 60  # set the time interval for sending a ping to the broker to 5 seconds
app.config['MQTT_TLS_ENABLED'] = False  # set TLS to disabled for testing purposes

mqtt = Mqtt(app)



@app.route("/inventory")
def Get():
    return dl.get_inventory_catalog()

@app.route("/order")
def Get(id):
    return dl.get_order_status(id)

@app.route('/order', methods=['POST'])
def Post():
    data = request.json #access json which contain order information
    order = Order.from_json(data) # deserialize order      
    order.order_id = str(uuid.uuid4()) # generate uuid and set it to given order
    dl.PostOrder(order) # call domain logic
    resp = Response("{}", status=201, mimetype='application/json')
    resp.headers['location'] = '/order/' + order.order_id
    return resp

@app.route("/order")
def Delete(id):
    return dl.delete_order(id)




