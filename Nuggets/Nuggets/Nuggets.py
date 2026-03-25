import os
filename = "nugget_ratings.txt"
def display_menu():
    print("\n--- Nugget Place Rating Menu ---")
    print("1. Rate a Nugget Place")
    print("2. View Past Ratings")
    print("3. Exit")
def rate_place():
    places = ["McDonald's", "Burger King", "Wendy's"]
    print("\nChoose your favorite nugget place:")
    for i, place in enumerate(places, start=1):
        print(f"{i}. {place}")
    print(f"{len(places) + 1}. Other")
    try:
        choice = int(input("Enter your choice number: "))
        if 1 <= choice <= len(places):
            selected_place = places[choice - 1]
        elif choice == len(places) + 1:
            selected_place = input("Enter your favorite nugget place: ")
        else:
            print("Invalid choice. Returning to menu.")
            return
    except ValueError:
        print("Invalid input. Returning to menu.")
        return
    
    rating = input(f"Rate {selected_place} out of 10: ")
    with open(filename, "a") as file:
        file.write(f"{selected_place}: {rating}/10\n")
    print(f"Your rating for {selected_place} has been saved!")

def view_ratings():
    if os.path.exists(filename):
        print("\n--- Past Nugget Ratings ---")
        with open(filename, "r") as file:
            content = file.read()
            if content:
                print(content)
            else:
                print("No ratings recorded yet.")
    else:
        print("\nNo ratings recorded yet.")
while True:
    display_menu()
    choice = input("Select an option (1-3): ")
    if choice == '1':
        rate_place()
    elif choice == '2':
        view_ratings()
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")