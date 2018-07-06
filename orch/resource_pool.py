# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from engine_manager import EngineManager
from random import randint, choice
import string
class ResourcePool():
    
    def __init__(self, callback):
        self.callback = callback
        
    def accept_resource(self, resource):
        self.callback([resource])
    
    def accept_bulk_resources(self, resources):
        self.callback(resources)
        
def generate_address():
    first_part = ''.join(choice(string.ascii_letters) for _ in range(6))
    second_part = ''.join(choice(string.ascii_letters) for _ in range(6) )

    return first_part + ' ' + second_part + ' ' +  str(randint(1, 50))
def generate_resources():
    
    resources = []
    for number in range (1 , 10):
        resource = {
        'ip': str(randint(1, 255)) + '.'+ str(randint(1, 255)) + '.' + str(randint(1, 255))+'.' + str(randint(1, 255)),
        'building': generate_address() ,
        'postal_code': randint(80331, 85764),
        'city': 'Munich',
        'cpu': randint(2000, 5000),
        'mem': randint(3000, 10000)
        }
        resources.append(resource)
    return resources
engine = EngineManager()
resourcepool = ResourcePool(engine.place_resource)
# add single resource
resource = {
        'ip': '10.10.10.14',
        'building': 'Hans leipelt str. 7',
        'postal_code': 80806,
        'city': 'Munich',
        'cpu': 1000,
        'mem': 3000
        }
resourcepool.accept_resource(resource)
        
# add bulk resources
resourcepool.accept_bulk_resources(generate_resources())