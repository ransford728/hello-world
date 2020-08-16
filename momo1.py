customer ={
    'phone': '0546819106',
    'pin': '077',
    'bal' : '5000'
}
customer1 ={
    'phone': '0245320260',
    'pin': '077',
    'bal': '2000'
}
vendor ={
    'phone': '0241234567',
    'bal': '10000'
}
telco ={
    'tel_code': '000'
}
def deposit():
    code: input('dial telco code: ')
    telco_code = telco['tel_code']
    if code == 'tel_code':
        cnumber = input("Enter momo number: ")
        if cnumber == customer['phone']:
            print("Welcome")
        else:
            print("Number incorrect")
        amount = eval(input("Enter amount to deposit: "))
        if amount >=1:
            print("Deposit succeful")
        else:
            print("Amount not recognised")
            customer['bal'] = int(amount) + int(customer['bal'])

    else:
        print("no")
deposit()

def transfer():
    code = input("Dial telco number: ")
    if code == telco['tel_code']:
        reciever = input("Enter receiver's number: ")
        if 'receiver' == customer1['phone']:
            amount = eval(input ("Enter amount: "))
            if amount>=1:
                pin= input("Enter sender's pin: ")
                if pin == customer['phone']:
                    print("Money Trensdered sucessful.")
                else:
                    print("Money cannot be sent. ")
                    customer['bal'] = int(customer['bal'])

transfer()

