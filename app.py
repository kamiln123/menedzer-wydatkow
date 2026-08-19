"""Interfejs aplikacji Menedżer wydatków."""
import streamlit as st

st.set_page_config(page_title="Menedżer wydatków", page_icon="💰")

if "expenses" not in st.session_state:
    st.session_state.expenses = []

st.title("💰 Menedżer wydatków")
st.write("Witaj! To moja aplikacja do śledzenia wydatków.")

st.subheader("Dodaj wydatek")

# Streamlit uruchamia skrypt ponownie po każdej interakcji.
# Session state zachowuje wydatki podczas bieżącej sesji w przeglądarce.
with st.form("expense_form"):
    amount = st.number_input(
        "Kwota (zł)",
        min_value = 0.0,
        step = 0.01,
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
        expense = {"amount": amount,
                   "category": category,
                   "date": expense_date,
                   "description": description,
                   }

        st.session_state.expenses.append(expense)
        st.success("Wydatek został dodany.")

st.subheader("Wydatki w tej sesji")


if not st.session_state.expenses:
    st.info("Nie dodano jeszcze żadnych wydatków.")
else:
    for expense in st.session_state.expenses:
        st.write(
            f"{expense['date']:%d.%m.%Y} | "
            f"{expense['category']} | "
            f"{expense['amount']:.2f} zł | "
            f"{expense['description'] or 'Brak opisu'}"
        )