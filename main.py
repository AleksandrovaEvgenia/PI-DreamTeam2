import streamlit as st
import Var_1
import Var_4
import Var_5_2
import Var_11
import var_10
with open("data.csv") as file:
    data = file.readlines()
st.title('Веб-приложение "ТИТАНИК" (разработка PI-DreamTeam2)')
option = st.selectbox('Выберите исполнителя',
    ('Григорьева К.В.', 'Александрова Е.В', 'Кузнецов Н.В.', 'Беляева М.М.', 'Бессонова А.А.'))
if option == 'Григорьева К.В.':
   var_11.run_result()
if option == 'Александрова Е.В':
    Var_1.var1()
if option == 'Кузнецов Н.В.':
    var_10.var10(data)    
if option == 'Беляева М.М.':
    Var_4.var4() 
if option == 'Бессонова А.А.':
    Var_5_2.var5_2()   
