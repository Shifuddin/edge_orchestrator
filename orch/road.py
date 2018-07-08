#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 12:26:33 2018

@author: shifu
"""

import random


roads = ['Hans-Leipelt-Straße', 'Heimstättenstraße', 'Karl-Beck-Weg'
         , 'Fröttmaninger Straße', 'Guerickestraße', 'Karl-Beck-Weg',
         'Alte Heide', 'Beltweg', 'Berliner Straße', 'Etschweg']


def bfs_adjacency_list(graph, start):
    
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
        return 'Cant found ' + str(KE)
    
    

        
    
bfs_adjacency_list(, 'Karl-Beck-Weg 1')

