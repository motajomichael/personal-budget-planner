# budget/config.py

DEFAULT_MONTHS = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
]

# Derived from your spreadsheet structure.
# (group, item, type) where type in {"income", "expense"}.
DEFAULT_CATEGORIES = [
    # INCOME
    ("Income", "Wages & Tips", "income"),
    ("Income", "Interest Income", "income"),
    ("Income", "Dividends", "income"),
    ("Income", "Gifts Received", "income"),
    ("Income", "Refunds/Reimbursements", "income"),
    ("Income", "Transfer From Savings", "income"),
    ("Income", "Other Income 1", "income"),
    ("Income", "Other Income 2", "income"),

    # HOME EXPENSES
    ("Home Expenses", "Mortgage/Rent", "expense"),
    ("Home Expenses", "Electricity", "expense"),
    ("Home Expenses", "Gas", "expense"),
    ("Home Expenses", "Water & Sewer", "expense"),
    ("Home Expenses", "Trash", "expense"),
    ("Home Expenses", "Phone", "expense"),
    ("Home Expenses", "Mobile Phone", "expense"),
    ("Home Expenses", "Cable/Satellite", "expense"),
    ("Home Expenses", "Internet", "expense"),
    ("Home Expenses", "Home Maintenance", "expense"),
    ("Home Expenses", "Other Home 1", "expense"),
    ("Home Expenses", "Other Home 2", "expense"),

    # TRANSPORTATION
    ("Transportation", "Auto Loan", "expense"),
    ("Transportation", "Auto Insurance", "expense"),
    ("Transportation", "Fuel", "expense"),
    ("Transportation", "Bus/Taxi/Train Fare", "expense"),
    ("Transportation", "Repairs", "expense"),
    ("Transportation", "Registration/License", "expense"),
    ("Transportation", "Other Transport", "expense"),

    # HEALTH
    ("Health", "Health Insurance", "expense"),
    ("Health", "Doctor/Dentist", "expense"),
    ("Health", "Medicine/Drugs", "expense"),
    ("Health", "Health Club Dues", "expense"),
    ("Health", "Life Insurance", "expense"),
    ("Health", "Gym", "expense"),
    ("Health", "Other Health", "expense"),

    # DAILY LIVING
    ("Daily Living", "Groceries", "expense"),
    ("Daily Living", "Household Supplies", "expense"),
    ("Daily Living", "Clothing", "expense"),
    ("Daily Living", "Dry Cleaning/Laundry", "expense"),
    ("Daily Living", "Hair Care/Cosmetics", "expense"),
    ("Daily Living", "Babysitting/Child Care", "expense"),
    ("Daily Living", "Daycare", "expense"),
    ("Daily Living", "Lunch Money", "expense"),
    ("Daily Living", "Pet Food & Care", "expense"),
    ("Daily Living", "Tobacco", "expense"),
    ("Daily Living", "Alcohol", "expense"),
    ("Daily Living", "Other Daily 1", "expense"),
    ("Daily Living", "Other Daily 2", "expense"),

    # ENTERTAINMENT
    ("Entertainment", "Videos/DVDs", "expense"),
    ("Entertainment", "Music", "expense"),
    ("Entertainment", "Games", "expense"),
    ("Entertainment", "Rentals", "expense"),
    ("Entertainment", "Movies/Theater", "expense"),
    ("Entertainment", "Concerts/Plays", "expense"),
    ("Entertainment", "Books", "expense"),
    ("Entertainment", "Hobbies", "expense"),
    ("Entertainment", "Film/Photos", "expense"),
    ("Entertainment", "Sports", "expense"),
    ("Entertainment", "Outdoor Recreation", "expense"),
    ("Entertainment", "Toys/Gadgets", "expense"),
    ("Entertainment", "Vacation/Travel", "expense"),
    ("Entertainment", "Other Entertainment", "expense"),

    # SAVINGS
    ("Savings", "Emergency Fund", "expense"),
    ("Savings", "Retirement", "expense"),
    ("Savings", "Investments", "expense"),
    ("Savings", "College", "expense"),
    ("Savings", "Other Savings", "expense"),

    # GIFTS & DONATIONS
    ("Gifts & Donations", "Gifts", "expense"),
    ("Gifts & Donations", "Charitable Donations", "expense"),
    ("Gifts & Donations", "Other Gifts", "expense"),

    # OBLIGATIONS
    ("Obligations", "Student Loans", "expense"),
    ("Obligations", "Credit Card 1", "expense"),
    ("Obligations", "Credit Card 2", "expense"),
    ("Obligations", "Credit Card 3", "expense"),
    ("Obligations", "Personal Loan", "expense"),
    ("Obligations", "Alimony", "expense"),
    ("Obligations", "Child Support", "expense"),
    ("Obligations", "Federal Taxes", "expense"),
    ("Obligations", "State/Local Taxes", "expense"),
    ("Obligations", "Other Obligations", "expense"),

    # SUBSCRIPTIONS
    ("Subscriptions", "Apple One", "expense"),
    ("Subscriptions", "Magazines", "expense"),
    ("Subscriptions", "Dues/Memberships", "expense"),
    ("Subscriptions", "Other Subscriptions", "expense"),

    # MISCELLANEOUS
    ("Miscellaneous", "Bank Fees", "expense"),
    ("Miscellaneous", "Postage", "expense"),
    ("Miscellaneous", "Other Misc 1", "expense"),
    ("Miscellaneous", "Other Misc 2", "expense"),
]
