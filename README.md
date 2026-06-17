# Simple Banking System

A lightweight, object-oriented Command Line Interface (CLI) banking application built with **Python**. This system handles user persistence via a native JSON database, allowing users to securely manage their account details, balances, and real-time transaction tracking between sessions.

---

## Features

* **Smart User Authentication:** Automatically detects whether an input username belongs to a new or existing user.
    * **New Users:** Prompted to register with a secure password and an initial deposit balance.
    * **Existing Users:** Grants profile access after password verification (supports up to 3 login attempts).
* **Core Banking Operations:** Smooth handling of money management functionality:
    * `Deposit:` Safely credits money to your balance.
    * `Withdrawal:` Debits funds with safety checks to prevent overdrafts (*"mafesh floos"*).
    * `Balance Inquiries:` Displays current active funds on demand.
* **Persistent Storage (JSON DB):** Real-time automatic updates rewrite internal balances and transaction histories to a local state file immediately following successful transactions.

---

##  Project Architecture

```text
├── assets/
│   └── output_screenshot.png  # Application preview image
├── bank_app.py                # Core application logic, main script, and UI loop
└── savingFile.json            # Local JSON state file (Auto-generated database)
