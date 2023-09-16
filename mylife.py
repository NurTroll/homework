import requests

print("Добро пожаловать в конвертер валют!")
print("""
Инструкция:
1. Ввести исходную валюту
2. Ввести валюту в которую необходимо перевести исходную валюту
3. Ввести количество валюты
""")

URL = "https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_JrCb3T3AUE2bUTq850AHulJSraibsTbg0gz3RO3S&currencies="

#Функция проверки верности вводимых данных
def check_data(string, cur: dict ):
    i = 1
    while i == 1:
        text = input(string).strip().upper()
        for key in cur:
            if text == key:
                return text

        print('Вы ввели неверные данные, попробуйте ещё раз')
#Загрузка справочика волют из apt
def get_actual_currencies():
    response = requests.get(URL)
    return response.json()['data']
#Функция конвертации валют
def converter(amount: float, from_currency: str, to_currency: str, currencies: dict) -> float:
    from_value = currencies.get(from_currency)
    to_value = currencies.get(to_currency)

    coefficient = to_value / from_value
    return round(amount * coefficient, 2)

#Вывод возможных валют из справочника
print("Доступные валюты:")
CURRENCIES = get_actual_currencies()
for key in CURRENCIES:
    print(f'* {key}')
#Ввод данных
current_currency = check_data('Введите исходную валюту:', CURRENCIES)
result_currency = check_data('Введите искомую валюту: ', CURRENCIES)
amount = input("Введите количество валюты: ")
#Расчёт результата
result = converter(float(amount), current_currency, result_currency, CURRENCIES)
#Вывод результара
print(f'{amount} {current_currency} = {result} {result_currency}')
