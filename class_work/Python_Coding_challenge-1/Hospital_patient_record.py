'''Hospital Patient Record Management System 
Problem Statement A hospital maintains patient details in a file named patients.txt. 
Sample Input/Data (patients.txt) 
 P101,Anuj,Normal 
 P102,Rahul,Critical 
 P103,Priya,Stable 
 P104,Neha,Critical 
 P105,Amit,Stable 
 P106,Sneha,Normal 
 P107,Karan,Critical 
 P108,Pooja,Stable 
 P109,Rohit,Normal 
 P110,Anjali,Stable 
Tasks:-
1. Display all patient records.  
2. Display critical patients.  
3. Count patients under each status.  
4. Search patient details using Patient ID.  
5. Save critical patient records to critical_patients.txt.'''
#-----------------------------------------------------------------------------------------------------------------
#Display all patient records
file = open("patient.txt","r")
records = file.readlines()
file.close()

print("All Patient records")
for record in records:
    print(record.strip())
#------------------------------------------------------------------------------------------------------------------
#Display critical patients
print("Critical Patients:")
critical_records = []
for record in records:
    patient_id , name , status = record.strip().split(",")
    if status == "Critical":
        print(name)
        critical_records.append(record)
#-------------------------------------------------------------------------------------------------------------------
#Count patient under each status 
normal_count = 0
stable_count = 0
critical_count = 0

for record in records:
    patient_id , name , status = record.strip().split(",")
    if status == "Normal":
        normal_count +=1

    elif status == "Stable":
        stable_count += 1

    elif status == "Critical":
        critical_count += 1
print("Patient Count:")
print("Normal :", normal_count)
print("Stable :", stable_count)
print("Critical :", critical_count)
#--------------------------------------------------------------------------------------------------------------------
#Search patient using Patient ID
search_id = input("\nEnter Patient ID: ")
found = False
for record in records:
    patient_id, name, status = record.strip().split(",")

    if patient_id == search_id:
        print("Patient Found:", record.strip())
        found = True
        break
if not found:
    print("Patient Not Found")
#----------------------------------------------------------------------------------------------------------------------
# Save critical patients to another file
file = open("critical_patients.txt", "w")
for record in critical_records:
    file.write(record)
file.close()
print("\nCritical Patient Report Generated Successfully.")
