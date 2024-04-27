

#Classes for patient, staff, and appointments

class Patient:
     def __init__(self,patientID, FName, LName, SSN, birthday, 
                 gender, contactName, contactPhone, medical_history, notes):
        self.patientID = patientID
        self.FName = FName
        self.LName= LName
        self.SSN = SSN
        self.birthday = birthday
        self.gender = gender
        self.contactName = contactName
        self.contactPhone = contactPhone
        self.medical_history = medical_history
        self.notes = notes

     #Function to add a patient to the list of patients
     def add_patient(patients):
          newPatient = Patient()
          newPatient.name = input("Patient name: ")
          newPatient.age = input("Patient age: ")
          newPatient.gender = input("Patient gender (M/F): ")
          newPatient.contact_info = input("Patient contact information: ")
          newPatient.medical_history = input("Patient medical history: ")

          # with open(newPatient.name + '.txt', "w") as file:
          #      file.write(newPatient.name  newPatient.age)
          # pass




class Staff:
     def __init__(self,sname,srole,scontact_info):
        self.sname= sname
        self.srole = srole
        self.scontact_info = scontact_info

     #Function to add a staff member to the list of staff
     def add_staff(staff):
          pass

class Appointment:
     def __init__(self,patient,doctor,appointment_datetime):
          self.patient = patient
          self.doctor = doctor
          self.appointment_datetime = appointment_datetime
     
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

if __name__ == " __main__":
       main()