from requests import get, utils
from decimal import Decimal



def currency_rates(cash):
    cash = cash.upper()
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    date = response.headers['Set-cookie'].split(',')[-1]

    response = response.text


    if cash not in response:
        print("Oops! We didn't find the same valute :(")


    result = response[response.find('<Value>',
                      response.find(cash))+7:response.find('</Value>',
                      response.find(cash))].split(',')

    result = Decimal('.'.join(result))

    print(f'{date}\n{cash} = {result}')

cash = input('Enter valute char-code')
currency_rates(cash)