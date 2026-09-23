"""Interfejs aplikacji Menedżer wydatków."""
from datetime import date

import plotly.express as px
import streamlit as st

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
    update_expense,
    delete_expense,
)

CATEGORIES = [
    "Jedzenie",
    "Transport",
    "Rachunki",
    "Rozrywka",
    "Zdrowie",
    "Inne",
]
MAX_DESCRIPTION_LENGTH = 200

st.set_page_config(page_title="Menedżer wydatków", page_icon="💰")

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
    )
    figure.update_layout(
        xaxis_title="Kategoria",
        yaxis_title="Kwota (zł)",
    )

    st.plotly_chart(figure, width="stretch")

st.subheader("Dodaj wydatek")
add_success_message = st.session_state.pop(
    "add_success_message",
    None,
)

if add_success_message:
    st.success(add_success_message)

# Pola formularza są wysyłane razem po kliknięciu przycisku.
with st.form("expense_form", clear_on_submit=True):
    amount = st.number_input(
        "Kwota (zł)",
        min_value=0.0,
        step=0.01,
        format="%.2f",
    )
    category = st.selectbox(
        "Kategoria",
        CATEGORIES,
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
        st.session_state.add_success_message = (
            "Wydatek został dodany."
        )
        st.rerun()

st.subheader("Zapisane wydatki")

expenses = get_expenses(
    category=category_filter,
    month=month_filter,
)

management_success_message = st.session_state.pop(
    "success_message",
    None,
)
if not expenses:
    st.info("Nie dodano jeszcze żadnych wydatków.")

    if management_success_message:
        st.success(management_success_message)

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
    st.subheader("Zarządzaj wydatkiem")

    if management_success_message:
        st.success(management_success_message)

    expense_options = {}

    for expense in expenses:
        option_date = date.fromisoformat(
            expense["expense_date"]
        ).strftime("%d.%m.%Y")

        option_label = (
            f"#{expense['id']} | "
            f"{option_date} | "
            f"{expense['category']} | "
            f"{format_currency(expense['amount_cents'])}"
        )
        expense_options[option_label] = expense

    selected_expense_label = st.selectbox(
        "Wybierz wydatek",
        options=list(expense_options.keys()),
    )
    selected_expense = expense_options[selected_expense_label]
    selected_expense_date = date.fromisoformat(
        selected_expense["expense_date"]
    )
    selected_category_index = CATEGORIES.index(
        selected_expense["category"]
    )

    with st.form(f"edit_expense_form_{selected_expense['id']}"):
        edited_amount = st.number_input(
            "Nowa kwota (zł)",
            min_value=0.0,
            value=selected_expense["amount_cents"] / 100,
            step=0.01,
            format="%.2f",
            key=f"edit_amount_{selected_expense['id']}",
        )
        edited_category = st.selectbox(
            "Nowa kategoria",
            CATEGORIES,
            index=selected_category_index,
            key=f"edit_category_{selected_expense['id']}",
        )
        edited_date = st.date_input(
            "Nowa data",
            value=selected_expense_date,
            key=f"edit_date_{selected_expense['id']}",
        )
        edited_description = st.text_input(
            "Nowy opis (opcjonalnie)",
            value=selected_expense["description"],
            key=f"edit_description_{selected_expense['id']}",
        )
        save_column, delete_column = st.columns(2)

        with save_column:
            edit_submitted = st.form_submit_button(
                "Zapisz zmiany",
                type="primary",
                width="stretch",
            )

        with delete_column:
            delete_requested = st.form_submit_button(
                "Usuń wydatek",
                width="stretch",
            )

    if delete_requested:
        st.session_state.pending_delete_id = selected_expense["id"]

    if edit_submitted:
        st.session_state.pop("pending_delete_id", None)
        cleaned_edited_description = edited_description.strip()

        if edited_amount <= 0:
            st.error("Kwota wydatku musi być większa od zera.")
        elif len(cleaned_edited_description) > MAX_DESCRIPTION_LENGTH:
            st.error(
                f"Opis wydatku może mieć maksymalnie "
                f"{MAX_DESCRIPTION_LENGTH} znaków."
            )
        else:
            update_expense(
                expense_id=selected_expense["id"],
                amount_cents=int(round(edited_amount * 100)),
                category=edited_category,
                expense_date=edited_date.isoformat(),
                description=cleaned_edited_description,
            )
            st.session_state.success_message = (
                "Wydatek został zaktualizowany."
            )
            st.rerun()

    pending_delete_id = st.session_state.get("pending_delete_id")

    if (
        pending_delete_id is not None
        and pending_delete_id != selected_expense["id"]
    ):
        st.session_state.pop("pending_delete_id")
        pending_delete_id = None

    if pending_delete_id == selected_expense["id"]:
        st.warning(
            "Czy na pewno chcesz trwale usunąć wybrany wydatek?"
        )

        confirm_column, cancel_column = st.columns(2)

        with confirm_column:
            confirm_delete_clicked = st.button(
                "Tak, usuń",
                type="primary",
                width="stretch",
                key=f"confirm_delete_{selected_expense['id']}",
            )

        with cancel_column:
            cancel_delete_clicked = st.button(
                "Anuluj",
                width="stretch",
                key=f"cancel_delete_{selected_expense['id']}",
            )

        if confirm_delete_clicked:
            delete_expense(selected_expense["id"])
            st.session_state.pop("pending_delete_id", None)
            st.session_state.success_message = (
                "Wydatek został usunięty."
            )
            st.rerun()
        elif cancel_delete_clicked:
            st.session_state.pop("pending_delete_id", None)
            st.rerun()
