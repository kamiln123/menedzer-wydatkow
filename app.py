"""Interfejs aplikacji Menedżer wydatków."""
from datetime import date

import streamlit as st

from database import add_expense, get_expenses, initialize_database


st.set_page_config(page_title="Menedżer wydatków", page_icon="💰")
initialize_database()

st.title("💰 Menedżer wydatków")
st.write("Witaj! To moja aplikacja do śledzenia wydatków.")

st.subheader("Dodaj wydatek")

# Pola formularza są wysyłane razem po kliknięciu przycisku.
with st.form("expense_form"):
    amount = st.number_input(
        "Kwota (zł)",
        min_value=0.0,
        step=0.01,
        format="%.2f",
    )
    category = st.selectbox(
        "Kategoria",
         ["Jedzenie", "Transport", "Rachunki", "Rozrywka", "Zdrowie", "Inne"],
    )
    expense_date = st.date_input("Data")
    description = st.text_input("Opis (opcjonalnie)")
    submitted = st.form_submit_button("Dodaj wydatek")

# Pola formularza są wysyłane razem po kliknięciu przycisku.
if submitted:
    if amount <= 0:
        st.error("Kwota wydatku musi być większa od zera.")
    else:
        amount_cents = int(round(amount * 100))

        add_expense(
            amount_cents=amount_cents,
            category=category,
            expense_date=expense_date.isoformat(),
            description=description,
        )
        st.success("Wydatek został dodany.")

st.subheader("Zapisane wydatki")

expenses = get_expenses()

if not expenses:
    st.info("Nie dodano jeszcze żadnych wydatków.")
else:
    for expense in expenses:
        formatted_date = date.fromisoformat(
            expense["expense_date"]
        ).strftime("%d.%m.%Y")
        amount_pln = expense["amount_cents"] / 100

        st.write(
            f"{formatted_date} | "
            f"{expense['category']} | "
            f"{amount_pln:.2f} zł | "
            f"{expense['description'] or 'Brak opisu'}"
        )
