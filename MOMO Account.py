#Mobile Money Account
print("1. send money")
print("2. withdraw money")
phone_number = "0546819106"
user = input("select choice:\n")
if user == "1":
    print("send Money")
    print("1. MTN user")
    print("2. Tigo user")
    x = input("choice:\n")
    if x == "1":
        print("MTN User:")
        number = input("Enter Mobile Number\n")
        if number == phone_number:
            amount = input("Enter Amount to send\n")
            print(amount," sent sucessfully to number",phone_number)
        else:
            print("wrong phone number or input details")
            exit()
        if x == "2":
            print("Tigo User:")
            number = input("Enter Mobile Number\n")
            print(amount,"sent sucessfully to number",phone_number)
        else:
             print("wrong phone number or input details")
             exit()




