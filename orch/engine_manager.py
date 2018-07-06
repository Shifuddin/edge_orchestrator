#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 22:10:00 2018

@author: shifu
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from resource_agent import Agent
from orch_engine import Engine
class EngineManager():
    def __init__(self):
        self.db_engine = create_engine('postgresql+psycopg2://postgres:321@localhost/orchestrator', echo=False)
        self.Session = sessionmaker(bind=self.db_engine)
        self.engine_list = []
    
    def add_agent_db(self, session, resource):
        '''
        insert new agen / fog node to database
        '''
        ag = Agent(ip=resource.get('ip'), building = resource.get('building'),
                   postal_code = resource.get('postal_code'), city=resource.get('city'),
                   cpu= resource.get('cpu'), mem=resource.get('mem'))
        session.add(ag)
        session.commit()
        
        
    def update_agent(self, old_agent, resource, session):
        
        '''
        update capabilities of  a fog node for example cpu, memory
        '''
        old_agent.building = resource.get('building')
        old_agent.postal_code= resource.get('postal_code')
        old_agent.city = resource.get('city')
        old_agent.cpu = resource.get('cpu')
        old_agent.mem = resource.get('mem')
        session.commit()
        
        
    def check_db(self, resource, session):
        '''
        check weather a agent / resource already in the database
        if yes, just update the properties of the resource
        if no, add the resource to database, check wheather there is a engine for that region
        '''
        old_agent = session.query(Agent).filter_by(ip = resource.get('ip')).first()
        if old_agent is None:
            self.add_agent_db(session, resource)
            self.check_engine(resource.get('city') + '_' + str(resource.get('postal_code')), resource)
        else:
            self.update_agent(old_agent, resource, session)
            self.pass_updated_resource(resource.get('city') + '_' + str(resource.get('postal_code')), resource)
    
    def check_engine(self, engine_name, resource):
        '''
        Check wheather a engine already exists
        if yes, just give the resource to region manager of that engine.
        '''
        for orch_eng in self.engine_list:
            if engine_name == orch_eng.engine_name:
                orch_eng.add_resource(resource)
                print ('Engine already exists')
                return
        
        self.create_new_engine(engine_name, resource)
    
    def pass_updated_resource(self, engine_name, resource):
        '''
        pass update resource to a particular engine
        '''
        for orch_eng in self.engine_list:
            if engine_name == orch_eng.engine_name:
                orch_eng.add_resource(resource)
                return
    
    def create_new_engine(self, engine_name, resource):
        '''
        Create new engine and pass resource to that engine
        '''
        orch_en = Engine(engine_name)
        self.engine_list.append(orch_en)
        orch_en.add_resource(resource)
        print (len(self.engine_list))
        
    def place_resource(self, resources):
        '''
        Take resources from resouce pool to be placed to region manager of a engine
        '''
        session = self.Session()
        {self.check_db(resource, session) for resource in resources}
        
    def inspect_all_engines(self):
        
        for engine in self.engine_list:
            print(engine.region_su.get_current_resources())
        
        