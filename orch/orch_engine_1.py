#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 11:49:35 2018

@author: shifu
"""
from region_supervisor import Regionsupervisor
from service_scheduler import Scheduler
class Engine():
    def __init__(self, engine_name, dao):
        self.engine_name = engine_name
        region_name = engine_name[engine_name.find('_')+1:]
        self.region_su = Regionsupervisor(dao, region_name)
        self.scheduler = Scheduler(self.region_su)
    
    def assign_service_to_scheduler(self, task_details, origin_node):
        self.scheduler.schedule(task_details, origin_node)