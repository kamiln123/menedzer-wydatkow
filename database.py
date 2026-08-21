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
