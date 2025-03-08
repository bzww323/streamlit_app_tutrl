import streamlit as st

# st.title("С праздником тебя, Сергун-Дудко!")
# st.write("с твоим днем! с 8 марта! гы! гыы! гыыыыы!")

# st.title("Конвертер валют")
# x = st.number_input("USD", min_value=0.0, value=1.0, step=1.0)
# st.write(x)
# rate = 88.67
# # st.write(f'{x * rate:,.2f}') # :,.2f - разделитель между цифрами - запятая, берем их до 2 цифр после запятой
# # st.write(f'{x * rate:,.2f}') # :,.2f - разделитель между цифрами - запятая, берем их до 2 цифр после запятой
# st.success(f'{x * rate:,.2f}') # :,.2f - разделитель между цифрами - запятая, берем их до 2 цифр после запятой

st.title("Конвертер валют")
col1, col2 = st.columns(2)
x = col1.number_input("", min_value=0.0, value=1.0, step=1.0)
st.write(x)
rates = {"USD": 88.67, "KZT": 0.18}
currency = col2.selectbox("Валюта", list(rates))
# st.write(f'{x * rate:,.2f}') # :,.2f - разделитель между цифрами - запятая, берем их до 2 цифр после запятой
# st.write(f'{x * rate:,.2f}') # :,.2f - разделитель между цифрами - запятая, берем их до 2 цифр после запятой
st.success(f'{x * rates[currency]:,.2f}')  # :,.2f - разделитель между цифрами - запятая, берем их до 2 цифр после запятой
