F1 = ["F1", "VW Off-Road-Bug", 235 , (145, 198), 6500, 5.5, 1880, 4]
G2 = ["G2", " Seat Ibiza GTi", 220, (205, 280), 8400, 6.5, 1984, 4]
F3 = ["F3", "Renault Megane", 218, (198, 270), 8400, 5.9, 1995, 4]
G3 = ["G3", "Mitsubishi Pajero", 185, (153, 208), 7000, 9.6, 3497, 6]
A4 = ["A4", "Suzuki Ignis", 180, (153, 206), 7250, 8.0, 1597, 4]
G1 = ["G1", "Citroen Visa 4x4", 190, (74, 100), 7680, 9, 1566, 4]
C3 = ["C3", "VW-polo GTI", 185, (96,103), 7600, 8, 1600, 4]
B1 = ["B1", "Seat Cordoba WRC", 230, (221, 300), 6000, 5, 1998, 4]
E2 = ["E2", "Ford Escort WRC", 220, (220, 299), 6250, 5.6, 1993, 4]
B3 = ["B3", "Toyota Corolla WRC", 210, (220, 299), 5700, 5.4, 1972, 4 ]


# All cars
cars = [F1, G2, F3, G3, A4, G1, C3, B1, E2, B3]

# Welcome
print("WELCOME TO QUARTET")
print("===================")
print(f"Number of cars: {len(cars)}")
print()

# Show cars
print("Your cars:")
i = 1
for car in cars:
    print(f"{i}. {car[0]} - {car[1]}")
    i += 1

print()

# Pick a car
choice = int(input("Pick a car by number: "))
chosen_car = cars[choice - 1]

print()
print("YOUR CHOSEN CAR")
print("----------------")
print(f"ID: {chosen_car[0]}")
print(f"Name: {chosen_car[1]}")
print(f"Top Speed: {chosen_car[2]}","Power: {chosen_car[3]}")
