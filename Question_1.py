#Task 1
restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

restaurant_menu["Beverages"] = {"Beer": 5.99, "Wine": 7.99, "Whiskey": 12.99}

restaurant_menu["Main Course"]["Steak"] = 17.99

restaurant_menu["Starters"].popitem()


print(restaurant_menu)