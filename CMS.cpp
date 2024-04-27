

#Classes for patient, staff, and appointments

class Patient:
    def __init__(self,name,age,gender, contact_info,medical_history):
        self.name= name 
        self.age = age
        self.gender = gender
        self.contact_info = contact_info
        self.medical_history = medical_history


class Staff:
        def __init__(self,name,role,contact_info):
        self.name= name
        self.role = role
        self.contact_info = contact_info

class Appointment:
     def __init__(self,patient,doctor,appointment_datetime):
          self.patient = patient
          self.doctor = doctor
          self.appointment_datetime = appointment_datetime

#Function to add a patient to the list of patients
def add_patient(patients):
     pass

#Function to add a staff member to the list of staff
def add_staff(staff):
     pass

#Function to schedule a new appointment
def schedule_appointment(appointments,patients,staff):
     pass

def main():
     patients = []
     staff = []
     appointments = []

#Main Menu
while True:
     print("Main Menu")
     print("1. Add Patient")
     print("2.Add Staff")
     print("3. Schedule Appointment")
     print("4.Exit")
     choice = input("Enter your selection ")

 
if choice == '1':
          add_patient(patients)
elif choice == '2':
            add_staff(staff)
elif choice =='3':
            schedule_appointment(appointments,patients,staff)
elif choice == '4':
            print("Exiting program...")
else:
            print("Invalid selection. Try Again.")
    else:
            print("Invalid selection. Try Again.")

if __name__ == " __main__":
       main()
