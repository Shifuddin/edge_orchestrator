#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 23:55:00 2018

@author: shifu
"""

class Regionsupervisor():
    def __init__(self):
        self.raw_data = []
    
    def add_new_raw_data(self, resource):
        self.raw_data.append(resource)
    def get_current_resources(self):
        return self.raw_data