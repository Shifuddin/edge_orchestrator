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
        
    def bfs_adjacency_list(self, graph, start):
    
        result, queue = [], []
        queue.append(start)
        result.append(start)
        
        try:
            while queue:
                element = queue.pop()
                for adja in graph[element]:
                    if adja not in result:
                        queue.append(adja)
                        result.append(adja)
            return result
        except KeyError as KE:
            return 'Position in the region unknown ' + str(KE)
    
    def schedule(self, command, iot_resource):
        bfs = self.bfs_adjacency_list(self.region_sp.get_region_map(), iot_resource.get('building'))
        print (bfs)
        print ("Will schedule")
        print (iot_resource)
        
