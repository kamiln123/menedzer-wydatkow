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


def get_expenses() -> list[sqlite3.Row]:
    """Zwraca wszystkie wydatki od najnowszego do najstarszego."""
    connection = get_connection()

    try:
        cursor = connection.execute(
            """
            SELECT id, amount_cents, category, expense_date, description
            FROM expenses
            ORDER BY expense_date DESC, id DESC
            """
        )
        return cursor.fetchall()
    finally:
        connection.close()
