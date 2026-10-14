# toolkit.py - Personal Mini-Toolkit Final Project

def todo_list_tool():
    """Tool 1: A dynamic Todo List manager using lists."""
    print("\n--- Tool 1: Todo List Manager ---")
    tasks = ["Buy groceries", "Complete Python assignment"]
    
    while True:
        print(f"\nCurrent Tasks: {tasks}")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Return to main menu")
        
        choice = input("Choose an option (1-3): ")
        
        if choice == "1":
            new_task = input("Enter the new task: ")
            tasks.append(new_task)
            print(f"Success! '{new_task}' has been added.")
        elif choice == "2":
            print("Your Tasks:")
            for index, task in enumerate(tasks, 1):
                print(f"{index}. {task}")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def even_counter_tool():
    """Tool 2: Counts even numbers in a user-defined range using loops and conditionals."""
    print("\n--- Tool 2: Even Number Counter ---")
    try:
        start = int(input("Enter start number: "))
        end = int(input("Enter end number: "))
        
        even_count = 0
        for num in range(start, end + 1):
            if num % 2 == 0:
                even_count += 1
                
        print(f"There are {even_count} even numbers between {start} and {end}.")
    except ValueError:
        print("Please enter valid integers.")

def tip_calculator_tool():
    """Tool 3: Calculates tips based on service quality using conditionals."""
    print("\n--- Tool 3: Tip Calculator ---")
    try:
        bill = float(input("Enter the bill amount ($): "))
        print("Service quality options: great, good, poor")
        service = input("How was the service? ").lower()
        
        if service == "great":
            tip_percentage = 0.20
        elif service == "good":
            tip_percentage = 0.15
        elif service == "poor":
            tip_percentage = 0.10
        else:
            print("Unknown service quality rating. Defaulting to 15%.")
            tip_percentage = 0.15
            
        tip_amount = bill * tip_percentage
        total_bill = bill + tip_amount
        print(f"Tip: ${tip_amount:.2f} | Total Bill: ${total_bill:.2f}")
    except ValueError:
        print("Please enter a valid number for the bill.")

def main_menu():
    """Main program loop displaying the toolkit menu."""
    print("Welcome to your Personal Mini-Toolkit!")
    
    while True:
        print("\n==============================")
        print("      MAIN TOOLKIT MENU       ")
        print("==============================")
        print("1. Todo List Manager")
        print("2. Even Number Counter")
        print("3. Tip Calculator")
        print("4. Quit")
        
        choice = input("Select a tool (1-4): ")
        
        if choice == "1":
            todo_list_tool()
        elif choice == "2":
            even_counter_tool()
        elif choice == "3":
            tip_calculator_tool()
        elif choice == "4":
            print("\nThank you for using Personal Mini-Toolkit. Goodbye!")
            break
        else:
            print("\n⚠️ Oops! That is not a valid menu option. Please choose between 1 and 4.")

if __name__ == "__main__":
    main_menu()
