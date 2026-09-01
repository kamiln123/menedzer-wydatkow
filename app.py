"""Interfejs aplikacji Menedżer wydatków."""
from datetime import date

import streamlit as st

import plotly.express as px

from database import (
    add_expense,
    get_categories,
    get_expenses,
    get_months,
    initialize_database,
    get_budget,
    save_budget,
    get_budget_total,
    get_expense_total,
    get_months_without_budget,
    get_category_totals,
)


st.set_page_config(page_title="Menedżer wydatków", page_icon="💰")
MAX_DESCRIPTION_LENGTH = 200

initialize_database()


def format_currency(amount_cents: int) -> str:
    """Formatuje kwotę w groszach jako złotówki."""
    return f"{amount_cents / 100:.2f} zł"


st.sidebar.header("Filtry")

category_options = ["Wszystkie"] + get_categories()
selected_category = st.sidebar.selectbox(
    "Kategoria",
    category_options,
)

month_options = ["Wszystkie"] + get_months()
selected_month = st.sidebar.selectbox(
    "Miesiąc",
    month_options,
)

category_filter = None if selected_category == "Wszystkie" else selected_category

month_filter = None if selected_month == "Wszystkie" else selected_month

st.sidebar.divider()
st.sidebar.subheader("Miesięczny budżet")

if month_filter is None:
    st.sidebar.info("Wybierz konkretny miesiąc, aby ustawić budżet.")
else:
    saved_budget = get_budget(month_filter)
    default_budget = (
        0.0 if saved_budget is None else saved_budget / 100
    )

    with st.sidebar.form("budget_form"):
        budget_amount = st.number_input(
            "Budżet (zł)",
            min_value=0.0,
            value=default_budget,
            step=0.01,
            format="%.2f",
            key=f"budget_{month_filter}",
        )
        budget_submitted = st.form_submit_button("Zapisz budżet")

    if budget_submitted:
        if budget_amount <= 0:
            st.sidebar.error("Budżet musi być większy od zera.")
        else:
            budget_cents = int(round(budget_amount * 100))
            save_budget(month_filter, budget_cents)
            st.sidebar.success("Budżet został zapisany.")

st.title("💰 Menedżer wydatków")
st.write("Witaj! To moja aplikacja do śledzenia wydatków.")

st.subheader("Podsumowanie budżetu")

if month_filter is None:
    st.caption("Podsumowanie dla wszystkich zapisanych miesięcy.")
else:
    st.caption(f"Podsumowanie dla miesiąca: {month_filter}.")

expense_total_cents = get_expense_total(month=month_filter)
budget_total_cents = get_budget_total(month=month_filter)
remaining_cents = budget_total_cents - expense_total_cents

expense_column, budget_column, remaining_column = st.columns(3)

expense_column.metric(
    "Wydano",
    format_currency(expense_total_cents),
)
budget_column.metric(
    "Budżet",
    format_currency(budget_total_cents),
)
remaining_column.metric(
    "Pozostało",
    format_currency(remaining_cents),
)

if month_filter is None:
    months_without_budget = get_months_without_budget()

    if months_without_budget:
        st.warning(
            "Brak budżetu dla miesięcy: "
            + ", ".join(months_without_budget)
            + ". Są liczone jako 0 zł."
        )
elif budget_total_cents == 0:
    st.warning("Dla wybranego miesiąca nie ustawiono budżetu.")

if remaining_cents < 0:
    st.error(
        "Budżet został przekroczony o "
        + format_currency(abs(remaining_cents))
        + "."
    )

st.subheader("Wydatki według kategorii")

category_totals = get_category_totals(month=month_filter)

if not category_totals:
    st.info("Brak danych do pokazania na wykresie.")
else:
    chart_rows = [
        {
            "Kategoria": row["category"],
            "Kwota (zł)": row["total_cents"] / 100,
        }
        for row in category_totals
    ]

    figure = px.bar(
        chart_rows,
        x="Kategoria",
        y="Kwota (zł)",
        text_auto=".2f",
        title="Wydatki według kategorii",
    )
    figure.update_layout(
        xaxis_title="Kategoria",
        yaxis_title="Kwota (zł)",
    )

    st.plotly_chart(figure, width="stretch")

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

if submitted:
    cleaned_description = description.strip()

    if amount <= 0:
        st.error("Kwota wydatku musi być większa od zera.")
    elif len(cleaned_description) > MAX_DESCRIPTION_LENGTH:
        st.error(
            f"Opis wydatku może mieć maksymalnie "
            f"{MAX_DESCRIPTION_LENGTH} znaków."
        )
    else:
        amount_cents = int(round(amount * 100))

        add_expense(
            amount_cents=amount_cents,
            category=category,
            expense_date=expense_date.isoformat(),
            description=cleaned_description,
        )
        st.success("Wydatek został dodany.")

st.subheader("Zapisane wydatki")

expenses = get_expenses(
    category=category_filter,
    month=month_filter,
)

if not expenses:
    st.info("Nie dodano jeszcze żadnych wydatków.")
else:
    table_rows = []

    for expense in expenses:
        formatted_date = date.fromisoformat(
            expense["expense_date"]
        ).strftime("%d.%m.%Y")

        table_rows.append(
            {
                "Data": formatted_date,
                "Kategoria": expense["category"],
                "Opis": expense["description"] or "Brak opisu",
                "Kwota": format_currency(expense["amount_cents"]),
            }
        )

    st.dataframe(table_rows, hide_index=True)
    st.caption(f"Widoczne wydatki: {len(expenses)}")
