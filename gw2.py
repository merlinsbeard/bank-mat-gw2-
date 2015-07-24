"""
Get the details of Bank and Material Storage
Tells what Gift is missing and how much percentage is left to complete.
"""

# Change to class
# create __init__.py
# Api key uses environment variables
# table for  items

import requests
import os

def get_details(api_key):
    url = "https://api.guildwars2.com/v2/account"
    key_dicts={"Authorization": api_key}
    r = requests.get(url, headers=key_dicts)
    account = r.json()
    return account

#api_key = os.environ['GW2_KEY']

#### Testing ####
#url = "https://api.guildwars2.com/v2/account"
#key_dicts={"Authorization": api_key}
#r = requests.get(url, headers=key_dicts)
#account = r.json()
#print account['id']
#print account['name']
#bank = bank_storage()
#gifts = check_for_gifts(bank)
#print "GIFTS"
#print gifts

def bank_storage():
    # Returns Bank storage in dictionary form
    s = requests.Session()
    s = s.get("https://api.guildwars2.com/v2/account/bank", headers=key_dicts)

    items = s.json()

    # ID, Name, Count
    bank_dict={}
    bank_dict=[]
    for item in items:
        if item:
            #print item['id']
            bank_dict.append(item)

    return bank_dict

def get_item(item_id):
    # Returns the json for specific item using its id
    url = "https://api.guildwars2.com/v2/items/%s" % (item_id)
    r = requests.get(url)
    r = r.json()
    return r	

def mats():
    # Returns all the current materials from material storage
    s = requests.Session()
    s = s.get("https://api.guildwars2.com/v2/account/materials", headers=key_dicts)
    all_mats =  s.json()
    mats_list = []
    for mat in all_mats:
        if mat['count'] > 0:
            mats_list.append({'id': mat['id'],'count': mat['count']})

    return mats_list

def check_for_gifts(items):
    # Under development
    list_of_gifts = [{19674: [20797, 19677, 19678]}]
    current_gifts = []
    for item in items:
        if item['id'] in list_of_gifts:
            current_gifts.append(item)

    return current_gifts

def check_for_main_gifts(items):
	pass


items_to_look = [24315, 24325,]

def check_for_specific_items(items,items_to_look):
    has_items=[]
    for item in items:
        if item['id'] in items_to_look:
            has_items.append(item)
    return has_items


def get_tp_info(item_id):
    # Returns the json for specific item using its id
    url = "https://api.guildwars2.com/v2/commerce/prices/%s" % (item_id)
    r = requests.get(url)
    r = r.json()
    return r	
	
def get_current_transactions(api_key, current):
    url = "https://api.guildwars2.com/v2/commerce/transactions/current/%s" % (current)
    key_dicts={"Authorization": api_key}
    r = requests.get(url, headers=key_dicts)
    #trans= r.json()
    trans= r.json()
    return trans


api = os.environ['API_KEY']
api_key = "Bearer %s" % (api)
account = get_details(api_key)
key_dicts={"Authorization": api_key}
print account['id']
print account['name']
current_buys = get_current_transactions(api_key, 'buys')

for buy in current_buys:
    i = get_item(buy['item_id'])
    print i['name'], buy['price'], buy['quantity']

mats = mats()
c = check_for_specific_items(mats, items_to_look)

total_cost_buy = 0
total_cost_sell = 0
for item in c:
    i = get_item(item['id'])
    print i['name']
    item_left = 100 - item['count']  
    print item_left, "left"
    tp = get_tp_info(item['id'])
    buy_ea = tp["buys"]["unit_price"]
    buy_total = buy_ea * item_left
    total_cost_buy += buy_total
    print "Buying:", buy_ea,  "each"
    print "Total Cost:",buy_total 
    # Sells
    sell_ea = tp["sells"]["unit_price"]
    sell_total = sell_ea * item_left
    total_cost_sell += sell_total
    print "Selling:",sell_ea, "each"
    print "Total Cost:", sell_total 
    print "######################"

# check for spark in bank
items = bank_storage()
c = check_for_specific_items(items, [29167])
if not c:
    item_id = 29167
    i = get_item(item_id)
    print i['name']
    tp = get_tp_info(item_id)
    buy_ea = tp["buys"]["unit_price"]
    buy_total = buy_ea
    total_cost_buy += buy_total
    print "Buying:", buy_ea,  "each"
    print "Total Cost:",buy_total 
    # Sells
    sell_ea = tp["sells"]["unit_price"]
    sell_total = sell_ea
    total_cost_sell += sell_total
    print "Selling:",sell_ea, "each"
    print "Total Cost:", sell_total 
    print "######################"

print "Total Cost Buy:", total_cost_buy
print "Total Cost Sell:", total_cost_sell


