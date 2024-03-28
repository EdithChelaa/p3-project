from hospital_manager import create_patient, admit_patient, discharge_patient, transfer_patient, get_patient_info, delete_patient_by_name, delete_patient_by_id

def main():
    #initialize input descriptions
    while True:
        print("\nHospital Account Manager:")
        print("0. Register Patient")
        print("1. Admit Patient")
        print("2. Discharge Patient")
        print("3. Transfer Patient")
        print("4. Patient Information")
        print("5. Delete Patient by Name")
        print("6. Delete Patient by ID")
        print("7. Exit")

        #manage inputs
        choice = input("Enter your choice (0-7): ")
        if choice == "0":
            name = input("Enter patient's full name: ")
            age = int(input("Enter patient's age: "))
            gender = input("Enter patient's gender: ")
            create_patient(name, age, gender)
        elif choice == "1":
            patient_id = int(input("Enter patient's ID: "))
            admit_date = input("Enter admission date (YYYY-MM-DD): ")
            admit_patient(patient_id, admit_date)
        elif choice == "2":
            patient_id = int(input("Enter patient's ID: "))
            discharge_date = input("Enter discharge date (YYYY-MM-DD): ")
            discharge_patient(patient_id, discharge_date)
        elif choice == "3":
            patient_id = int(input("Enter patient's ID: "))
            new_department = input("Enter the new department: ")
            transfer_patient(patient_id, new_department)
        elif choice == "4":
            patient_id = int(input("Enter patient's ID: "))
            get_patient_info(patient_id)
        elif choice == "5":
            name = input("Enter patient's full name: ")
            delete_patient_by_name(name)
        elif choice == "6":
            patient_id = int(input("Enter patient's ID: "))
            delete_patient_by_id(patient_id)
        elif choice == "7":
            print("Exiting Hospital Account Manager. Goodbye!")
            break
        else:
            print("Invalid choice!!! Please enter a number between 0 and 7.")

if __name__ == "__main__":
    main()
