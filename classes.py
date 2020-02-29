class Person:
    first_name = None
    last_name = None
    age = None

    def __init__(self, first_name_arg=None,
                 last_name_arg=None, age_arg=None):
        self.first_name = first_name_arg
        self.last_name = last_name_arg
        self.age = age_arg

    # def increase_age(self, number_of_years=1):
    #     self.age = self.age + number_of_years

    def print_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def print_all_info(self):
        full_name = self.print_full_name()
        print("Patient name is {}".format(full_name))
        print("Age is {}".format(self.age))


def create_person(first, last, age):
    new_person = Person(first, last, age)
    # new_person.first_name = 'Bob'
    # new_person.last_name = 'Anderson'
    # new_person.age = 30
    return new_person


def print_patient_info(pat):
    print("First name is {}".format(pat.first_name))
    print("Last name is {}".format(pat.last_name))
    print("Age is {}".format(pat.age))


def age_patient(pat):
    pat.age = pat.age + 1
    return pat


def minor(pat):
    if pat.age < 18:
        pat.minor = True
    else:
        pat.minor = False
    return pat


def main():
    db = list()
    x = create_person("Bob", "Anderson", 30)
    db.append(x)
    y = Person("Jose", "George", 23)
    db.append(y)
    for patient in db:
        # print("{} {}".format(patient.first_name,
        #                      patient.last_name))
        patient.print_all_info()

    # print_patient_info(x)
    # x.increase_age(5)
    # print_patient_info(x)
    # y = Person()
    # print(y.first_name)


if __name__ == '__main__':
    main()
