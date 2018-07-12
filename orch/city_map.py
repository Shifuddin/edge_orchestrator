#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 15:38:54 2018

@author: shifu
"""

graph_adjacency_list_80805 = {'Alte Heide 1': set([ 'Alte Heide 2', 'Frottmaninger Str 1']),
        'Alte Heide 2': set(['Alte Heide 1', 'Alte Heide 3', 'Frottmaninger Str 2']),
        'Alte Heide 3': set(['Alte Heide 2', 'Alte Heide 4', 'Frottmaninger Str 3']),
        'Alte Heide 4': set(['Alte Heide 3', 'Frottmaninger Str 4']),
        'Frottmaninger Str 1': set(['Alte Heide 1', 'Frottmaninger Str 2', 'Hans-Leipelt-Str 1']),
        'Frottmaninger Str 2': set(['Frottmaninger Str 1', 'Alte Heide 2','Frottmaninger Str 3', 'Hans-Leipelt-Str 2']),
        'Frottmaninger Str 3': set(['Frottmaninger Str 2', 'Alte Heide 3','Frottmaninger Str 4', 'Hans-Leipelt-Str 3']),
        'Frottmaninger Str 4': set(['Frottmaninger Str 3', 'Alte Heide 4', 'Hans-Leipelt-Str 4']),
        'Hans-Leipelt-Str 1': set(['Frottmaninger Str 1', 'Hans-Leipelt-Str 2', 'Christoph-Probst-str 1']),
        'Hans-Leipelt-Str 2': set(['Hans-Leipelt-Str 1', 'Frottmaninger Str 2', 'Hans-Leipelt-Str 3', 'Christoph-Probst-str 2']),
        'Hans-Leipelt-Str 3': set(['Hans-Leipelt-Str 2', 'Frottmaninger Str 3', 'Hans-Leipelt-Str 4', 'Christoph-Probst-str 3']),
        'Hans-Leipelt-Str 4': set(['Hans-Leipelt-Str 3', 'Frottmaninger Str 4', 'Christoph-Probst-str 4']),
        'Christoph-Probst-str 1': set(['Hans-Leipelt-Str 1', 'Christoph-Probst-str 2']),
        'Christoph-Probst-str 2': set(['Christoph-Probst-str 1', 'Hans-Leipelt-Str 2', 'Christoph-Probst-str 3']),
        'Christoph-Probst-str 3': set(['Christoph-Probst-str 2', 'Hans-Leipelt-Str 3', 'Christoph-Probst-str 4']),
        'Christoph-Probst-str 4': set(['Christoph-Probst-str 3', 'Hans-Leipelt-Str 4'])}

graph_adjacency_list_80806 = {'Beltweg 1': set([ 'Beltweg 2', 'Guerickestra 1']),
        'Beltweg 2': set(['Beltweg 1', 'Beltweg 3', 'Guerickestra 2']),
        'Beltweg 3': set(['Beltweg 2', 'Beltweg 4', 'Guerickestra 3']),
        'Beltweg 4': set(['Beltweg 3', 'Guerickestra 4']),
        'Guerickestra 1': set(['Beltweg 1', 'Guerickestra 2', 'Etschweg 1']),
        'Guerickestra 2': set(['Guerickestra 1', 'Beltweg 2', 'Guerickestra 3', 'Etschweg 2']),
        'Guerickestra 3': set(['Guerickestra 2', 'Beltweg 3', 'Guerickestra 4', 'Etschweg 3']),
        'Guerickestra 4': set(['Guerickestra 3', 'Beltweg 4',  'Etschweg 4']),
        'Etschweg 1': set(['Guerickestra 1', 'Etschweg 2', 'Karl-Beck-Weg 1']),
        'Etschweg 2': set(['Etschweg 1', 'Guerickestra 2', 'Etschweg 3', 'Karl-Beck-Weg 2']),
        'Etschweg 3': set(['Etschweg 2', 'Guerickestra 3', 'Etschweg 4', 'Karl-Beck-Weg 3']),
        'Etschweg 4': set(['Etschweg 3', 'Guerickestra 3', 'Karl-Beck-Weg 4']),
        'Karl-Beck-Weg 1': set(['Etschweg 1', 'Karl-Beck-Weg 2']),
        'Karl-Beck-Weg 2': set(['Karl-Beck-Weg 1', 'Etschweg 2', 'Karl-Beck-Weg 3']),
        'Karl-Beck-Weg 3': set(['Karl-Beck-Weg 2', 'Etschweg 3', 'Karl-Beck-Weg 4']),
        'Karl-Beck-Weg 4': set(['Karl-Beck-Weg 3', 'Etschweg 3'])}

list_graph_adjacency_list = [{'code':80805, 'graph_ad_list':graph_adjacency_list_80805},
                             {'code':80806, 'graph_ad_list':graph_adjacency_list_80806}
                             ]
def get_adjacency_list(postal_code):   
    for graph_adjacency_list in list_graph_adjacency_list:
        if graph_adjacency_list.get('code') == int(postal_code):
            return graph_adjacency_list.get('graph_ad_list')
        
