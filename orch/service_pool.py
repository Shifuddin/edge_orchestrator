#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 17:15:16 2018

@author: shifu
"""

class ServicePool():
    
    def __init__(self, callback):
        self.callback = callback
        
    def accept_sevice(self, command, iot_resource):
        self.callback([command], [iot_resource])
    