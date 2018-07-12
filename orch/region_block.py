#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 23:46:44 2018

@author: shifu
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class RegionBlock(Base):
    
    __tablename__ = 'regionblocks'
    __table_args__ = {'useexisting':False}
    postal_address = Column(String, primary_key=True)
    band = Column(Numeric, nullable=False)
    latency = Column(Numeric, nullable=False)
    
    
class ResourceAgent(Base):
    
    __tablename__ = 'resourceagents'
    __table_args__ = {'useexisting':False}
    ip = Column(String, primary_key=True)
    cpu = Column(Numeric, nullable=False)
    memory = Column(Numeric, nullable=False)
    postal_address = Column(String, ForeignKey('regionblocks.postal_address'))
    block = relationship('RegionBlock', back_populates='resourceagents')

RegionBlock.resources = relationship('ResourceAgent', back_populates='block')