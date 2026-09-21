"""Testy funkcji bazy danych."""

import pytest

import database


@pytest.fixture
def test_database(monkeypatch, tmp_path):
    """Ustawia tymczasową bazę danych na czas jednego testu."""
    database_path = tmp_path / "test_expenses.db"
    monkeypatch.setattr(database, "DATABASE_PATH", database_path)
    database.initialize_database()

    return database_path


def test_add_expense_and_get_expenses(test_database):
    """Dodany wydatek jest dostępny podczas odczytu."""
    database.add_expense(
        amount_cents=1234,
        category="Jedzenie",
        expense_date="2026-08-25",
        description="kawa",
    )

    expenses = database.get_expenses()

    assert len(expenses) == 1
    assert expenses[0]["amount_cents"] == 1234
    assert expenses[0]["category"] == "Jedzenie"
    assert expenses[0]["expense_date"] == "2026-08-25"
    assert expenses[0]["description"] == "kawa"


def test_get_expenses_filters_by_category_and_month(test_database):
    """Filtry kategorii i miesiąca zwracają właściwe wydatki."""
    database.add_expense(
        amount_cents=1000,
        category="Jedzenie",
        expense_date="2026-08-01",
        description="śniadanie",
    )
    database.add_expense(
        amount_cents=2000,
        category="Transport",
        expense_date="2026-08-02",
        description="bilet",
    )
    database.add_expense(
        amount_cents=3000,
        category="Jedzenie",
        expense_date="2026-07-03",
        description="zakupy",
    )

    food_expenses = database.get_expenses(category="Jedzenie")
    august_expenses = database.get_expenses(month="2026-08")
    august_food_expenses = database.get_expenses(
        category="Jedzenie",
        month="2026-08",
    )

    assert len(food_expenses) == 2
    assert len(august_expenses) == 2
    assert len(august_food_expenses) == 1
    assert august_food_expenses[0]["amount_cents"] == 1000


def test_save_budget_updates_existing_budget(test_database):
    """Ponowny zapis budżetu miesiąca aktualizuje jego wartość."""
    database.save_budget("2026-08", 200000)
    database.save_budget("2026-09", 150000)
    database.save_budget("2026-08", 250000)

    assert database.get_budget("2026-08") == 250000
    assert database.get_budget("2026-09") == 150000
    assert database.get_budget("2026-07") is None
    assert database.get_budget_total(month="2026-08") == 250000
    assert database.get_budget_total() == 400000


def test_expenses_totals_and_months_without_budget(test_database):
    """Sumy wydatków i brakujący budżet są obliczane poprawnie."""
    database.add_expense(
        amount_cents=1234,
        category="Jedzenie",
        expense_date="2026-08-10",
        description="zakupy",
    )
    database.add_expense(
        amount_cents=2345,
        category="Inne",
        expense_date="2026-08-11",
        description="książka",
    )
    database.add_expense(
        amount_cents=1500,
        category="Transport",
        expense_date="2026-07-12",
        description="bilet",
    )
    database.save_budget("2026-08", 200000)

    assert database.get_expense_total(month="2026-08") == 3579
    assert database.get_expense_total() == 5079
    assert database.get_budget_total() == 200000
    assert database.get_months_without_budget() == ["2026-07"]


def test_get_category_totals_returns_sums_for_month(test_database):
    """Dane wykresu zawierają sumy kategorii dla wybranego miesiąca."""
    database.add_expense(
        amount_cents=1000,
        category="Jedzenie",
        expense_date="2026-08-01",
        description="śniadanie",
    )
    database.add_expense(
        amount_cents=500,
        category="Jedzenie",
        expense_date="2026-08-02",
        description="kawa",
    )
    database.add_expense(
        amount_cents=2000,
        category="Transport",
        expense_date="2026-08-03",
        description="bilet",
    )
    database.add_expense(
        amount_cents=300,
        category="Jedzenie",
        expense_date="2026-07-04",
        description="zakupy",
    )

    august_totals = database.get_category_totals(month="2026-08")
    empty_totals = database.get_category_totals(month="2026-06")

    assert [
        (row["category"], row["total_cents"])
        for row in august_totals
    ] == [
        ("Transport", 2000),
        ("Jedzenie", 1500),
    ]
    assert empty_totals == []


def test_update_expense_changes_existing_record(test_database):
    """Aktualizacja zmienia rekord i nie tworzy duplikatu."""
    database.add_expense(
        amount_cents=1000,
        category="Jedzenie",
        expense_date="2026-09-01",
        description="stary opis",
    )
    expense_id = database.get_expenses()[0]["id"]

    database.update_expense(
        expense_id=expense_id,
        amount_cents=2500,
        category="Transport",
        expense_date="2026-09-02",
        description="bilet miesięczny",
    )

    expenses = database.get_expenses()
    updated_expense = expenses[0]

    assert len(expenses) == 1
    assert updated_expense["id"] == expense_id
    assert updated_expense["amount_cents"] == 2500
    assert updated_expense["category"] == "Transport"
    assert updated_expense["expense_date"] == "2026-09-02"
    assert updated_expense["description"] == "bilet miesięczny"


def test_delete_expense_removes_only_selected_record(test_database):
    """Usunięcie kasuje tylko wybrany wydatek."""
    database.add_expense(
        amount_cents=1000,
        category="Jedzenie",
        expense_date="2026-09-01",
        description="do usunięcia",
    )
    expense_id = database.get_expenses()[0]["id"]

    database.add_expense(
        amount_cents=2000,
        category="Transport",
        expense_date="2026-09-02",
        description="pozostaje",
    )

    database.delete_expense(expense_id)

    expenses = database.get_expenses()

    assert len(expenses) == 1
    assert expenses[0]["description"] == "pozostaje"
    assert expenses[0]["id"] != expense_id
