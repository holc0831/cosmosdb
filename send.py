# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 13:44:26 2021

@author: Justin Ho
"""


import time
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
    
    while True:
        try:

            with open('system_status.txt') as json_file:
                system_status= json.load(json_file)


            container.upsert_item({
                    'id': 'system_status',
                    'Inputs': system_status})
            
            time.sleep(5)

        except KeyboardInterrupt:
            break
        except:
            pass
