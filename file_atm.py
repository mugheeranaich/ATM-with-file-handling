import os
import sys
from tabulate import tabulate

all_args =sys.argv
args = all_args[1:]

if args[0] == "--register":
    name = input("Enter Your Name: ")
    father_name = input("Enter your Father name: ")
    user_name  = input("Enter user name: ")
    password = input("Enter your pin: ")
    amount = 0
    c =os.listdir("/home/mugheera/aatm")

    for i in c:


        if  user_name != i:
            with open(f'./{user_name}',"a") as f:
                f.write("{\n")
                f.write(f'name:{name}\nfather name:{father_name}\nuser name:{user_name}\nAmount:{amount}\npin:{password}\n')
                f.write("}\n")
            print("hello")

        else:
            sys.exit("user_name is  already avalible\n Try another user name")

elif  args[0] == "--login":
    name2 = input("Enter user name: ")
    pin = input("Enter your pin: ")

    c =os.listdir("./")

    for i in c:

        if name2 == i:

            with open(f'{name2}',"r") as f:
                content = f.readlines()

                for line in content:
                    lines=line.strip()

                    if lines.startswith("user name:"):
                        user = lines.split("user name:")

                    elif lines.startswith("name:"):
                        Name = lines.split("name:")

                    elif lines.startswith("father name:"):
                        father_name = lines.split("father name:")

                    elif lines.startswith("pin:"):
                        pin2 = lines.split("pin:")

                        if  name2 == user[1] and pin == pin2[1]:
                            print(f"Welcome {name2}!!")
                            print("1:Deposit\n2:withdrawal\n3:Send money\n4:Check balance")

                            user_input = int(input("Enter your choice: "))

                            if user_input == 1:
                                deposit = int(input("Enter the amount to Deposit: "))

                                if deposit >=0:
                                    with open(f'{name2}',"r") as f:
                                        content = f.readlines()

                                        for line in content:
                                            lines=line.strip()

                                            if lines.startswith("Amount:"):
                                                amount = lines.split("Amount:")
                                                amount2 = int(amount[1]) + deposit

                                                with open(f'{name2}',"w") as f:
                                                    f.write(f'name:{Name[1]}\nfather name:{father_name[1]}\nuser name:{name2}\nAmount:{str(amount2)}\npin:{pin}\n')

                                                    print(f'{deposit}Deposit successful!!')

                                else:
                                    raise Exception("Invalid amount\n Amount should be >0")

                            elif user_input == 2:
                                withdrawal = int(input("Enter the amount to withdrawal: "))

                                with open(f'{name2}',"r") as f:
                                    content = f.readlines()

                                    for line in content:
                                        lines=line.strip()

                                        if lines.startswith("Amount:"):
                                            amount = lines.split("Amount:")

                                            if withdrawal >= 0 and withdrawal <= int(amount[1]):
                                                amount2 = int(amount[1]) - withdrawal

                                                with open(f'{name2}',"w") as f:
                                                    f.write(f'name:{Name[1]}\nfather name:{father_name[1]}\nuser name:{name2}\nAmount:{str(amount2)}\npin:{pin}\n')

                                                    print(f"{withdrawal} Withdrawal successful!!")

                                            elif withdrawal < 0:
                                                raise Exception("Invalid amount\nAmount should be >0")

                                            elif withdrawal > int(amount[1]):
                                                raise Exception("Low Account Balance")

                            elif user_input == 4:
                                with open(f'{name2}',"r") as f:
                                    content = f.readlines()

                                    for line in content:
                                        lines=line.strip()

                                        if lines.startswith("Amount:"):
                                            amount = lines.split("Amount:")
                                            print(f"Your account Balance is {amount[1]}")

                            elif user_input == 3:
                                recipent_account = input("Enter the recipient account user name: ")
                                transfer_amount = int(input("Enter the amount that you wan't to send: "))

                                c =os.listdir("/home/mugheera/aatm")
                                for i in c:
                                    if recipent_account == i:

                                        with open(f'{name2}',"r") as f:
                                            content = f.readlines()

                                            for line in content:
                                                lines = line.strip()

                                                if lines.startswith("Amount:"):
                                                    amount = lines.split("Amount:")

                                                    if transfer_amount >= 0 and transfer_amount <= int(amount[1]):
                                                        amount2 = int(amount[1]) - transfer_amount


                                                        with open(f'{name2}',"w") as f:
                                                            g = "{"
                                                            h = "}"
                                                            f.write(f'{g}\nname:{Name[1]}\nfather name:{father_name[1]}\nuser name:{name2}\nAmount:{str(amount2)}\npin:{pin}\n{h}')

                                                            with open(f'{recipent_account}',"r") as f:
                                                                content = f.readlines()

                                                            for line in content:
                                                                lines = line.strip()

                                                                if lines.startswith("user name:"):
                                                                    user = lines.split("user name:")

                                                                elif lines.startswith("name:"):
                                                                    Name = lines.split("name:")

                                                                elif lines.startswith("father name:"):
                                                                    father_name = lines.split("father name:")

                                                                elif lines.startswith("pin:"):
                                                                    pin2 = lines.split("pin:")


                                                                elif lines.startswith("Amount:"):
                                                                    amount = lines.split("Amount:")

                                                                    amount2 = int(amount[1]) + transfer_amount

                                                                    with open(f'{recipent_account}',"w") as f:
                                                                        g = "{"
                                                                        h = "}"
                                                                        f.write(f'{g}\nname:{Name[1]}\nfather name:{father_name[1]}\nuser name:{recipent_account}\nAmount:{str(amount2)}\npin:{pin2[1]}\n{h}')
                                                                        print("Amount Transfer successful!!")

                                                    elif transfer_amount < 0:
                                                        raise Exception("Invalid amount\nAmount should be >0")

                                                    elif transfer_amount > int(amount[1]) :
                                                        raise Exception("Low account Balance\n amount Transfer fail")

                                        break

                                else:
                                    raise Exception("NO recipent avalibel of this user name\nCheck recipent user name and try again")

                        else:
                            raise Exception("wrong password")

            break

    else:
        raise Exception("No account avalible on your this user_name\nRegister yourself")


elif args[0] == "--help":
    menu = [
        ["1", "--Register", "If you have no  Account then Register yourself by using '--Register' "],
        ["2", "--login", "If you have already Account then use '--login' for more options"],
        ]
    table = tabulate(menu, headers=["Option", "Description", "Instructions"], tablefmt="fancy_grid")
    print(table)

else:
    print("invalid syntax\nFor help use'--help")
