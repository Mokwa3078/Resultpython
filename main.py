

# Function to display all results
def displayResults():
    with open("results.txt", "r") as file:
        for line in file:
            name, addno, subject, marks = line.strip().split(",")
            print(f"Name: {name}, Addmission No: {addno}, Subject: {subject}, Marks: {marks}")


# Function to add a student's result
def addResult():
    name = input("Enter student's name: ")
    addno = input("Enter Addmission number: ")
    subject = input("Enter Subject: ")
    marks = float(input("Enter marks: "))

    with open("results.txt", "a") as file:
        file.write(f"{name},{addno},{subject},{marks}\n")


# Function to search a student's result
def searchResult():
    addno = input("Enter Addmission number to search: ")

    with open("results.txt", "r") as file:
        for line in file:
            name, addmission_search, subject, marks = line.strip().split(",")
            if addmission_search == addno:
                print(f"Name: {name}, Addmission No: {addno}, Subject: {subject}, Marks: {marks}")
                break
        else:
            print("No result found.")

# Main menu
while True:
    print("Result Computing System")
    print("1. Add Result")
    print("2. Display All Results")
    print("3. Search Result")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        addResult()
        print()
    elif choice == "2":
        displayResults()
        print()
    elif choice == "3":
        searchResult()
        print()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")
