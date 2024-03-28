from patients_db import PatientsDB

def main():
    patients_db = PatientsDB("patients.txt")

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
            patient = {'name': name, 'age': age, 'gender': gender}
            patients_db.save_patient(patient)
            print("Patient registered successfully!")
        elif choice == "1":
            patient_id = int(input("Enter patient's ID: "))
            amount = float(input("Enter bill amount: "))
            # Add bill logic here
        elif choice == "2":
            patient_id = int(input("Enter patient's ID: "))
            amount = float(input("Enter amount to pay: "))
            # Pay bill logic here
        elif choice == "3":
            patient_id = int(input("Enter patient's ID: "))
            # Discharge patient logic here
        elif choice == "4":
            name = input("Enter patient's full name: ")
            patients_db.delete_patient_by_name(name)
            print("Patient deleted successfully!")
        elif choice == "5":
            patient_id = int(input("Enter patient's ID: "))
            patients_db.delete_patient_by_id(patient_id)
            print("Patient deleted successfully!")
        elif choice == "6":
            print("Exiting Hospital Management System. Goodbye!")
            break
        else:
            print("Invalid choice!!! Please enter a number between 0 and 6.")

if __name__ == "__main__":
    main()
