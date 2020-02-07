def create_dictionary():
    new_dictionary = {"day": "between sunrise and sunset",
                      "night": "when the moon is out"
                      }
    return new_dictionary


def read_dictionary(my_dict):
    my_key = "night"
    y = my_dict[my_key]
    print("The definition of {} is {}." .format(my_key, y))
    return


def add_info(my_dict):
    my_dict["lunch"] = "the meal I eat in the middle of the day"
    return my_dict


if __name__ == "__main__":
    x = create_dictionary()
    read_dictionary(x)
    x = add_info(x)
    print(x)
    z = x.get("dinner")
    print(z)
