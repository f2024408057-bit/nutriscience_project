import sqlite3

conn = sqlite3.connect("nutrisense.db")
cursor = conn.cursor()

# User 1
cursor.execute("""
INSERT OR IGNORE INTO users (name, email, age, goal)
VALUES ('Ali', 'ali@gmail.com', 22, 'Weight Loss')
""")

# User 2
cursor.execute("""
INSERT OR IGNORE INTO users (name, email, age, goal)
VALUES ('Sara', 'sara@gmail.com', 21, 'Weight Gain')
""")

# Food 1
cursor.execute("""
INSERT INTO foods (food_name, calories, protein, carbs)
VALUES ('Apple', 95, 0.5, 25)
""")

# Food 2
cursor.execute("""
INSERT INTO foods (food_name, calories, protein, carbs)
VALUES ('Egg', 78, 6, 1)
""")

# Food 3
cursor.execute("""
INSERT INTO foods (food_name, calories, protein, carbs)
VALUES ('Banana', 105, 1.3, 27)
""")

# Food 4
cursor.execute("""
INSERT INTO foods (food_name, calories, protein, carbs)
VALUES ('Chicken Breast', 165, 31, 0)
""")
# Pakistani Foods

cursor.execute("""
INSERT INTO foods (food_name, calories, protein, carbs)
VALUES ('Roti (1 piece)', 120, 3, 24)
""")

cursor.execute("""
INSERT INTO foods (food_name, calories, protein, carbs)
VALUES ('Rice (1 cup cooked)', 200, 4, 45)
""")

cursor.execute("""
INSERT INTO foods (food_name, calories, protein, carbs)
VALUES ('Daal (1 cup)', 230, 18, 40)
""")

cursor.execute("""
INSERT INTO foods (food_name, calories, protein, carbs)
VALUES ('Chicken Curry', 280, 25, 8)
""")

cursor.execute("""
INSERT INTO foods (food_name, calories, protein, carbs)
VALUES ('Yogurt (1 cup)', 150, 8, 12)
""")

cursor.execute("""
INSERT INTO foods (food_name, calories, protein, carbs)
VALUES ('Milk (1 glass)', 150, 8, 12)
""")

cursor.execute("""
INSERT INTO foods (food_name, calories, protein, carbs)
VALUES ('Almonds (10 pieces)', 70, 2.5, 2.5)
""")

cursor.execute("""
INSERT INTO foods (food_name, calories, protein, carbs)
VALUES ('Orange', 60, 1, 15)
""")

cursor.execute("""
INSERT INTO foods (food_name, calories, protein, carbs)
VALUES ('Spinach (cooked, 1 cup)', 40, 5, 6)
""")

cursor.execute("""
INSERT INTO foods (food_name, calories, protein, carbs)
VALUES ('Brown Bread (1 slice)', 80, 4, 15)
""")

cursor.execute("""
INSERT INTO foods (food_name, calories, protein, carbs)
VALUES ('Salmon Fillet', 200, 22, 0)
""")

cursor.execute("""
INSERT INTO foods (food_name, calories, protein, carbs)
VALUES ('Lentil Soup', 180, 12, 28)
""")
conn.commit()
conn.close()

print("Data Inserted Successfully!")