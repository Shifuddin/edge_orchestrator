#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 23:55:00 2018

@author: shifu
"""

class Regionsupervisor():
    def __init__(self, region_map):
        self.raw_data = []
        self.region_map = region_map
    
    def add_new_resource(self, resource):
        self.raw_data.append(resource)
        
    def update_resource(self, resource):
        for rs in self.raw_data:
            if rs.get('ip') == resource.get('ip'):
                self.raw_data.remove(rs)
                self.raw_data.append(resource)
    def get_current_resources(self):
        return self.raw_data
    def show_region_map(self):
        return self.region_map
    