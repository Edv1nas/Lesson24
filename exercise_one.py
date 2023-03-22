from dotenv import dotenv_values


values = dotenv_values(".env")

username = values["USERNAME"]
password = values["PASSWORD"]

while True:
    user_input_username = input("Enter your username: ")
    user_input_password = input("Enter your password: ")

    if user_input_username == username and user_input_password == password:
        print("ACCESS GRANTED")
        break
    else:
        print("WRONG PASSWORD")
