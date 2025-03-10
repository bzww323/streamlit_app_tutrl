import streamlit as st
import requests

# динамически берем курс валюты 1 раз в сутки
@st.cache_data(ttl=1)
def get_rates():
    url = "https://open.er-api.com/v6/latest/RUB"
    inverse_rates = requests.get(url).json()["rates"]
    return {x: 1 / y for x, y in inverse_rates.items()}

st.title("Конвертер валют")
st.write("Переведем рубли в нужную валюту")
col1, col2 = st.columns(2)
x = col1.number_input("", min_value=0.0, value=1.0, step=1.0)
st.write(x)
rates = get_rates()
# исключаем перевод из рублей в рубли
if "RUB" in rates:
    del rates["RUB"]
# cоздаем список валют с приоритетом для USD и EUR
priority_currencies = ["USD", "EUR"]
other_currencies = sorted([x for x in rates.keys() if x not in priority_currencies])
currencies = priority_currencies + other_currencies
currency = col2.selectbox("Валюта", list(currencies))
st.success(f"{x * rates[currency]:,.2f} RUB")  # :,.2f - разделитель между цифрами - запятая, берем их до 2 цифр после запятой
