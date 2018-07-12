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
        
    def get_resource_from_block(self, block):
        resources = self.region_sp.get_current_resources()
        
        #result_resources = []
        for resource in resources:
            if resource.get('building') == block:
                yield resource
        #return result_resources
        
    def check_requirement_matches(self, requriments, block):
        
        resources_block = self.get_resource_from_block(block)
        
        for r_b in resources_block:
            if r_b.get('mem') >= requriments.get('mem') and r_b.get('cpu') >= requriments.get('cpu'):
                yield r_b
    def bfs_adjacency_list(self, graph, start, requirements):
    
        result, queue = [], []
        queue.append(start)
        result.append(start)
        matched_nodes = self.check_requirement_matches(requirements, start)
        
        for node in matched_nodes:
            print (node)
        try:
            while queue:
                element = queue.pop()
                for adja in graph[element]:
                    if adja not in result:
                        queue.append(adja)
                        result.append(adja)
                        matched_nodes = self.check_requirement_matches(requirements, adja)
        
                        for node in matched_nodes:
                            print (node)
            return result
        except KeyError as KE:
            return 'Position in the region unknown ' + str(KE)
    
    def schedule(self, requirements, iot_resource):
        print (requirements)
        print ('Generated at :' + iot_resource.get('building'))
        self.bfs_adjacency_list(self.region_sp.get_region_map(), iot_resource.get('building'), requirements)
        
 
        
