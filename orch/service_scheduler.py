#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 23:20:16 2018

@author: shifu
"""

class Scheduler():
    def __init__(self, region_supervisor):
        self.region_sp = region_supervisor
        

    def 
    def bfs_adjacency_list(self, graph, task_details, start_postal_address):
    
        result, queue = [], []
        
        start = start_postal_address[0:start_postal_address.find(',')]
        extra_part = start_postal_address[start_postal_address.find(',')+1:]
        
        print (start)
        print (extra_part)
        
        queue.append(start)
        result.append(start)
        
        block_obj = self.region_sp.dao.get_resouces_of_block(start_postal_address)
        
        if block_obj is not None:
            for resource in block_obj.resources:
                print (resource.ip)
        
        
        try:
            while queue:
                element = queue.pop()
                for adja in graph[element]:
                    if adja not in result:
                        queue.append(adja)
                        result.append(adja)
                        
                        adja_postal_address = adja + ',' + extra_part
                        block_obj = self.region_sp.dao.get_resouces_of_block(adja_postal_address)
        
                        if block_obj is not None:
                            for resource in block_obj.resources:
                                print (resource.ip)
            return result
        except KeyError as KE:
            return 'Position in the region unknown ' + str(KE)
    
    def schedule(self, task_details, origin_node):
        self.bfs_adjacency_list(self.region_sp.get_region_map(), task_details, origin_node.get('postal_address'))
        #print(self.region_sp.get_region_map())
        
 
        