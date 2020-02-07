import json

in_file = open("patient_data.txt", "r")
new_patient = json.load(in_file)
print("The patient's name is {}." .format(new_patient["first name"]))
in_file.close()
print(new_patient)
