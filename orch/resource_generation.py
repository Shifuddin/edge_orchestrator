#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 15:17:31 2018

@author: shifu
"""

from random import randint, choice
def generate_address():
    '''
    generate space seperated address
    '''
    address_80805 = [{ 'building': 'Alte Heide 1', 'ip': '10.10.10.10'},
           { 'building': 'Alte Heide 1', 'ip': '10.10.10.11'},
           { 'building': 'Alte Heide 2', 'ip': '10.10.11.10'},
           { 'building': 'Alte Heide 2', 'ip': '10.10.11.11'},
           { 'building': 'Hans-Leipelt-Str 1', 'ip': '10.10.14.10'},
           { 'building': 'Hans-Leipelt-Str 1', 'ip': '10.10.14.11'},
           { 'building': 'Hans-Leipelt-Str 2', 'ip': '10.10.15.10'},
           { 'building': 'Hans-Leipelt-Str 2', 'ip': '10.10.15.11'},
        ]
    address_80806 = [{ 'building': 'Beltweg 1', 'ip': '10.10.20.10'},
           { 'building': 'Beltweg 1', 'ip': '10.10.20.11'},
           { 'building': 'Beltweg 2', 'ip': '10.10.21.10'},
           { 'building': 'Beltweg 2', 'ip': '10.10.21.11'},
           { 'building': 'Etschweg 1', 'ip': '10.10.25.10'},
           { 'building': 'Etschweg 1', 'ip': '10.10.25.11'},
           { 'building': 'Etschweg 2', 'ip': '10.10.26.10'},
           { 'building': 'Etschweg 2', 'ip': '10.10.26.11'},
        ]
    
    postal_areas =[{'code': 80805, 'address': address_80805},
              {'code': 80806, 'address': address_80806}]
    postal_area = choice(postal_areas)
    address = choice(postal_area.get('address'))
    
    return postal_area.get('code'), address
    
def generate_edge_resources():
    '''
    generate properties of fog node randomly in a bulk amount 
    '''
    resources = []
    for number in range (1 , 20):
        postal_code, address = generate_address()
        resource = {
        'ip': address.get('ip'),
        'building': address.get('building') ,
        'postal_code': postal_code,
        'city': 'Munich',
        'cpu': randint(2000, 5000),
        'mem': randint(3000, 10000),
        'band': randint(30000, 50000),
        'latency': 0.001
        }
        resources.append(resource)
    return resources

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