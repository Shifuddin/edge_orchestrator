#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 10:11:41 2018

@author: shifu
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_models import Block, Agent
from sqlalchemy.exc import IntegrityError
class Dao():
    
    def __init__(self, credintials, db):
        db_engine = create_engine('postgresql+psycopg2://'+credintials+ '@localhost/'+db, echo=False)
        self.Session = sessionmaker(bind=db_engine)
        
    
    def add_new_block(self,block):
        
        try:
            
            session = self.Session()
            block_obj = Block(postal_address= block.get('postal_address'), band=block.get('band'), latency=block.get('latency'))
            session.add(block_obj)
            print("ok")
            resources_agent = [Agent(ip=resource.get('ip'), cpu=resource.get('cpu'), memory=resource.get('memory'), block_postal_address=block_obj.postal_address) for resource in block.get('resources')]
            block_obj.resources = resources_agent
            session.commit()
            print ('ok')
            return True
        except IntegrityError:
            return False
        except Exception as e:
            print (e)
        
    def get_blocks_of_region(self, region_name):
        session = self.Session()
        
        blocks = session.query(Block).filter(Block.postal_address.like(region_name)).all()
        
        return blocks
    def update_block_properties(self, block):
        session= self.Session()
        
        block_obj = session.query(Block).filter_by(postal_address= block.get('postal_address')).first()
        
        block_obj.band = block.get('band')
        block_obj.latency = block.get('latency')
        
        session.commit()
        
    def check_region_exists(self, region_name):
        
        if self.get_blocks_of_region(region_name):
            return True
        else:
            return False
        

