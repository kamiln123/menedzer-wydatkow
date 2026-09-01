"""Funkcje komunikujące aplikację z lokalną bazą SQLite."""

import sqlite3
from pathlib import Path

DATABASE_PATH = Path("data") / "expenses.db"


def get_connection() -> sqlite3.Connection:
    """Zwraca połączenie z lokalną bazą i tworzy folder danych, jeśli potrzeba."""
    DATABASE_PATH.parent.mkdir(exist_ok=True)
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database() -> None:
    """Tworzy tabelę wydatków, jeżeli jeszcze nie istnieje."""
    connection = get_connection()

    try:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                amount_cents INTEGER NOT NULL CHECK (amount_cents > 0),
                category TEXT NOT NULL,
                expense_date TEXT NOT NULL,
                description TEXT NOT NULL DEFAULT ''
            )
            """
        )
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS budgets (
                month TEXT PRIMARY KEY,
                limit_cents INTEGER NOT NULL CHECK (limit_cents > 0)
            )
            """
        )
        connection.commit()
    finally:
        connection.close()


def add_expense(
    amount_cents: int,
    category: str,
    expense_date: str,
    description: str,
) -> None:
    """Zapisuje jeden wydatek w lokalnej bazie danych."""
    connection = get_connection()

    try:
        connection.execute(
            """
            INSERT INTO expenses(amount_cents, category, expense_date, description)
            VALUES (?, ?, ?, ?)
            """,
            (amount_cents, category, expense_date, description),
        )
        connection.commit()
    finally:
        connection.close()


def get_expenses(
    category: str | None = None,
    month: str | None = None,
) -> list[sqlite3.Row]:
    """Zwraca wydatki opcjonalnie ograniczone kategorią i miesiącem."""
    connection = get_connection()

    try:
        query = """
            SELECT id, amount_cents, category, expense_date, description
            FROM expenses
        """
        conditions: list[str] = []
        parameters: list[str] = []

        if category is not None:
            conditions.append("category = ?")
            parameters.append(category)

        if month is not None:
            conditions.append("substr(expense_date, 1, 7) = ?")
            parameters.append(month)

        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        query += " ORDER BY expense_date DESC, id DESC"

        cursor = connection.execute(query, parameters)
        return cursor.fetchall()
    finally:
        connection.close()


def get_categories() -> list[str]:
    """Zwraca alfabetyczną listę kategorii zapisanych w bazie."""
    connection = get_connection()

    try:
        cursor = connection.execute(
            """
            SELECT DISTINCT category
            FROM expenses
            ORDER BY category ASC
            """
        )
        return [row["category"] for row in cursor.fetchall()]
    finally:
        connection.close()


def get_months() -> list[str]:
    """Zwraca miesiące z wydatkami w formacie RRRR-MM."""
    connection = get_connection()

    try:
        cursor = connection.execute(
            """
            SELECT DISTINCT substr(expense_date, 1, 7) AS month
            FROM expenses
            ORDER BY month DESC
            """
        )
        return [row["month"] for row in cursor.fetchall()]
    finally:
        connection.close()


def save_budget(month: str, limit_cents: int) -> None:
    """Zapisuje lub aktualizuje budżet dla wybranego miesiąca."""
    connection = get_connection()

    try:
        connection.execute(
            """
            INSERT INTO budgets (month, limit_cents)
            VALUES (?, ?)
            ON CONFLICT(month) DO UPDATE SET
                limit_cents = excluded.limit_cents
            """,
            (month, limit_cents),
        )
        connection.commit()
    finally:
        connection.close()


def get_budget(month: str) -> int | None:
    """Zwraca budżet miesiąca w groszach albo None, jeśli go nie ustawiono."""
    connection = get_connection()

    try:
        cursor = connection.execute(
            """
            SELECT limit_cents
            FROM budgets
            WHERE month = ?
            """,
            (month,),
        )
        row = cursor.fetchone()

        return None if row is None else row["limit_cents"]
    finally:
        connection.close()


def get_expense_total(month: str | None = None) -> int:
    """Zwraca sumę wydatków w groszach, opcjonalnie dla jednego miesiąca."""
    connection = get_connection()

    try:
        query = "SELECT COALESCE(SUM(amount_cents), 0) AS total_cents FROM expenses"
        parameters: list[str] = []

        if month is not None:
            query += " WHERE substr(expense_date, 1, 7) = ?"
            parameters.append(month)

        cursor = connection.execute(query, parameters)
        row = cursor.fetchone()

        return row["total_cents"]
    finally:
        connection.close()


def get_budget_total(month: str | None = None) -> int:
    """Zwraca sumę budżetów w groszach."""
    connection = get_connection()

    try:
        query = "SELECT COALESCE(SUM(limit_cents), 0) AS total_cents FROM budgets"
        parameters: list[str] = []

        if month is not None:
            query += " WHERE month = ?"
            parameters.append(month)

        cursor = connection.execute(query, parameters)
        row = cursor.fetchone()

        return row["total_cents"]
    finally:
        connection.close()


def get_months_without_budget() -> list[str]:
    """Zwraca miesiące z wydatkami, dla których nie ustawiono budżetu."""
    connection = get_connection()

    try:
        cursor = connection.execute(
            """
            SELECT DISTINCT substr(expense.expense_date, 1, 7) AS month
            FROM expenses AS expense
            LEFT JOIN budgets AS budget
                ON substr(expense.expense_date, 1, 7) = budget.month
            WHERE budget.month IS NULL
            ORDER BY month DESC
            """
        )
        return [row["month"] for row in cursor.fetchall()]
    finally:
        connection.close()


def get_category_totals(month: str | None = None) -> list[sqlite3.Row]:
    """Zwraca sumy wydatków w groszach dla poszczególnych kategorii."""
    connection = get_connection()

    try:
        query = """
            SELECT category, SUM(amount_cents) AS total_cents
            FROM expenses
        """
        parameters: list[str] = []

        if month is not None:
            query += " WHERE substr(expense_date, 1, 7) = ?"
            parameters.append(month)

        query += " GROUP BY category ORDER BY total_cents DESC, category ASC"

        cursor = connection.execute(query, parameters)
        return cursor.fetchall()
    finally:
        connection.close()
