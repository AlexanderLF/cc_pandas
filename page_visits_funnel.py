import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

print(visits)
print(cart)
print(checkout)
print(purchase)

visits_cart = pd.merge(visits, cart, how='left')

visits_cart_length = len(visits_cart)

count_no_cart = visits_cart[visits_cart.cart_time.isnull()].user_id.count()

print(count_no_cart)

percent_no_cart = (count_no_cart * 100) / float(visits_cart_length)


checkout_cart = pd.merge(checkout, cart, how='left')
checkout_cart_length = len(checkout_cart)

print(checkout_cart)

count_no_checkout = checkout_cart[checkout_cart.checkout_time.isnull()].user_id.count()

print(count_no_checkout)

percent_no_checkout = (count_no_checkout * 100) / float(checkout_cart_length)



#merge all
all_data = visits.merge(cart, how='left').merge(checkout, how='left').merge(purchase, how='left')

print(all_data.head())

all_data_length = len(all_data)
count_no_purchase = all_data[(all_data.purchase_time.isnull() == True) & (all_data.checkout_time.isnull() == False)].user_id.count()

print(count_no_purchase)

percent_checkout_noPurchase = (count_no_purchase * 100) / float(all_data_length)

print("Funnel Measures")
print(percent_no_cart)
print(percent_no_checkout)
print(percent_checkout_noPurchase)

all_data['time_to_purchase'] = all_data.purchase_time - all_data.visit_time

print('Time to Purchase')
print(all_data.time_to_purchase)
print(all_data.time_to_purchase.mean())

