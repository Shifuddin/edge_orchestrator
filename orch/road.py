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

print (random.choice(roads) + ' '+str(random.randint(1,5)))