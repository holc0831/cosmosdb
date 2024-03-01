#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 14:21:35 2021

@author: Justin Ho
"""

import time
import sys
import json

from azure.cosmos import exceptions, CosmosClient, PartitionKey

# Initialize the Cosmos client
endpoint =" endpoint"
key = 'key'

# <create_cosmos_client>
client = CosmosClient(endpoint, key)

database_name = 'name'
database = client.get_database_client(database_name)
container_name = 'name'
container = database.get_container_client(container_name)



if __name__ == '__main__':
  try:     
      for item in container.query_items(
            query='SELECT * FROM mycontainer r WHERE r.id="system_status"',
            enable_cross_partition_query=True):     #get the raw controller data from cosmosDB
        system_status= item["Inputs"]   
  
  except:
    with open('system_status.txt') as json_file:
        system_stauts= json.load(json_file)
  
  
  except KeyboardInterrupt:
  break
  except:
  pass
        

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
