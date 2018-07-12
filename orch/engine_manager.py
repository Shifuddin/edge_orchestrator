#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 22:10:00 2018

@author: shifu
"""
from orch_engine_1 import Engine
class EngineManager():
    def __init__(self, dao):
        self.engine_list = []
        self.dao = dao
        self.create_engine_on_startup()
        
    def create_engine_on_startup(self):
        blocks = self.dao.get_all_blocks()
        
        for block in blocks:
            postal_address = block.postal_address
            region_name = postal_address[postal_address.find(',')+2: postal_address.rfind(',')]
            city_name = postal_address[postal_address.rfind(',')+2:]
            self.create_new_engine(city_name+'_'+region_name)
            
    def check_engine_exists(self, engine_name):
        for engine in self.engine_list:
            if engine.engine_name == engine_name:
                return True
        return False
        
    def create_new_engine(self, engine_name):
        '''
        Create new engine and pass resource to that engine
        '''
        if self.check_engine_exists(engine_name):
            print ('Engine already exists')
        else:
            
            orch_en = Engine(engine_name, self.dao)
            self.engine_list.append(orch_en)
    
    def place_blocks(self, blocks):
        '''
        Take blocks from resouce pool to be added to the database
        '''
        for block in blocks:
            if self.dao.add_new_block(block):
                postal_address = block.get('postal_address')
                region_name = postal_address[postal_address.find(',')+2: postal_address.rfind(',')]
                city_name = postal_address[postal_address.rfind(',')+2:]
                self.create_new_engine(city_name+'_'+region_name)
            else:
                print ("Block already exists. Need block update or resource update")
                
                
        
    def place_service(self, command, task_details, origin_node):
        
        origin_postal_address = origin_node.get('postal_address')
        region_name = origin_postal_address[origin_postal_address.find(',')+2: origin_postal_address.rfind(',')]
        city_name = origin_postal_address[origin_postal_address.rfind(',')+2:]
        engine_name = city_name + '_'+ region_name
        for engine in self.engine_list:
            if engine_name == engine.engine_name:
                engine.assign_service_to_scheduler(task_details, origin_node)
        
                
    def inspect_all_engines(self):
        
        for engine in self.engine_list:
            print (engine.engine_name)
            engine.region_su.get_blocks()
            print ('\n')
        
        