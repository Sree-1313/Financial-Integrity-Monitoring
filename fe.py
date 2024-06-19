import streamlit as st

acc_no = st.text_input("Account number", max_chars=24)
print(acc_no)

tran_date = st.text_input("Transaction date",max_chars=10)
print(tran_date)

tran_dat = st.text_input("Transaction detail", max_chars=15)
print(tran_dat)

check_no=st.number_input("Check no:")
if check_no == "":
    st.write(check_no, 'Enter the number in integer')
elif isinstance(check_no, int):
    st.write(check_no, '...works as it is an integer')


val_date = st.text_input("Value date", value=tran_date)

amount_draw = st.number_input("Amount for withdraw")
print(amount_draw)

if amount_draw == "":
    st.write(amount_draw, 'Enter the number in integer')
elif isinstance(amount_draw, int):
    st.write(amount_draw)

amount_dep = st.number_input("Amount for Deposit")
print(amount_dep)

if amount_dep == "":
    st.write(amount_dep, 'Enter the number in integer')
elif isinstance(amount_dep, int):
    st.write(amount_dep)

st.button("Submit")