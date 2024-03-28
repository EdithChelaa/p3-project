class PatientsDB:
    def __init__(self, filename):
        self.filename = filename

    def save_patient(self, patient):
        # Write patient data to the database file
        with open(self.filename, 'a') as file:
            file.write(f"{patient['name']},{patient['age']},{patient['gender']}\n")

    def get_all_patients(self):
        # Read all patients from the database file
        patients = []
        with open(self.filename, 'r') as file:
            for line in file:
                name, age, gender = line.strip().split(',')
                patients.append({'name': name, 'age': int(age), 'gender': gender})
        return patients

    def delete_patient_by_name(self, name):
        # Delete patient from the database file by name
        patients = self.get_all_patients()
        updated_patients = [patient for patient in patients if patient['name'] != name]
        self._rewrite_db(updated_patients)

    def delete_patient_by_id(self, patient_id):
        # Delete patient from the database file by ID (index)
        patients = self.get_all_patients()
        if 0 <= patient_id < len(patients):
            del patients[patient_id]
            self._rewrite_db(patients)
        else:
            print("Invalid patient ID.")

    def _rewrite_db(self, patients):
        # Rewrite the entire database file with updated patient data
        with open(self.filename, 'w') as file:
            for patient in patients:
                file.write(f"{patient['name']},{patient['age']},{patient['gender']}\n")
