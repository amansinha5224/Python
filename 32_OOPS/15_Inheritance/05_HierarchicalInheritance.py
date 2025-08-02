'''
Hierarchical Inheritance:-
    - In this type of inheritance, multiple child class inherit properties from single parent class
'''

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def displayPersonInfo(self):
        print(f"NAME: {self.name}\nAGE: {self.age}\nGENDER: {self.gender}")

class Doctor(Person):
    def __init__(self, name, age, gender, specialization, years_of_experience):
        super().__init__(name, age, gender)
        self.specialization = specialization
        self.years_of_experience = years_of_experience

    def displayDoctorInfo(self):
        super().displayPersonInfo()
        print(f"SPECIALIZATION: {self.specialization}\nYEARS OF EXPERIENCE: {self.years_of_experience}")

class Patient(Person):
    def __init__(self, name, age, gender, disease, admission_date):
        super().__init__(name, age, gender)
        self.disease = disease
        self.admission_date = admission_date

    def displayPatientInfo(self):
        super().displayPersonInfo()
        print(f"DISEASE: {self.disease}\nADMISSION DATE: {self.admission_date}")

class Nurse(Person):
    def __init__(self, name, age, gender, ward, shift):
        super().__init__(name, age, gender)
        self.ward = ward
        self.shift = shift

    def displayNurseInfo(self):
        super().displayPersonInfo()
        print(f"WARD: {self.ward}\nSHIFT: {self.shift}")

doc1 = Doctor("Rahul", 45, "Male", "Neuro Surgeon", "10")
pat1 = Patient("Dev", 25, "Male", "Cold", "02-08-2025")
nur1 = Nurse("Nandni", 30, "Female", "432A", "Morning")

doc1.displayDoctorInfo()
print()
pat1.displayPatientInfo()
print()
nur1.displayNurseInfo()
print()