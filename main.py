import requests

#Функция проверки верности вводимых пользователям валют
def check_input(message: str, currencies: dict)->str:
    while True:
        text = input(message).strip().upper()
        for key in currencies:
            if text == key:
                return text
        print('Вы ввели неверные данные, попробуйте ещё раз')


#Провверка вводимых пользовател данных по количеству валют
def check_float():
    while True:
        amount = input("Введите сумму валюты:")
        if amount.isdigit() == True:
            return amount
    print('Вы ввели не число, попробуйте ещё раз')


#Загрузка справочика валют из aptzar
def get_actual_currencies():
    response = requests.get(URL)
    return response.json().get('data')


#Функция конвертации валют
def converter(amount: float, from_currency: str, to_currency: str, currencies: dict) -> float:
    from_value = currencies.get(from_currency)
    to_value = currencies.get(to_currency)
    coefficient = to_value / from_value
    return round(amount * coefficient, 2)


URL = "https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_JrCb3T3AUE2bUTq850AHulJSraibsTbg0gz3RO3S&currencies="
print("Добро пожаловать в конвертер валют!")
print("""
Инструкция:
1. Ввести исходную валюту
2. Ввести валюту в которую необходимо перевести исходную валюту
3. Ввести количество валюты
""")
#Вывод возможных валют из справочника
print("Доступные валюты:")
CURRENCIES = get_actual_currencies()
for key in CURRENCIES:
    print(f'* {key}')
#Ввод данных
current_currency = check_input('Введите исходную валюту:', CURRENCIES)
result_currency = check_input('Введите искомую валюту: ', CURRENCIES)
amount = check_float()
#Расчёт результата
result = converter(float(amount), current_currency, result_currency, CURRENCIES)
#Вывод результара
print(f'{amount} {current_currency} = {result} {result_currency}')
