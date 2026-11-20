FILE_NAME = "employees.txt"


def format_employee_record(name, emp_id, salary):
    """Formats employee details into a single pipe-separated string."""
    return f"{name} | {emp_id} | {salary}\n"


def add_employee(name, emp_id, salary):
    """Appends a formatted employee record to the text file."""
    record = format_employee_record(name, emp_id, salary)
    with open(FILE_NAME, "a") as file:
        file.write(record)
    return "Employee Added Successfully"


def read_employees():
    """Reads all lines from the employee file and returns them as a list."""
    try:
        with open(FILE_NAME, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return []


def view_employees():
    """Displays all stored employee records cleanly."""
    records = read_employees()
    if not records:
        print("\nNo employee records found.\n")
        return

    print("\n--- Employee Records ---")
    for record in records:
        print(record.strip())
    print("------------------------\n")


def main():
    """Runs the main interactive menu loop."""
    while True:
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Exit")

        choice = input("Choose Option: ").strip()

        if choice == "1":
            name = input("Enter Name: ").strip()
            emp_id = input("Enter ID: ").strip()
            salary = input("Enter Salary: ").strip()

            status = add_employee(name, emp_id, salary)
            print(f"{status}\n")

        elif choice == "2":
            view_employees()

        elif choice == "3":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1, 2, or 3.\n")


if __name__ == "__main__":
    main()
