products = {
    "A1": ("Shawarma", 5),
    "A2": ("Chicken Burger", 6),
    "A3": ("Chicken Burger L", 8),

    "B1" : ("Bottled Drinking Water 500mL", 2),
    "B2" : ("Bottled Drinking Water 1L", 10),

    "C1" : ("Coke", 3),
    "C2" : ("Pepsi", 3),
    "C3" : ("Sprite", 3),

    "D1" : ("Fried Rice Combo w/ Spicy Chicken", 15),
    "D2" : ("Fried Rice Combo w/ Adobong Manac", 15),
    "D3" : ("Plain Rice w/ any combo", 15),

    "E1" : ("Sinigang add-on", 5),
    "E2" : ("Kare-Kare add-on", 5),
    "E3" : ("Tinola add-on", 5)
}

for code, (product, price) in products.items():
    print(f"{code} contains {product} and costs {price} AED.") 