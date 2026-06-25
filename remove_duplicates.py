import sqlite3

conn = sqlite3.connect("nutrisense.db")
cursor = conn.cursor()

cursor.execute("""
DELETE FROM foods
WHERE id NOT IN (
    SELECT MIN(id)
    FROM foods
    GROUP BY food_name
)
""")

conn.commit()
conn.close()

print("Duplicates Removed Successfully!")
