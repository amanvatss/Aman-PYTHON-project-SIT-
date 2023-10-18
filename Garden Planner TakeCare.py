# Initialize the garden plot as a 2D grid
garden_width = 10
garden_height = 10
garden = [["Empty" for _ in range(garden_width)] for _ in range(garden_height)]

# Define a dictionary to store plant information
plant_database = {
    "Tomato": {
        "spacing": 12,
        "care": "Tomatoes need full sun and regular watering. Provide support for the vines, prune as needed, and watch for pests."
    },
    "Carrot": {
        "spacing": 3,
        "care": "Plant carrots in loose, well-drained soil. Keep the soil consistently moist and thin seedlings to the recommended spacing."
    },
    # Add more plants and their care instructions here
}


# Function to display the garden plot
def display_garden():
    for row in garden:
        print(" | ".join(row))
        print("-" * (4 * garden_width - 1))


# Function to display care instructions for a plant
def display_care_instructions(plant_name):
    if plant_name in plant_database:
        care_instructions = plant_database[plant_name]["care"]
        print(f"Care Instructions for {plant_name}: {care_instructions}")
    else:
        print("Plant not found in the database.")


# Function to plant a plant in the garden
def plant_plant(plant_name, x, y):
    if garden[y][x] == "Empty":
        garden[y][x] = plant_name
        print(f"Planted {plant_name} at ({x}, {y})")
    else:
        print("There's already a plant there!")


# Main menu
while True:
    print("\nMain Menu:")
    print("1. Display Garden")
    print("2. Plant a Plant")
    print("3. Display Care Instructions")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_garden()
    elif choice == "2":
        plant_name = input("Enter the plant name: ")
        if plant_name in plant_database:
            x = int(input("Enter the x-coordinate: "))
            y = int(input("Enter the y-coordinate: "))
            plant_plant(plant_name, x, y)
        else:
            print("Plant not found in the database.")
    elif choice == "3":
        plant_name = input("Enter the plant name: ")
        display_care_instructions(plant_name)
    elif choice == "4":
        print("Exiting the garden planner.")
        break
    else:
        print("Invalid choice. Please try again.")
