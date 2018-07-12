#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 23:55:00 2018

@author: shifu
"""

class Regionsupervisor():
    
    def __init__(self, dao, engine_name):
        self.dao = dao
        self.engine_name = engine_name
        
    def get_blocks(self):
        
        region_name = self.engine_name[self.engine_name.find('_')+1:]
        blocks = self.dao.get_blocks_of_region(region_name)
        
        for block in blocks:
            print (block.postal_address)
            
    def get_region_map(self):
        return self.region_map
    