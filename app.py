from flask import Flask
from flask_mqtt import Mqtt
import domain.domain_logic as dl
import config
from domain.order import Order, OrderCancel
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

@app.route("/order")
def Post(payload):
    order_id=str(uuid.uuid4())
    #check in doc id it will be aut ser or not 
    return dl.PostOrder(order_id,payload)

@app.route("/order")
def Delete(id):
    return dl.delete_order(id)




