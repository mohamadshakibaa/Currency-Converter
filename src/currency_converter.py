import requests


def get_exchange_rate(base_currency, target_currency):
    url = f"https://v6.exchangerate-api.com/v6/fcbf69001983b522b05841fc/latest/{base_currency}"
    response = requests.get(url)
    if response.status_code != 200 :
        return None
    return response.json()['conversion_rates'][target_currency]

def convert_currency(amount, exchahge_rate):
    return amount * exchahge_rate


if __name__ == "__main__":
    base_currency = input("Enter your currency: ")
    target_currency = input("Enter your currency: ")
    amount = float(input("Enter amount: "))
    exchange_rate = get_exchange_rate(base_currency, target_currency)
    converted_amount = convert_currency(amount, exchange_rate)
    print(f'{amount:.3f} {base_currency} is {converted_amount:.3f} {target_currency}')
    