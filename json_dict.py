def create_patient():
    new_patient = {"last name": "Smith",
                   "first name": "Bob",
                   "age": 60,
                   "married": False,
                   "test results": [0, 16, 23, 2.3]
                   }
    return new_patient


def save_Json(patient):
    import json
    filename = "patient_data.txt"
    out_file = open(filename, 'w')
    json.dump(patient, out_file)
    out_file.close()


if __name__ == "__main__":
    x = create_patient()
    save_Json(x)
