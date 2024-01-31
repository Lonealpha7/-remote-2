# cars.py

import random

car_brands = ["Toyota", "Ford", "Chevrolet", "Honda", "BMW", "Mercedes-Benz"]

def get_random_model_year():
    return random.randint(1990, 2024)  

selected_brand = random.choice(car_brands)

print(f"Randomly selected car brand: {selected_brand}")
print(f"Random model year: {get_random_model_year()}")

