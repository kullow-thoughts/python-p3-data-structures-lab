spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
     return [f['name'] for f in spicy_foods if 'name' in f]

    

def get_spiciest_foods(spicy_foods):
    return [f for f in spicy_foods if f.get ("heat_level", 0)> 5]
    

def print_spicy_foods(spicy_foods):
    for f in spicy_foods:
        print(f"{f['name']} ({f['cuisine']}) | Heat Level: {f['heat_level'] * '🌶'}") 
        #print(f"{food['name']} ({food['cuisine']}) | Heat Level: {food['heat_level']*'🌶'}")
   

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for f in spicy_foods:
        if f ["cuisine"]== cuisine: 
            return f 
    

def print_spiciest_foods(spicy_foods):
    for f in spicy_foods:
        if f ["heat_level"] > 5:
           print(f"{f['name']} ({f['cuisine']}) | Heat Level: {f['heat_level'] * '🌶'}") 
    
    

def get_average_heat_level(spicy_foods):
    heat_level_count = 0
    for f in spicy_foods:
        heat_level_count += f["heat_level"]
    return heat_level_count/len(spicy_foods)
    

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods


