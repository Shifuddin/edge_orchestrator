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
    def __init__(self, engine_name):
        self.engine_name = engine_name
        self.region_su = Regionsupervisor(self.get_region_map())
        self.scheduler = Scheduler(self.region_su)
    
    def get_region_map(self):
        postal_code = self.engine_name[-5:]
        return city_map.get_adjacency_list(int(postal_code))
    def add_to_region_supervisor(self, resource):
        self.region_su.add_new_resource(resource)
    def update_region_supervisor(self, resource):
        self.region_su.update_resource(resource)
    def show_engine_data(self):
        print (self.engine_name)
        print (self.region_su.get_current_resources())
        print (self.region_su.get_region_map())
    def add_to_scheduler(self, command, iot_resource):
        self.scheduler.schedule(command, iot_resource)