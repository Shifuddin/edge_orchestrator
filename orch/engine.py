#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 11:49:35 2018

@author: shifu
"""
from region_supervisor import Regionsupervisor
class Engine():
    def __init__(self, engine_name):
        self.engine_name = engine_name
        self.region_su = Regionsupervisor()
    
    def add_to_region_supervisor(self, resource):
        self.region_su.add_new_raw_data(resource)
        
    def show_engine_data(self):
        print (self.engine_name)
        print (self.region_su.get_current_resources())