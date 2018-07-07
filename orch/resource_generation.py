#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 15:17:31 2018

@author: shifu
"""

from random import randint, choice, uniform
def generate_address():
    '''
    generate space seperated address
    '''
    roads = ['Karl-Beck-Weg', 'Alte Heide']

    return choice(roads) + ' '+str(randint(1,2))

def generate_ip():
    return str(randint(1, 255)) + '.'+ str(randint(1, 255)) + '.' + str(randint(1, 255))+'.' + str(randint(1, 255))

def generate_resources():
    '''
    generate properties of fog node randomly in a bulk amount 
    '''
    resources = []
    for number in range (1 , 20):
        resource = {
        'ip': generate_ip(),
        'building': generate_address() ,
        'postal_code': randint(80331, 80335),
        'city': 'Munich',
        'cpu': randint(2000, 5000),
        'mem': randint(3000, 10000),
        'band': randint(30000, 50000),
        'latency': 0.001
        }
        resources.append(resource)
    return resources

def generate_single_resource():
    '''
    create static single resource properties
    '''
    resource = {
        'ip': '211.17.171.4',
        'building': 'Hans leipelt str. 7',
        'postal_code': 81522,
        'city': 'Munich',
        'cpu': 1000,
        'mem': 3000,
        'band': 33000,
        'latency': 0.01
        }
    return resource