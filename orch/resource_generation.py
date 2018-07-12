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
                 {'ip':'10.10.10.10','memory_mb': randint(3000, 6000),'cpu_mips': randint(3300, 4000), 'avg_wt':uniform(0,1)},
                 {'ip':'10.10.10.11','memory_mb': randint(3000, 6000),'cpu_mips': randint(3300, 4000), 'avg_wt':uniform(0,1)},
                 {'ip':'10.10.10.12','memory_mb': randint(3000, 6000),'cpu_mips': randint(3300, 4000), 'avg_wt':uniform(0,1)},
                 {'ip':'10.10.10.13','memory_mb': randint(3000, 6000),'cpu_mips': randint(3300, 4000), 'avg_wt':uniform(0,1)}],
         'band': randint(3300, 4000),
         'latency': uniform(0,0.5)},
        
         {'postal_address': 'Alte Heide 2, 80805, Munich',
         'resources':[
                 {'ip':'10.10.11.10','memory_mb': randint(3000, 6000),'cpu_mips': randint(3300, 4000), 'avg_wt':uniform(0,1)},
                 {'ip':'10.10.11.11','memory_mb': randint(3000, 6000),'cpu_mips': randint(3300, 4000), 'avg_wt':uniform(0,1)},
                 {'ip':'10.10.11.12','memory_mb': randint(3000, 6000),'cpu_mips': randint(3300, 4000), 'avg_wt':uniform(0,1)},
                 {'ip':'10.10.11.13','memory_mb': randint(3000, 6000),'cpu_mips': randint(3300, 4000), 'avg_wt':uniform(0,1)}],
         'band': randint(3300, 4000),
         'latency': uniform(0,0.5)},
          
          
         {'postal_address': 'Hans-Leipelt-Str 1, 80805, Munich',
         'resources':[
                 {'ip':'10.10.24.10','memory_mb': randint(3000, 6000),'cpu_mips': randint(3300, 4000), 'avg_wt':uniform(0,1)},
                 {'ip':'10.10.24.11','memory_mb': randint(3000, 6000),'cpu_mips': randint(3300, 4000), 'avg_wt':uniform(0,1)},
                 {'ip':'10.10.24.12','memory_mb': randint(3000, 6000),'cpu_mips': randint(3300, 4000), 'avg_wt':uniform(0,1)},
                 {'ip':'10.10.24.13','memory_mb': randint(3000, 6000),'cpu_mips': randint(3300, 4000), 'avg_wt':uniform(0,1)}],
         'band': randint(3300, 4000),
         'latency': uniform(0,0.5)},
          
          
         {'postal_address': 'Hans-Leipelt-Str 2, 80805, Munich',
         'resources':[
                 {'ip':'10.10.25.10','memory_mb': randint(3000, 6000),'cpu_mips': randint(3300, 4000), 'avg_wt':uniform(0,1)},
                 {'ip':'10.10.25.11','memory_mb': randint(3000, 6000),'cpu_mips': randint(3300, 4000), 'avg_wt':uniform(0,1)},
                 {'ip':'10.10.25.12','memory_mb': randint(3000, 6000),'cpu_mips': randint(3300, 4000), 'avg_wt':uniform(0,1)},
                 {'ip':'10.10.25.13','memory_mb': randint(3000, 6000),'cpu_mips': randint(3300, 4000), 'avg_wt':uniform(0,1)}],
         'band': randint(3300, 4000),
         'latency': uniform(0,0.5)},
          
         {'postal_address': 'Beltweg 1, 80806, Munich',
         'resources':[
                 {'ip':'10.11.10.10','memory_mb': randint(3000, 6000),'cpu_mips': randint(3300, 4000), 'avg_wt':uniform(0,1)},
                 {'ip':'10.11.10.11','memory_mb': randint(3000, 6000),'cpu_mips': randint(3300, 4000), 'avg_wt':uniform(0,1)},
                 {'ip':'10.11.10.12','memory_mb': randint(3000, 6000),'cpu_mips': randint(3300, 4000), 'avg_wt':uniform(0,1)},
                 {'ip':'10.11.10.13','memory_mb': randint(3000, 6000),'cpu_mips': randint(3300, 4000), 'avg_wt':uniform(0,1)}],
         'band': randint(3300, 4000),
         'latency': uniform(0,0.5)},
          
         {'postal_address': 'Beltweg 2, 80806, Munich',
         'resources':[
                 {'ip':'10.11.11.10','memory_mb': randint(3000, 6000),'cpu_mips': randint(3300, 4000), 'avg_wt':uniform(0,1)},
                 {'ip':'10.11.11.11','memory_mb': randint(3000, 6000),'cpu_mips': randint(3300, 4000), 'avg_wt':uniform(0,1)},
                 {'ip':'10.11.11.12','memory_mb': randint(3000, 6000),'cpu_mips': randint(3300, 4000), 'avg_wt':uniform(0,1)},
                 {'ip':'10.11.11.13','memory_mb': randint(3000, 6000),'cpu_mips': randint(3300, 4000), 'avg_wt':uniform(0,1)}],
         'band': randint(3300, 4000),
         'latency': uniform(0,0.5)},
          
         {'postal_address': 'Etschweg 1, 80806, Munich',
         'resources':[
                 {'ip':'10.11.24.10','memory_mb': randint(3000, 6000),'cpu_mips': randint(3300, 4000), 'avg_wt':uniform(0,1)},
                 {'ip':'10.11.24.11','memory_mb': randint(3000, 6000),'cpu_mips': randint(3300, 4000), 'avg_wt':uniform(0,1)},
                 {'ip':'10.11.24.12','memory_mb': randint(3000, 6000),'cpu_mips': randint(3300, 4000), 'avg_wt':uniform(0,1)},
                 {'ip':'10.11.24.13','memory_mb': randint(3000, 6000),'cpu_mips': randint(3300, 4000), 'avg_wt':uniform(0,1)}],
         'band': randint(3300, 4000),
         'latency': uniform(0,0.5)},
          
         {'postal_address': 'Etschweg 2, 80806, Munich',
         'resources':[
                 {'ip':'10.11.25.10','memory_mb': randint(3000, 6000),'cpu_mips': randint(3300, 4000), 'avg_wt':uniform(0,1)},
                 {'ip':'10.11.25.11','memory_mb': randint(3000, 6000),'cpu_mips': randint(3300, 4000), 'avg_wt':uniform(0,1)},
                 {'ip':'10.11.25.12','memory_mb': randint(3000, 6000),'cpu_mips': randint(3300, 4000), 'avg_wt':uniform(0,1)},
                 {'ip':'10.11.25.13','memory_mb': randint(3000, 6000),'cpu_mips': randint(3300, 4000), 'avg_wt':uniform(0,1)}],
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



def generate_origin_iot():
    '''
    create static single resource properties
    '''
    #postal_code, address = generate_address()
    resource = {
        
        'postal_address': 'Hans-Leipelt-Str 2, 80805, Munich' ,
        'ip': '10.10.11.11'
        }
    return resource

def generate_task_details():
    
    task_details = {
        'cpu_time_predicted_sc': uniform(1, 6),
        'cpu_mips_profiled_machine': randint(3000, 10000),
        'required_exe_time_sc': uniform(1,6),
        'data_size_mb': randint(20, 40)
            }
    return task_details