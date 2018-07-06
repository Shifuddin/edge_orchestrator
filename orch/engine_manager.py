#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 22:10:00 2018

@author: shifu
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from resource_agent import Agent
from sqlalchemy.exc import IntegrityError
from orch_engine import Engine
class EngineManager():
    def __init__(self):
        self.db_engine = create_engine('postgresql+psycopg2://postgres:321@localhost/orchestrator', echo=False)
        self.Session = sessionmaker(bind=self.db_engine)
        self.engine_list = []
    
    def add_agent_db(self, resource, session):
        print ()
    def update_agent(self, old_agent, resource, session):
        print ()
    def check_db(self, resource, session):
        
        old_agent = session.query(Agent).filter_by(ip = resource.get('ip')).first()
        if old_agent is None:
            print ('New agent')
        else:
            print ('old agent')
        '''
        ag = Agent(ip=resource.get('ip'), building = resource.get('building'),
                   postal_code = resource.get('postal_code'), city=resource.get('city'),
                   cpu= resource.get('cpu'), mem=resource.get('mem'))
        session.add(ag)
        
        try:
            session.commit()
            self.create_engine(resource.get('city') + '_' + str (resource.get('postal_code')), resource)
        except IntegrityError as IE:
            old_agent = session.query(Agent).filter_by(ip = resource.get('ip')).first()
            old_agent.postal_code = 1010
            session.commit()
            print ('Agent updated')
        '''
    
    def create_engine(self, engine_name, resource):
        
        for orch_eng in self.engine_list:
            if engine_name == orch_eng.engine_name:
                orch_eng.add_resource(resource)
                print ('Engine already exists')
                return
        
        orch_en = Engine(engine_name)
        self.engine_list.append(orch_en)
        orch_en.add_resource(resource)
        print (len(self.engine_list))
    def place_resource(self, resources):
        session = self.Session()
        {self.check_db(resource, session) for resource in resources}
        