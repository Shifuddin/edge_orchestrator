# -*- coding: utf-8 -*-
"""
Spyder Editor

Resource pool accepts new resource at startup time
It accepts new resource at runtime
It also accepts resource for update
"""
from engine_manager import EngineManager
import resource_generation as rg
class ResourcePool():
    
    def __init__(self, callback):
        self.callback = callback
        
    def accept_resource(self, resource):
        '''
        accept a new resource
        @param resource: propertifes of fog node as dict 
        '''
        self.callback([resource])
    
    def accept_bulk_resources(self, resources):
        '''
        accept a list of resources
        @param resources: list of properties of fog nodes.
        '''
        self.callback(resources)
        
    
engine_mngr = EngineManager()
resourcepool = ResourcePool(engine_mngr.place_resource)
        
# add bulk resources
resourcepool.accept_bulk_resources(rg.generate_resources())

engine_mngr.inspect_all_engines()

# add single resource
resourcepool.accept_resource(rg.generate_single_resource())