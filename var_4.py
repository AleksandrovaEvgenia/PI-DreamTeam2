import streamlit as st


def name_cena(data, cena): #  Основной код
    n = []
    for line in data:
        if line.split(",")[0] == "PassengerId":
            continue
        if float(line.split(",")[10]) > float(cena):
            n += [line.split(",")[3] + line.split(",")[4]]
    return n


def var4(data): # Вариант 4
    st.header('Вариант 4. Выполнила Беляева М.М., группа 3-см')
    st.subheader("Задание:")
    st.info("Вывести имена пассажиров, стоимость билета которых была выше указанной")
    st.subheader("Результат:")
    cena = st.text_input("Введите стоимость билета", 10000)
    st.table(name_cena(data, cena))
