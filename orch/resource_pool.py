# -*- coding: utf-8 -*-
"""
Spyder Editor

Resource pool accepts new resource at startup time
It accepts new resource at runtime
It also accepts resource for update
"""

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
        
    