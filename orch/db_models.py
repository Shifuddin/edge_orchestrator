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

class Block(Base):
    
    __tablename__ = 'regionblock'
    __table_args__ = {'useexisting':True}
    
    postal_address = Column(String, primary_key=True)
    band = Column(Numeric, nullable=False)
    latency = Column(Numeric, nullable=False)
    resources = relationship('Agent' , back_populates='block')
    
class Agent(Base):
    
    __tablename__ = 'regionagent'
    __table_args__ = {'useexisting':False}
    ip = Column(String, primary_key=True)
    cpu = Column(Numeric, nullable=False)
    memory = Column(Numeric, nullable=False)
    block_postal_address = Column(String, ForeignKey('regionblock.postal_address'), nullable=False)
    block = relationship('Block', back_populates='resources')
