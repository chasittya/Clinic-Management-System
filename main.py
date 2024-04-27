
import os

#Classes for patient, staff, and appointments

class Patient:
     def __init__(self):
        self.patientID = ""
        self.FName = ""
        self.LName= ""
        self.SSN = ""
        self.birthday = "" 
        self.gender = ""
        self.contactName = ""
        self.contactPhone = ""
        self.medical_history = ""
        self.notes = ""

     def getPatientID(self):
          return self.patientID
     
     def setPatientID(self):
          self.patientID = input("Enter Patient ID: ")
            
     def getFName(self):
          return self.FName
     
     def setFname(self):
          self.FName = input("Enter Patient first name: ")
     
     def getLName(self):
          return self.LName
     
     def setFname(self):
          self.LName = input("Enter Patient last name: ")

     def getSSN(self):
          return self.SSN
     
     def setSSN(self):
          self.SSN = input("Enter patient's social security number:")
     
     def read(self, fileName):
          text_file = open(self.getPatientID + '.txt', 'r')
          text_file.readlines()
          # test


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
          newStaff = staff()
          newStaff.name = input("Staff Name: ")
          newStaff.age = input("Staff Age: ")
          newStaff.gender = input("Staff Gender: ")
          newStaff.contact_info = input("Staff Contact Info: ")
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
