import eel
import random
from datetime import datetime
from os import getcwd

dir = getcwd()
eel.init('application/web')

@eel.expose
def get_random_name():
    eel.prompt_alerts('Random name')

@eel.expose
def get_random_number():
    eel.prompt_alerts(random.randint(1, 100))

@eel.expose
def get_date():
    eel.prompt_alerts(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    print("ADASD")
@eel.expose
def get_ip():
    eel.prompt_alerts('127.0.0.1')

eel.start('index.html')