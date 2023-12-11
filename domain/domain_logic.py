from domain.order import Order, OrderCancel
from typing import List
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import config 
from domain.order import Order, OrderCancel
from domain.messages import Ordersent, OrderCancelled
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt


def get_inventory_catalog():
    url = config.url1
    response = requests.get(url)
    if response.status_code == 200:
        catalog = response.json()
        return catalog
    else:
        return None
def get_order_status(order_id):
    url = config.url2
    response = requests.get(url)
    if response.status_code == 200:
        status = response.json()
        return status
    else:
        return None 
    
def PostOrder(order: Order):
    topic = config.mqtt_topic_on_order_send    
    __message_publish(topic, order.to_json())
    return

def delete_order(order_id):
    topic =config.mqtt_topic_on_order_canceled
    payload= json.dumps(order_id)
    #here ser order id before passing it
    __message_publish(topic, payload)

    response = {
        "status_code": 204
    }
    return response


def __message_publish(topic: str, payload: str):

    print("Out going message")
    print(F"Topic: {topic}")
    print(F"Payload: {payload}")

    publish.single(
        topic, 
        payload=payload, 
        qos=1, #least once
        retain=False, 
        hostname=config.mqtt_host,
        port=config.mqtt_port, 
        client_id=config.mqtt_client_id, 
        auth= {'username' : config.mqtt_username, 'password' : config.mqtt_password}, 
        tls=None,
        protocol=mqtt.MQTTv5, transport=config.mqtt_transport) 

