#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 23:55:00 2018

@author: shifu
"""
import city_map as cm
class Regionsupervisor():
    
    def __init__(self, dao, region_name):
        self.dao = dao
        self.region_name = region_name
        
    def get_blocks(self):
    
        region_name = '%' + self.region_name+ '%'
        
        blocks = self.dao.get_blocks_of_region(region_name)
        
        for block in blocks:
            print (block.postal_address)
            
    def get_region_map(self):
        return cm.get_adjacency_list(self.region_name)
    