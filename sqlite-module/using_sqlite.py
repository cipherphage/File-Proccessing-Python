import sqlite3

def tenure(name, years_with_company):
    return f"{name} has worked for {years_with_company} years"

class PersonYears:
    def __init__(self):
        self.total = 0

    def step(self, value):
        self.total += value
    
    def finalize(self):
        return f"Total person years: {self.total}"

# conn = sqlite3.connect('employees.db')
conn = sqlite3.connect(':memory:')
conn.row_factory = sqlite3.Row

conn.create_function("tenure", 2, tenure)
conn.create_aggregate("person_years", 1, PersonYears)

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    years_with_company INTEGER DEFAULT 0
)
""")

cur.executemany("""
INSERT INTO employees (first_name, last_name, email, years_with_company) 
VALUES (?, ?, ?, ?)
""", [
    ('Kesin', 'Bavon', 'kb@example.com', 2),
    ('Lesin', 'Cavon', 'lc@example.com', 1),
    ('Mesin', 'Davon', 'md@example.com', 0),
])

conn.commit()

# cur.execute("SELECT * FROM employees")
# print(cur.fetchall())

# using standard row type which returns a tuple
# for row in cur.execute("SELECT * FROM employees WHERE years_with_company >= 1"):
#     print(row[1], "has worked for", row[4], "years")

for row in cur.execute("SELECT * FROM employees WHERE years_with_company >= 1"):
    print(row["first_name"], "has worked for", row["years_with_company"], "years")

cur.execute(
    "UPDATE employees SET years_with_company = ? WHERE email = ?",
    (3, "kb@example.com")
)
print(f"Updated {cur.rowcount} rows")

cur.execute("DELETE FROM employees WHERE id = 2")
print(f"Deleted {cur.rowcount} rows")

cur.execute("SELECT * FROM employees")
print(f"Remaining rows: {len(cur.fetchall())}")

for row in conn.execute("SELECT tenure(first_name, years_with_company) FROM employees"):
    print(row[0])

for row in conn.execute("SELECT person_years(years_with_company) from employees"):
    print(row[0])

cur.close()
conn.close()