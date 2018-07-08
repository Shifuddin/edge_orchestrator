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

engine_mngr = EngineManager()
resourcepool = ResourcePool(engine_mngr.place_resource)
servicepool = ServicePool(engine_mngr.place_service)


# add bulk resources
resourcepool.accept_bulk_resources(rg.generate_edge_resources())

engine_mngr.inspect_all_engines()

# add single resource
resourcepool.accept_resource(rg.generate_single_edge_resource())

servicepool.accept_service('hello shifudding', rg.generate_single_iot_resource())