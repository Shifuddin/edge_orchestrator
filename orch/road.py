#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 12:26:33 2018

@author: shifu
"""
from DatabaseAccess import Dao

import resource_generation as rg

blocks =rg.generate_edge_resources()

for block in blocks:
    print (block)