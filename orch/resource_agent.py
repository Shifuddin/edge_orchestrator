#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 23:46:44 2018

@author: shifu
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Agent(Base):
    
    __tablename__ = 'resources'
    __table_args__ = {'useexisting':False}
    ip = Column(Integer, primary_key=True)
    building = Column(String, nullable=False)
    postal_code = Column(String, nullable=False)
    city = Column(String, nullable=False)
    cpu = Column(String, nullable=False)
    mem = Column(String, nullable=False)