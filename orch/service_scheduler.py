#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 23:20:16 2018

@author: shifu
"""
from decimal import Decimal
class Scheduler():
    def __init__(self, region_supervisor):
        self.region_sp = region_supervisor
        

    def apply_cost_function_on_resources(self, task_details, origin_block_band, current_block_band, origin_block_latency, current_block_latency, current_resources, origin_node):
        avg_band = (origin_block_band + current_block_band) /2
        if origin_node == True:
            total_latency = 0
        else:
            total_latency = (origin_block_latency + current_block_latency)
            
        for resource in current_resources:
            #print (str (task_details.get('cpu_mips_profiled_machine') ) +  ' ' + str(resource.cpu_mips) + ' ' + str(task_details.get('cpu_time_predicted_sc')))
            cpu_time = (task_details.get('cpu_mips_profiled_machine')/ resource.cpu_mips) * Decimal(task_details.get('cpu_time_predicted_sc'))
            avg_wt = resource.avg_wt
            dtt = Decimal(task_details.get('data_size_mb') / avg_band) + Decimal(Decimal((task_details.get('data_size_mb') / 64 ) )* total_latency)
            
            total_ex_time = cpu_time + avg_wt + dtt
            if total_ex_time <= task_details.get('required_exe_time_sc'):
                print (str(cpu_time) + ' ' + str(avg_wt ) + ' ' + str(dtt) + ' rq '+ str(task_details.get('required_exe_time_sc')))
            
                print (resource.ip)
            
            
    def bfs_adjacency_list(self, graph, task_details, origin_postal_address):
    
        result, queue, matched_nodes = [], [], []
        
        origin = origin_postal_address[0:origin_postal_address.find(',')]
        extra_part = origin_postal_address[origin_postal_address.find(',')+1:]
        print (origin)
        queue.append(origin)
        result.append(origin)
        
        origin_block = self.region_sp.dao.get_block_from_postal_address(origin_postal_address)
        
        if origin_block is not None:
            origin_block_band = origin_block.band
            origin_block_latency = origin_block.latency
        
            self.apply_cost_function_on_resources(task_details, origin_block_band, origin_block_band, origin_block_latency, origin_block_latency, origin_block.resources, True)
        else:
            print ('Task origin can''t be found')
        try:
            while queue:
                element = queue.pop()
                for adja in graph[element]:
                    if adja not in result:
                        queue.append(adja)
                        result.append(adja)
                        print (adja)
                        adja_postal_address = adja + ',' + extra_part
                        cur_block_obj = self.region_sp.dao.get_block_from_postal_address(adja_postal_address)
                        if cur_block_obj is not None:
                            self.apply_cost_function_on_resources(task_details, origin_block_band, cur_block_obj.band, origin_block_latency, cur_block_obj.latency, cur_block_obj.resources, False)
        
                       
            return result
        except KeyError as KE:
            return 'Position in the region unknown ' + str(KE)
    
    def schedule(self, task_details, origin_node):
        self.bfs_adjacency_list(self.region_sp.get_region_map(), task_details, origin_node.get('postal_address'))
        #print(self.region_sp.get_region_map())
        
 
        