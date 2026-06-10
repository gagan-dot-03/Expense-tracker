# Expense Tracker Mini-Project

## Project Overview
This is a terminal-based, menu-driven Expense Tracker built in Python. It allows users to log daily expenses and view their spending history. This project was developed as a mini-project submission for the Qubitedge Internship.

# Relational Personal Expense Tracker (with Dynamic Budget Analysis)

An advanced, terminal-based menu-driven Python application constructed to log, categorize, monitor, and analyze financial transactions. Powered by an SQLite relational database engine, this application operates natively in Indian Rupees (Rs.) and offers real-time budget forecasting alongside financial report exporting capabilities.

---

## Key Features

* **Multi-User Management:** Supports localized user registration and individual profile logins with custom financial threshold targets.
* **Three-Table Relational Schema:** Implements professional data normalization patterns, securing entity relationships via explicit Foreign Keys.
* **Dynamic Before/After Budget Analysis:** Calculates and displays active monthly spending balances *before* an expense entry is added and predicts the remaining balance *after* deduction, triggering system warnings if limits are breached.
* **Advanced SQL Analytics Engine:** Runs complex grouping query logic utilizing relational table joins and SQL aggregate functions (`SUM()`, `AVG()`, and `GROUP BY`).
* **Multi-Criteria Data Filtering:** Allows instantaneous operational history retrieval indexed by custom category tags or precise date-range intervals (`YYYY-MM-DD`).
* **Data Portability Processing:** Compiles personalized financial tables into cross-platform standalone `.csv` spreadsheet files automatically.

---

## 📊 Database Schema Architecture

The localized engine manages data inside an isolated repository container (`expense_tracker.db`) mapped out across three interconnected relational tables:

### 1. `users` Table
Handles user profile initialization and specific budget configurations.
| Field Name       | Data Type | Attributes                | Description                                     |
| :---             | :---      | :---                      | :---                                            |
| `id`             | INTEGER   | PRIMARY KEY AUTOINCREMENT | Unique identifier sequence for each user account.|
| `username`       | TEXT      | UNIQUE NOT NULL           | Alpha-numeric login moniker identifier.         |
| `monthly_budget` | REAL      | DEFAULT 0.0               | Active financial cap ceiling limit (Rs.).       |

### 2. `categories` Table
Stores preset transaction groupings to keep indices uniform.
| Field Name | Data Type | Attributes                | Description                                       |
| :---       | :---      | :---                      | :---                                              |
| `id`       | INTEGER   | PRIMARY KEY AUTOINCREMENT | Unique category relationship row pointer key.     |
| `name`     | TEXT      | UNIQUE NOT NULL           | Label descriptors (`Food`, `Transport`, etc.).    |

### 3. `expenses` Table
Tracks operational transaction entries bound to specified users and categories.
| Field Name    | Data Type | Attributes                | Description                                       |
| :---          | :---      | :---                      | :---                                              |
| `id`          | INTEGER   | PRIMARY KEY AUTOINCREMENT | Unique operational reference ledger log token.    |
| `user_id`     | INTEGER   | FOREIGN KEY NOT NULL      | References `id` inside the `users` table.         |
| `category_id` | INTEGER   | FOREIGN KEY NOT NULL      | References `id` inside the `categories` table.    |
| `amount`      | REAL      | NOT NULL                  | Transaction monetary metric numeric size (Rs.).   |
| `date`        | TEXT      | NOT NULL                  | Standardized ISO timestamp entry (`YYYY-MM-DD`).   |
| `description` | TEXT      | DEFAULT 'N/A'             | Context reference notations or brief memos.       |

---

## Installation & Local Execution Protocols

### System Requirements
* Windows 10 / 11 Operating System.
* Python 3.x runtime package installation (configured via a local Python environment setup or Anaconda distribution terminal console).

### Execution Steps
1. Download or clone this workspace folder containing `main.py` onto your local storage system.
2. Launch your command window workspace shell interface (**Command Prompt** or **Anaconda Prompt**).
3. Change paths straight into your extracted project target path location directory:
   ```cmd
   cd C:\Users\HP\Documents\ExpenseTracker
