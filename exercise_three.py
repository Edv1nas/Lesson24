"""[8:14 PM] Vytautas Sluckas

write a function that accepts an encoded string as a parameter. This string will contain a first name, last name, and an id.
Values in the string can be separated by any number of zeros. The id is a numeric value but will contain no zeros. The function should parse the string and return a Python dictionary that contains the first name, last name, and id values.
An example input would be “Robert000Smith000123”. The function should return the following using that input:
{​​ “first_name”: “Robert”, “last_name”: “Smith”, “id”: “123” }​​"""


def split_value(encoded_str: str) -> None:
    split_value = encoded_str.split("0")
    filtered_list = list(filter(None, split_value))
    return {"first_name": filtered_list[0], "last_name": filtered_list[1], "id": filtered_list[2]}


inputed_value = "Robert000Smith000123"
filtered_values_dict = split_value(inputed_value)
print(filtered_values_dict)
