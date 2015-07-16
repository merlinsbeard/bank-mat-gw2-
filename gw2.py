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


def bank_storage():
    # Returns Bank storage in dictionary form
    s = requests.Session()
    s = s.get("https://api.guildwars2.com/v2/account/bank", headers=key_dicts)

    items = s.json()
    print items

    # ID, Name, Count
    bank_dict={}
    bank_dict=[]
    for item in items:
        if item:
            print item['id']
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

api_key = os.environ['GW2_KEY']

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

api_key = "Bearer %s" % (api_key)
account = get_details(api_key)
key_dicts={"Authorization": api_key}
print account['id']
print account['name']

mats = mats()
print mats
