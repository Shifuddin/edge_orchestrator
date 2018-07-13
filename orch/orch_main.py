#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 17:19:47 2018

@author: shifu
"""

from engine_manager import EngineManager
import resource_generation as rg
from resource_pool import ResourcePool
from service_pool_1 import ServicePool
from DatabaseAccess import Dao
import time

current_time = lambda : int (round(time.time() * 1000))
'''
Create data access object.
This object will be used by all classes through out the project
to add, update or search in the database
'''
dao = Dao('postgres:321', 'orchestrator')

'''
Engine manager is created here.
Engine manager will manage all the engines created 
Engine manager adds data to database, later engines accesses those data
'''
engine_mngr = EngineManager(dao)

'''
Resource pool is created here. 
Callback function of engine manage is gived here, so that when new 
resources arrive it calls the engine manage to make the entry into the db
'''
resourcepool = ResourcePool(engine_mngr.place_blocks)

'''
Service pool is created here. 
Callback function of engine manage is gived here, so that when new 
service arrives it calls the engine manager for scheduling
'''
servicepool = ServicePool(engine_mngr.place_service)


'''
Resource pool accepts resources here.
It is a high level interface to
add new resources to the orchestrator
'''
#resourcepool.accept_bulk_resources(rg.generate_edge_resources())

'''
Inspects blocks in each region supervisors
'''
engine_mngr.inspect_all_engines()

'''
Service pool accepts service here
It is a high level interface to 
assign new services to orchestrator for scheduling
'''

servicepool.accept_service('hello shifudding', rg.generate_task_details() ,rg.generate_origin_iot())



# add single resource
#resourcepool.accept_resource(rg.generate_single_edge_resource())

