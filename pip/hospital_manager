from hospital_manager import register_patient, add_bill, pay_bill, discharge_patient, delete_patient_by_name, delete_patient_by_id

def main():
    while True:
        print("\nHospital Management System:")
        print("0. Register Patient")
        print("1. Add Bill")
        print("2. Pay Bill")
        print("3. Discharge Patient")
        print("4. Delete Patient by Name")
        print("5. Delete Patient by ID")
        print("6. Exit")

        choice = input("Enter your choice (0-6): ")
        if choice == "0":
            name = input("Enter patient's full name: ")
            age = int(input("Enter patient's age: "))
            gender = input("Enter patient's gender: ")
            register_patient(name, age, gender)
        elif choice == "1":
            patient_id = int(input("Enter patient's ID: "))
            amount = float(input("Enter bill amount: "))
            add_bill(patient_id, amount)
        elif choice == "2":
            patient_id = int(input("Enter patient's ID: "))
            amount = float(input("Enter amount to pay: "))
            pay_bill(patient_id, amount)
        elif choice == "3":
            patient_id = int(input("Enter patient's ID: "))
            discharge_patient(patient_id)
        elif choice == "4":
            name = input("Enter patient's full name: ")
            delete_patient_by_name(name)
        elif choice == "5":
            patient_id = int(input("Enter patient's ID: "))
            delete_patient_by_id(patient_id)
        elif choice == "6":
            print("Exiting Hospital Management System. Goodbye!")
            break
        else:
            print("Invalid choice!!! Please enter a number between 0 and 6.")

if __name__ == "__main__":
    main()
