#Intro to Data Analysis
#Unit 2, Day 5

import codecademylib
import pandas as pd

inventory = pd.read_csv('inventory.csv')
staten_island = inventory.head(10)

product_request = staten_island.product_description

seed_request = inventory[inventory.location == 'Brooklyn']

invlambda = lambda row: True if row['quantity'] > 0 else False

inventory['in_stock'] = inventory.apply(invlambda, axis=1)

vallambda = lambda row: row.price * row.quantity  

inventory['total_value'] = inventory.apply(vallambda, axis=1)

combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description)
  
inventory['full_description'] = inventory.apply(combine_lambda, axis=1)

print(inventory.head(10))

