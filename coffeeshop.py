import requests
import json

def fetch_data(url):
    """
    Fetch JSON data from a given URL.

    Steps to think about:
    - Send an HTTP request to the URL
    - Receive the response
    - Return raw data (usually text or JSON string)
    """
    response = requests.get(url)
    raw_data = response.text
    return raw_data

raw_data = fetch_data('https://raw.githubusercontent.com/ruslanhamidov/coffee_data/main/coffeeshop.json')

def deserialize_data(raw_data):
    """
    Convert raw JSON data into a Python dictionary.

    Steps to think about:
    - Use a JSON library
    - Parse the raw data
    - Return a Python dict
    """
    
    data = json.loads(raw_data)
    return data

data = deserialize_data(raw_data)

def get_data_from_key(data, key):
    """
    Get data for a specific day.

    Steps to think about:
    - Access dictionary using the day key
    - Return that day's data
    """
    day_data = data[key]
    return day_data

day_data = get_data_from_key(data, 'monday')


def get_price(prices, item):
    """
    Get price of a specific item (drink or dessert).

    Steps to think about:
    - Look up item in prices dictionary
    - Return the price
    """
    item_price = prices[item]
    return item_price

item_price = get_price(get_data_from_key(data, 'prices'), 'americano')

def calculate_day(day_data, prices):
    """
    Calculate how much was earned in one day.

    Steps to think about:
    - Get quantities of drinks and desserts
    - Get their prices
    - Multiply quantities by prices
    - Add everything together
    - Include tips
    - Return total for the day
    """
    drinks = get_data_from_key(day_data, 'drinks')
    desserts = get_data_from_key(day_data, 'desserts')
    total_day_amount = 0

    for drink_name, drink_quantity in drinks.items():
        total_day_amount += get_price(prices, drink_name) * drink_quantity

    for dessert_name, dessert_quantity in desserts.items():
        total_day_amount += get_price(prices, dessert_name) * dessert_quantity

    total_day_amount += get_data_from_key(day_data, 'tips')

    return total_day_amount

        
    
total_day_amount = calculate_day(day_data, get_data_from_key(data, 'prices'))

def calculate_week(data, prices):
    """
    Calculate total earnings for the whole week.

    Steps to think about:
    - Loop through each day in the data
    - Call calculate_day for each day
    - Sum all daily totals
    - Return final weekly total
    """
    week_amount = 0

    for day_name in data.keys():
        if day_name == 'prices':
            continue
        
        week_amount += calculate_day(get_data_from_key(data, day_name), prices)
    
    return week_amount

print(calculate_week(data, get_data_from_key(data, 'prices')))