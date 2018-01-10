import codecademylib
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')

most_views = ad_clicks.groupby('utm_source').user_id.count().reset_index()

ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()

clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()

clicks_pivot = clicks_by_source\
		.pivot(index='utm_source',
           columns='is_click',
           values='user_id').reset_index()
  
clicks_pivot['percent_clicked'] = clicks_pivot[True] / \
		(clicks_pivot[True] + clicks_pivot[False]) * 100
  
experimental_group_count = ad_clicks.groupby('experimental_group').user_id.count().reset_index()

exp_group_ad = ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index()

exp_group_ad_pivot = exp_group_ad\
		.pivot(index='experimental_group',
           columns='is_click',
           values='user_id').reset_index()
  
exp_group_ad_pivot['percent_clicked'] = exp_group_ad_pivot[True] / \
		(exp_group_ad_pivot[True] + exp_group_ad_pivot[False]) * 100
  
a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']

b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']

a_clicks_count = a_clicks.groupby(['is_click', 'day']).user_id.count().reset_index()

a_clicks_pivot = a_clicks_count\
		.pivot(index='day',
           columns='is_click',
           values='user_id').reset_index()
  
a_clicks_pivot['percent_clicked'] = a_clicks_pivot[True] / \
		(a_clicks_pivot[True] + a_clicks_pivot[False]) * 100
  
#start b_clicks

b_clicks_count = b_clicks.groupby(['is_click', 'day']).user_id.count().reset_index()

b_clicks_pivot = b_clicks_count\
		.pivot(index='day',
           columns='is_click',
           values='user_id').reset_index()
  
b_clicks_pivot['percent_clicked'] = b_clicks_pivot[True] / \
		(b_clicks_pivot[True] + b_clicks_pivot[False]) * 100



print(ad_clicks.head())

print(most_views)

print(clicks_by_source)

print(clicks_pivot)

print(experimental_group_count)

print(exp_group_ad)

print(exp_group_ad_pivot)

print(a_clicks_pivot)

print(b_clicks_pivot)
