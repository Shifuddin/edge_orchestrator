#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 23:20:16 2018

@author: shifu
"""

class Scheduler():
    def __init__(self, region_supervisor):
        self.region_sp = region_supervisor
        print('scheduler created')
    
    def schedule(self, command, iot_resource):
        print ("Will schedule")
        print (iot_resource)