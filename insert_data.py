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
foods = [
('Beef Curry',250,20,5),
('Fish Curry',220,22,4),
('Chapati',110,3,22),
('Paratha',260,5,30),
('Boiled Egg',78,6,1),
('Fried Egg',90,6,1),
('Omelette',154,11,2),
('White Bread Slice',75,3,14),
('Whole Wheat Bread',80,4,15),
('Tea with Milk',70,2,8),
('Coffee with Milk',90,3,10),
('Dates (3)',70,1,18),
('Guava',68,2.6,14),
('Mango',99,1.4,25),
('Watermelon',46,1,12),
('Pear',100,1,27),
('Peanuts (20g)',113,5,4),
('Cashews (10)',90,3,5),
('Walnuts (5)',130,3,3),
('Paneer',265,18,6),
('Cheese Slice',113,7,1),
('Butter (1 tbsp)',102,0,0),
('French Fries',312,4,41),
('Burger',295,17,30),
('Pizza Slice',285,12,36),
('Biryani (1 plate)',450,18,55),
('Pulao (1 cup)',250,6,40),
('Kebab (2)',220,16,4),
('Shami Kebab',140,10,6),
('Chana Masala',270,14,35),
('Rajma',215,13,40),
('Aloo Sabzi',180,4,28),
('Bhindi',90,3,12),
('Cucumber',16,1,4),
('Tomato',22,1,5),
('Carrot',41,1,10),
('Apple Juice',114,0,28),
('Orange Juice',112,2,26),
('Ice Cream',207,3,24),
('Chocolate Bar',230,3,25)
]

for food in foods:
    cursor.execute("""
    INSERT INTO foods (food_name, calories, protein, carbs)
    VALUES (?, ?, ?, ?)
    """, food)
conn.commit()
conn.close()

print("Data Inserted Successfully!")