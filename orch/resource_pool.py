# -*- coding: utf-8 -*-
"""
Spyder Editor

Resource pool accepts new resource at startup time
It accepts new resource at runtime
It also accepts resource for update
"""
from engine_manager import EngineManager
from random import randint, choice
import string
class ResourcePool():
    
    def __init__(self, callback):
        self.callback = callback
        
    def accept_resource(self, resource):
        '''
        accept a new resource
        @param resource: propertifes of fog node as dict 
        '''
        self.callback([resource])
    
    def accept_bulk_resources(self, resources):
        '''
        accept a list of resources
        @param resources: list of properties of fog nodes.
        '''
        self.callback(resources)
        
def generate_address():
    '''
    generate space seperated three words address
    '''
    first_part = ''.join(choice(string.ascii_letters) for _ in range(6))
    second_part = ''.join(choice(string.ascii_letters) for _ in range(6) )

    return first_part + ' ' + second_part + ' ' +  str(randint(1, 50))

def generate_resources():
    '''
    generate properties of fog node randomly in a bulk amount 
    '''
    resources = []
    for number in range (1 , 20):
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

def generate_single_resource():
    '''
    create static single resource properties
    '''
    resource = {
        'ip': '113.2.101.79',
        'building': 'Hans leipelt str. 7',
        'postal_code': 80807,
        'city': 'Munich',
        'cpu': 1000,
        'mem': 3000
        }
    return resource
    
engine = EngineManager()
resourcepool = ResourcePool(engine.place_resource)

# add single resource
resourcepool.accept_resource(generate_single_resource())
        
# add bulk resources
resourcepool.accept_bulk_resources(generate_resources())