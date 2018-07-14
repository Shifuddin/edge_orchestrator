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
            cpu_time = (task_details.get('cpu_mips_profiled_machine')/ resource.cpu_mips) * Decimal(task_details.get('cpu_time_predicted_sc'))
            avg_wt = resource.avg_wt
            dtt = Decimal(task_details.get('data_size_mb') / avg_band) + Decimal(Decimal((task_details.get('data_size_mb') / 64 ) )* total_latency)
            
            total_ex_time = cpu_time + avg_wt + dtt
            yield total_ex_time, task_details.get('required_exe_time_sc'), resource.ip
            
            '''
            if total_ex_time <= task_details.get('required_exe_time_sc'):
                yield total_ex_time, task_details.get('required_exe_time_sc'), resource.ip
            '''
    
    def get_exec_time(self, resource, band, latency,from_origin):
        
        avg_band = (self.origin_block.band + band) /2
        if from_origin == True:
            total_latency = 0
        else:
            total_latency = (self.origin_block.latency + latency)
        
        cpu_time = (self.task_details.get('cpu_mips_profiled_machine')/ resource.cpu_mips) * Decimal(self.task_details.get('cpu_time_predicted_sc'))
        avg_wt = resource.avg_wt
        dtt = Decimal(self.task_details.get('data_size_mb') / avg_band) + Decimal(Decimal((self.task_details.get('data_size_mb') / 64 ) )* total_latency)
            
        total_ex_time = cpu_time + avg_wt + dtt            
        
        return total_ex_time
    def third_party(self, block_obj, from_origin):
        
        if from_origin == True:
            block_obj = self.origin_block
            
        for resource in block_obj.resources:
            yield resource.ip, self.get_exec_time(resource, block_obj.band, block_obj.latency, from_origin)
            
    def bfs_adjacency_list(self, graph, task_details, origin_postal_address):
    
        result, queue = [], []
        
        origin = origin_postal_address[0:origin_postal_address.find(',')]
        extra_part = origin_postal_address[origin_postal_address.find(',')+1:]
        
        queue.append(origin)
        result.append(origin)
        
        min_node = {'address':'','time': 10000, 'ip': ''}
        matched_nodes =[]
        self.origin_block = self.region_sp.dao.get_block_from_postal_address(origin_postal_address)
        
        if self.origin_block is not None:
            
            all_ex_time = self.third_party(None, True)
            
            for ip, ex_time in all_ex_time:
                
                if ex_time < min_node.get('time'):
                    min_node['time'] = ex_time
                    min_node['ip'] = ip
                    min_node['address'] = origin_postal_address
                
                if ex_time <= self.task_details.get('required_exe_time_sc'):
                    matched_nodes.append({'address':origin_postal_address,'ip':ip,'time':ex_time})
                 
                if len(matched_nodes) >= 2:
                    return matched_nodes            

        else:
            print ('Task origin can''t be found')
            
        try:
            while queue:
                element = queue.pop()
                for adja in graph[element]:
                    if adja not in result:
                        queue.append(adja)
                        result.append(adja)
                        
                        adja_postal_address = adja + ',' + extra_part
                        cur_block_obj = self.region_sp.dao.get_block_from_postal_address(adja_postal_address)
                        
                        if cur_block_obj is not None:
                            
                            all_ex_time = self.third_party(cur_block_obj, False)
                            for ip, ex_time in all_ex_time:
                                #print (ip + ' Required time ' + str(ex_time) + ' expected: ' + str(self.task_details.get('required_exe_time_sc')))
                                if ex_time < min_node.get('time'):
                                    min_node['time'] = ex_time
                                    min_node['ip'] = ip
                                    min_node['address'] = adja_postal_address
                
                                if ex_time <= self.task_details.get('required_exe_time_sc'):
                                    matched_nodes.append({'address':adja_postal_address,'ip':ip,'time':ex_time})
                
                                if len(matched_nodes) >= 2:
                                    return matched_nodes

                       
            
            return [min_node]
        except KeyError as KE:
            return 'Position in the region unknown ' + str(KE)
        
    
    def schedule(self, task_details, origin_node):
        
        self.task_details = task_details
        print ('Origin of the task ' + origin_node.get('postal_address'))
        matched_nodes = self.bfs_adjacency_list(self.region_sp.get_region_map(), task_details, origin_node.get('postal_address'))
        
        print ('Expected ' + str(self.task_details.get('required_exe_time_sc')))
        print (matched_nodes)
        #print(self.region_sp.get_region_map())
        
 
        