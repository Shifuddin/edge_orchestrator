#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 15:17:31 2018

@author: shifu
"""
from random import randint, choice, uniform


city_blocks = [
        {'postal_address': 'Alte Heide 1, 80805, Munich',
         'resources':[
                 {'ip':'10.10.10.10','mem': randint(3000, 6000),'cpu': randint(3300, 4000)},
                 {'ip':'10.10.10.11','mem': randint(3000, 6000),'cpu': randint(3300, 4000)},
                 {'ip':'10.10.10.12','mem': randint(3000, 6000),'cpu': randint(3300, 4000)},
                 {'ip':'10.10.10.13','mem': randint(3000, 6000),'cpu': randint(3300, 4000)}],
         'band': randint(3300, 4000),
         'latency': uniform(0,0.5)},
        
         {'postal_address': 'Alte Heide 2, 80805, Munich',
         'resources':[
                 {'ip':'10.10.11.10','mem': randint(3000, 6000),'cpu': randint(3300, 4000)},
                 {'ip':'10.10.11.11','mem': randint(3000, 6000),'cpu': randint(3300, 4000)},
                 {'ip':'10.10.11.12','mem': randint(3000, 6000),'cpu': randint(3300, 4000)},
                 {'ip':'10.10.11.13','mem': randint(3000, 6000),'cpu': randint(3300, 4000)}],
         'band': randint(3300, 4000),
         'latency': uniform(0,0.5)},
          
          
         {'postal_address': 'Hans-Leipelt-Str 1, 80805, Munich',
         'resources':[
                 {'ip':'10.10.24.10','mem': randint(3000, 6000),'cpu': randint(3300, 4000)},
                 {'ip':'10.10.24.11','mem': randint(3000, 6000),'cpu': randint(3300, 4000)},
                 {'ip':'10.10.24.12','mem': randint(3000, 6000),'cpu': randint(3300, 4000)},
                 {'ip':'10.10.24.13','mem': randint(3000, 6000),'cpu': randint(3300, 4000)}],
         'band': randint(3300, 4000),
         'latency': uniform(0,0.5)},
          
          
         {'postal_address': 'Hans-Leipelt-Str 2, 80805, Munich',
         'resources':[
                 {'ip':'10.10.25.10','mem': randint(3000, 6000),'cpu': randint(3300, 4000)},
                 {'ip':'10.10.25.11','mem': randint(3000, 6000),'cpu': randint(3300, 4000)},
                 {'ip':'10.10.25.12','mem': randint(3000, 6000),'cpu': randint(3300, 4000)},
                 {'ip':'10.10.25.13','mem': randint(3000, 6000),'cpu': randint(3300, 4000)}],
         'band': randint(3300, 4000),
         'latency': uniform(0,0.5)},
          
         {'postal_address': 'Beltweg 1, 80806, Munich',
         'resources':[
                 {'ip':'10.11.10.10','mem': randint(3000, 6000),'cpu': randint(3300, 4000)},
                 {'ip':'10.11.10.11','mem': randint(3000, 6000),'cpu': randint(3300, 4000)},
                 {'ip':'10.11.10.12','mem': randint(3000, 6000),'cpu': randint(3300, 4000)},
                 {'ip':'10.11.10.13','mem': randint(3000, 6000),'cpu': randint(3300, 4000)}],
         'band': randint(3300, 4000),
         'latency': uniform(0,0.5)},
          
         {'postal_address': 'Beltweg 2, 80806, Munich',
         'resources':[
                 {'ip':'10.11.11.10','mem': randint(3000, 6000),'cpu': randint(3300, 4000)},
                 {'ip':'10.11.11.11','mem': randint(3000, 6000),'cpu': randint(3300, 4000)},
                 {'ip':'10.11.11.12','mem': randint(3000, 6000),'cpu': randint(3300, 4000)},
                 {'ip':'10.11.11.13','mem': randint(3000, 6000),'cpu': randint(3300, 4000)}],
         'band': randint(3300, 4000),
         'latency': uniform(0,0.5)},
          
         {'postal_address': 'Etschweg 1, 80806, Munich',
         'resources':[
                 {'ip':'10.11.24.10','mem': randint(3000, 6000),'cpu': randint(3300, 4000)},
                 {'ip':'10.11.24.11','mem': randint(3000, 6000),'cpu': randint(3300, 4000)},
                 {'ip':'10.11.24.12','mem': randint(3000, 6000),'cpu': randint(3300, 4000)},
                 {'ip':'10.11.24.13','mem': randint(3000, 6000),'cpu': randint(3300, 4000)}],
         'band': randint(3300, 4000),
         'latency': uniform(0,0.5)},
          
         {'postal_address': 'Etschweg 2, 80806, Munich',
         'resources':[
                 {'ip':'10.11.25.10','mem': randint(3000, 6000),'cpu': randint(3300, 4000)},
                 {'ip':'10.11.25.11','mem': randint(3000, 6000),'cpu': randint(3300, 4000)},
                 {'ip':'10.11.25.12','mem': randint(3000, 6000),'cpu': randint(3300, 4000)},
                 {'ip':'10.11.25.13','mem': randint(3000, 6000),'cpu': randint(3300, 4000)}],
         'band': randint(3300, 4000),
         'latency': uniform(0,0.5)}
        
        ]

def generate_edge_resources():
    '''
    generate properties of fog node randomly in a bulk amount 
    '''
    blocks = []
    for number in range (1 , 20):
        blocks.append(choice(city_blocks))
    return blocks

def generate_single_edge_resource():
    '''
    create static single resource properties
    '''
    #postal_code, address = generate_address()
    resource = {
        'ip': '10.10.11.11',
        'building': 'Alte Heide 2' ,
        'postal_code': 80805,
        'city': 'Munich',
        'cpu': 40000,
        'mem': 25000,
        'band': 33000,
        'latency': 0.001
        }
    return resource

def generate_single_iot_resource():
    '''
    create static single resource properties
    '''
    #postal_code, address = generate_address()
    resource = {
        'ip': '10.10.11.11',
        'building': 'Alte Heide 2' ,
        'postal_code': 80805,
        'city': 'Munich',
        'cpu': 40000,
        'mem': 25000,
        'band': 33000,
        'latency': 0.001
        }
    return resource

def generate_requirement():
    
    requirement = {
                    'cpu': randint(2000, 5000),
        'mem': randint(3000, 10000)
            }
    return requirement