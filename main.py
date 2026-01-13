import csv 

people = []

while True:
    filename = input("Enter the name of your file (must end with .csv):")
    try: 
        with open(filename, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader: 
                people.append({
                    "name" : row["name"],
                    "age" : int(row["age"]),
                    "city" : row["city"]
                })
        break
    except FileNotFoundError:
        print("No such file!")
        continue

unique_cities = list(set([person["city"] for person in people]))
print("Available cities: " + ", ".join(unique_cities))

enter_city = input("Enter your city from the list above: ").strip().title()
while enter_city not in unique_cities: 
    print("No such city, check your spelling and try again!")
    enter_city = input("Enter your city from the list above: ")

def adults_sorter(people):
    adults = []
    for person in people: 
        if person["age"] >= 18:
            adults.append(person)
    return adults

def the_oldest_one(adults):
    o_name = ""
    o_age = 0
    for person in adults: 
        if o_age < person["age"]:
            o_name = person["name"]
            o_age = person["age"]
    return o_name , o_age

def count_adults(adults):
    counter = 0 
    for person in adults:
        counter += 1
    return counter

def sorter(adults):
    sorted_list = sorted(adults, key=lambda p: p["age"], reverse=True)
    return sorted_list

adults = adults_sorter(people)
o_name , o_age = the_oldest_one(adults)
counter = count_adults(adults)
sorted_list = sorter(adults)

print(f"\n The oldest person: {o_name}, their age: {o_age}")
print(f"\n The number of adults: {counter}")
print("\n Sorted list of adults: ")
for p in sorted_list:
    print(f'{p["name"]}, {p["age"]} years old, {p["city"]}')


x = input("What file do you wish the content to be saved in? (must end with .csv):  ")

with open(x, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["name" , "age" , "city"])
    writer.writeheader()

    writer.writerow({"name": f"Oldest: {o_name}", "age": o_age})
    
    for x in sorted_list:
        writer.writerow(x)



