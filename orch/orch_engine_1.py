#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 11:49:35 2018

@author: shifu
"""
from region_supervisor import Regionsupervisor
from service_scheduler import Scheduler
import city_map
class Engine():
    def __init__(self, engine_name, dao):
        self.engine_name = engine_name
        self.region_su = Regionsupervisor(dao, engine_name)
        self.scheduler = Scheduler(self.region_su)
    
    def get_region_map(self):
        postal_code = self.engine_name[-5:]
        return city_map.get_adjacency_list(int(postal_code))
    
    def assign_service_to_scheduler(self, requirement, iot_resource):
        self.scheduler.schedule(requirement, iot_resource)