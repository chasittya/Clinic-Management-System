from os.path import exists

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
          self.SSN = input("Enter patient's social security number (XXX-XX-XXXX):")

     def setBirthday(self):
          self.birthday = input("Please enter patient's birthday (YYYYMMDD): ")
           

     def setGender(self):
           self.gender = input("Please enter the gender of the patient: ")

     def read(self, file_name):
          patient_file = open(self.getPatientID + '.txt', 'r')
          patient_file.readlines()

          # test
          patient_file.close()

     def write(self,):
           with open (file_name)
           return
           
     def deleteFile(self, file_name):
          # look for file
          
          warning_message = input("Are you sure you want to delete this patient's file? (Y/N): ")
          if warning_message == 'y' or "Y":
               self.remove(file_name)
               print("Patient file has been deleted.")
          else:
               print("Patient file has not been deleted.")
     
     def printFile (self, file_name):
          attributes = ["Patient ID: ", "First Name: ", "Last Name: ", "Social Security Number: ", "Birthday (YYYY-MM-DD): ", "Gender: " ]
          patient_file = open(file_name, 'r')
          file_lines = patient_file.readlines()
          for line in file_lines:
                print (line)

     def find(self, patientID):
           return
     
     def update_PatientID(self):
           self.patientID = self.setPatientID()
           self.write()                 #update patient file

     def updateFName(self):
           self.FName = self.setFname()
           self.write()                 #update patient file

     def updateLName(self):
           self.LName = self.LName()
           self.write()                 #update patient file


     #Function to add a patient to the list of patients
     def add_patient(self, patients):
          

          newPatient = Patient()
          newPatient.name = input("Patient name: ")
          newPatient.age = input("Patient age: ")
          newPatient.gender = input("Patient gender (M/F): ")
          newPatient.contact_info = input("Patient contact information: ")
          newPatient.medical_history = input("Patient medical history: ")

          # with open(newPatient.name + '.txt', "w") as file:
          #      self.write(newPatient.name  newPatient.age)
          # pass




class Staff:
     def __init__(self,sname,srole,scontact_info):
       
        self.staffID = ""
        self.FName = ""
        self.LName= ""
        self.srole = ""
        self.scontact_info = ""

     def getStaffID(self):
          return self.staffID
     
     def setStaffID(self):
          self.staffID = input("Enter Staff ID: ")
            
     def getFName(self):
          return self.FName
     
     def setFname(self):
          self.FName = input("Enter Staff first name: ")
     
     def getLName(self):
          return self.LName
     
     def setFname(self):
          self.LName = input("Enter Staff last name: ")

     def getSrole(self):
          return self.srole
     
     def setSrole(self):
          self.srole = input("Enter Staff Role: ")  

     def getScontactInfo(self):
          return self.scontact_info
     
     def setScontactInfo(self):
          self.scontact_info = input("Enter Staff Contact Info: ")  

     def read(self, file_name):
          patient_file = open(self.getStaffID + '.txt', 'r')
          patient_file.readlines()

          # test
          text_file.close()

     def write(self, fileName):
           return
           
     def deleteFile(self, file_name):
          # look for file
          
          warning_message = input("Are you sure you want to delete this staff member's file? (Y/N): ")
          if warning_message == 'y' or "Y":
               self.remove(file_name)
               print("Staff file has been deleted.")
          else:
               print("Staff file has not been deleted.")
     
     def printFile (self, file_name):
          attributes = ["Staff ID"]
          staff_file = open(file_name, 'r')
          file_lines = staff_file.readlines()
          for line in file_lines:
                print (line)

     def find(self, StaffID):
           return
     
     def update_StaffID(self):
           self.staffID = self.setStaffID()

     def updateFName(self):
           self.FName = self.setFname()

     def updateLName(self):
           self.LName = self.LName()

     #Function to add a staff member to the list of staff
     def add_staff(staff):
          newStaff = Staff()
          newStaff.FName = input ("Staff First Name: ")
          newStaff.LName = input ("Staff Last Name: ")
          newStaff.srole = input("Staff Role: ")
          newStaff.scontact_info = input("Staff Contact Info: ")
          pass 

class Appointment:
     def __init__(self,patient,doctor,appointment_datetime):
          self.patientID = patient_id
          self.doctor = ""
          self.appointment_datetime = appointment_datetime
     
     #Function to schedule a new appointment
     def schedule_appointment(appointments,patients,staff):
          patient_id = input("Enter patient ID: ")
          
          appointment_datetime = input("Enter appointment date and time (YYYY-MM-DD) (Hours:Minutes)AM/PM: ")
          

          appointment = 
          {
               "patient_id": patient_id,
               "datetime": appointment_datetime,
               
          }

          appointment.append(appointment)

          print("Appointment scheduled successfully")
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
