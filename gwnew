import requests

class account:

	def __init__(self, api_key):
		self.api_key = "Bearer %s" % (api_key)


	def account_details(self):
	    url = "https://api.guildwars2.com/v2/account"
	    key_dicts={"Authorization": self.api_key}
	    r = requests.get(url, headers=key_dicts)
	    account = r.json()
	    return account

	def trade_current_buys(self):
		url = "https://api.guildwars2.com/v2/commerce/transactions/current/buys"
		key_dicts={"Authorization": self.api_key}
		r = requests.get(url, headers=key_dicts)
		trade = r.json()
		return trade

	def trade_current_sells(self):
		url = "https://api.guildwars2.com/v2/commerce/transactions/current/sells"
		key_dicts={"Authorization": self.api_key}
		r = requests.get(url, headers=key_dicts)
		trade = r.json()
		return trade

	def trade_history_buys(self):
		url = "https://api.guildwars2.com/v2/commerce/transactions/history/buys"
		key_dicts={"Authorization": self.api_key}
		r = requests.get(url, headers=key_dicts)
		trade = r.json()
		return trade

	def trade_history_sells(self):
		url = "https://api.guildwars2.com/v2/commerce/transactions/history/sells"
		key_dicts={"Authorization": self.api_key}
		r = requests.get(url, headers=key_dicts)
		trade = r.json()
		return trade
	
def item_detail(item_id):
	url = "https://api.guildwars2.com/v2/items/%s" % (item_id)
	item = requests.get(url)
	item = item.json()
	return item

def print_item_name_price_quantity(item_list):
	count = 0
	for item in item_list:
		count += 1
		i = item_detail(item['item_id'])
		print count, i['name'], item['price'], item['quantity'], item['purchased']

	
#api_key = "3EA0E286-5898-204E-81E3-EEBB65B43EAF6B2F53BC-0854-4FB6-8951-D58229DA2340"

#bj = account(api_key)

#print bj.account_details()
#print "############# Buys ###########"
#print_item_name_price_quantity(bj.trade_current_buys())
#print "############# Sells ###########"
#print_item_name_price_quantity(bj.trade_current_sells())


#print "############# Buys history ###########"
#print_item_name_price_quantity(bj.trade_history_buys())
#print "############# Sells ###########"
#print_item_name_price_quantity(bj.trade_history_sells())
#for item in bj.trade_current_buys():
#	i = item_detail(item['item_id'])
#	print i['name'], item['price'], item['quantity']

