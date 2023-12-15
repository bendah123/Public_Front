# Public-Front service 

Distributed Systems, Fall 2023
#Stucture 
domain contains domain logic
app.py is service start entry point. It contains topic subscriptions
_config_sample is configuration file example. Should be copied and named as config.py
requirements contain all the requirements we need 
# Visual Studio Code 

Setup Flask to Visual Studio Code

https://code.visualstudio.com/docs/python/tutorial-flask

Install from requirements file

pip install -r requirements.txt
# Run service

python -m flask run --host=0.0.0.0 --port=8081


