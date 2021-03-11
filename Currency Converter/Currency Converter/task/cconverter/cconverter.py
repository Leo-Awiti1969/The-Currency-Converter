import requests

cache = {}
my_currency_code = input()
while True:
    new_currency_code = input()
    if len(new_currency_code) == 0:
        break
    elif len(new_currency_code) != 0:
        my_currency_amount = float(input())
        r = requests.get(f'http://www.floatrates.com/daily/{my_currency_code}.json')
        try:
            cache['eur'] = r.json()['eur'].get("rate")
            cache['usd'] = r.json()['usd'].get("rate")
        except KeyError:
            pass
        print('Checking the cache...')
        if new_currency_code in cache:
            print('Oh! It is in the cache!')
            keys = list(cache.keys())
            vals = list(cache.values())
            rate = vals[keys.index(new_currency_code)]
            new_currency_amount = round((rate * my_currency_amount), 2)
        else:
            print('Sorry, but it is not in the cache!')
            r = requests.get(f'http://www.floatrates.com/daily/{my_currency_code}.json')
            cache[new_currency_code] = r.json()[new_currency_code].get("rate")
            new_currency_amount = round((r.json()[new_currency_code].get('rate') * my_currency_amount), 2)
        print(f'You received {new_currency_amount} {new_currency_code}.')
