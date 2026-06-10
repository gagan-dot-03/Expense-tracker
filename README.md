# Expense Tracker Mini-Project

## Project Overview
This is a terminal-based, menu-driven Expense Tracker built in Python. It allows users to log daily expenses and view their spending history. This project was developed as a mini-project submission for the Qubitedge Internship.

## 🚀 Features

* **Menu-Driven Interface:** Entirely operational inside a standard command line interface (CLI).
* **Dedicated Category Selection:** Features a standalone sub-menu for choosing preset categories to eliminate operational typos and formatting errors.
* **Smart Fallbacks:** Automatically defaults to the local system date if the user skips explicit manual date entries.
* **Persistent Local Engine:** Powered by SQLite to keep records secure and intact between runtime restarts without third-party platform dependencies.

---

## 📊 Database Schema

The system initializes a lightweight SQLite database container file (`expense_tracker.db`) containing an `expenses` structured table layout:

| Field Name  | Data Type | Attributes                | Description                                |
| :---        | :---      | :---                      | :---                                       |
| `id`        | INTEGER   | PRIMARY KEY AUTOINCREMENT | Unique sequence flag generated per item.   |
| `date`      | TEXT      | NOT NULL                  | Event timing stamps using `YYYY-MM-DD`.     |
| `category`  | TEXT      | NOT NULL                  | Predetermined group label from sub-menu.   |
| `amount`    | REAL      | NOT NULL                  | Monetary numeric quantity.                  |
| `description`| TEXT     | DEFAULT 'N/A'             | Context details or reference pointers.     |

---

## Setup and Execution Instructions
1. Ensure Python 3.x is installed on your system.
2. Clone this repository to your local machine.
3. Open a terminal and navigate to the project directory.
4. Run the application using the command: `python main.py`
5. Follow the on-screen menu to add or view expenses.
