import sqlite3
import sys
from datetime import datetime

def init_db():
    """Initializes the database and creates the expenses table if it doesn't exist."""
    conn = sqlite3.connect('expense_tracker.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            description TEXT
        )
    ''')
    conn.commit()
    conn.close()

def select_category():
    """Displays a dedicated sub-menu for choosing an expense category."""
    categories = {
        "1": "Food & Dining",
        "2": "Transportation/Travel",
        "3": "Bills & Utilities",
        "4": "Entertainment & Leisure",
        "5": "Shopping",
        "6": "Healthcare",
        "7": "Other"
    }
    
    while True:
        print("\n--- Select Expense Category ---")
        for key, value in categories.items():
            print(f"{key}. {value}")
        
        choice = input("Select a category number (1-7): ").strip()
        if choice in categories:
            return categories[choice]
        else:
            print("Invalid choice. Please select a valid number between 1 and 7.")

def add_expense():
    """Prompts the user to add a new expense record with a structural category selection."""
    print("\n--- Add New Expense ---")
    
    # 1. Date Input
    date = input("Enter date (YYYY-MM-DD) [Press Enter for today]: ").strip()
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")
    
    # 2. Category Selection via Sub-Menu
    category = select_category()
    
    # 3. Amount Input
    try:
        amount = float(input("Enter amount ($): "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
    except ValueError:
        print("Invalid amount. Please enter a valid numerical value.")
        return

    # 4. Description Input
    description = input("Enter a brief description: ").strip()
    if not description:
        description = "N/A"

    # Save to Database
    conn = sqlite3.connect('expense_tracker.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO expenses (date, category, amount, description)
        VALUES (?, ?, ?, ?)
    ''', (date, category, amount, description))
    conn.commit()
    conn.close()
    
    print(f"\nSuccess: Added ${amount:.2f} under '{category}'!")

def view_expenses():
    """Retrieves and displays all expenses from the database."""
    print("\n--- Expense History Records ---")
    conn = sqlite3.connect('expense_tracker.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM expenses ORDER BY date DESC')
    records = cursor.fetchall()
    conn.close()

    if not records:
        print("No expenses recorded yet.")
        return

    # Structured Table Formatting
    print(f"{'ID':<5} | {'Date':<12} | {'Category':<25} | {'Amount':<10} | {'Description'}")
    print("-" * 80)
    
    for row in records:
        print(f"{row[0]:<5} | {row[1]:<12} | {row[2]:<25} | ${row[3]:<9.2f} | {row[4]}")

def main_menu():
    """Displays the primary terminal menu."""
    init_db()
    while True:
        print("\n===== EXPENSE TRACKER SYSTEM =====")
        print("1. Add New Expense Record")
        print("2. View Spending History")
        print("3. Safe Exit")
        
        choice = input("Enter option (1-3): ").strip()
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            print("\nExiting application safely. Data saved successfully.")
            sys.exit()
        else:
            print("Invalid input. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main_menu()