import streamlit as st
import requests
# st.title("С праздником тебя, Сергун-Дудко!")
# st.write("с твоим днем! с 8 марта! гы! гыы! гыыыыы!")

# st.title("Конвертер валют")
# x = st.number_input("USD", min_value=0.0, value=1.0, step=1.0)
# st.write(x)
# rate = 88.67
# # st.write(f'{x * rate:,.2f}') # :,.2f - разделитель между цифрами - запятая, берем их до 2 цифр после запятой
# # st.write(f'{x * rate:,.2f}') # :,.2f - разделитель между цифрами - запятая, берем их до 2 цифр после запятой
# st.success(f'{x * rate:,.2f}') # :,.2f - разделитель между цифрами - запятая, берем их до 2 цифр после запятой

# динамически берем курс валюты 1 раз в сутки
@st.cache_data(ttl="1 day")
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
currency = col2.selectbox("Валюта", list(rates))
# st.write(f'{x * rate:,.2f}') # :,.2f - разделитель между цифрами - запятая, берем их до 2 цифр после запятой
# st.write(f'{x * rate:,.2f}') # :,.2f - разделитель между цифрами - запятая, берем их до 2 цифр после запятой
st.success(f"{x * rates[currency]:,.2f} RUB")  # :,.2f - разделитель между цифрами - запятая, берем их до 2 цифр после запятой
