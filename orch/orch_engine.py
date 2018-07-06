#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 11:49:35 2018

@author: shifu
"""

class Engine():
    def __init__(self, engine_name):
        self.engine_name = engine_name
        
    def add_resource(self, resource):
        print (self.engine_name)
        print (resource)