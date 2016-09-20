import re
import hashlib
from datetime import datetime


def putLogPas(count, login, password, time):
    logdata = open("Login.txt", 'a')
    timedata = open("TimeData.txt", 'a')
    hashdata = open("HashResults.txt", 'a')

    logdata.write(count + ':' + login + '\n')
    timedata.write(count + ':' + time + '\n')
    hash_par = password + time
    hashres = hashlib.sha1(hash_par.encode("utf-8")).hexdigest()
    hashdata.write(count + ":" + hashres + '\n')
    print("You signed in.")

    logdata.close()
    timedata.close()
    hashdata.close()

def checkLogPas(login, password):
    logdata = open("Login.txt", 'r')
    timedata = open("TimeData.txt", 'r')
    hashdata = open("HashResults.txt", 'r')

    number = "0"

    scan = re.compile('\d*:')
    sec_scan = re.compile(login)
    third_scan = re.compile('\d*:\d*:\d*')
    # fourth_scan = re.compile('\d*:')
    line = logdata.readline()
    while line:
        if scan.search(line):
            result = line[(scan.search(line).end()):(len(line) - 1)]
        # print("search = " + sec_scan.search(line))
        if result == login:
            number = line[scan.search(line).start():(scan.search(line).end()-1)]
            break
        line = logdata.readline()



    if(number != "0"):
        line = timedata.readline()
        while line:
            if number == line[scan.search(line).start():(scan.search(line).end()-1)]:
                time = line[(scan.search(line).end()):(len(line)-1)]
                break
            line = timedata.readline()
        line = hashdata.readline()
        while line:
            if number == line[scan.search(line).start():(scan.search(line).end()-1)]:
                datahash = line[scan.search(line).end():(len(line)-1)]
                break
            line = hashdata.readline()

        checkhash = password + time
        if datahash == hashlib.sha1(checkhash.encode("utf-8")).hexdigest():
            print("You logged in. Congratulation!!!")
        else:
            print("Wrong login or password.")
        logdata.close()
        timedata.close()
        hashdata.close()
    else:
        print("Wrong login or password.")
        logdata.close()
        timedata.close()
        hashdata.close()


while True:
    print("Choose the action you are going to do:")
    print("1. Log in;")
    print("2. Sign in;")
    print("3. Exit.")
    choice = input("Your choice -> ")
    if choice == "1":
        login = input("Input your login: ")
        password = input("Input your password: ")
        checkLogPas(login, password)
    elif choice == "2":
        scanner = re.compile(r'\n')
        logdata = open("Login.txt", 'r')
        line = logdata.readline()
        count = 1
        while line:
            if scanner.search(line):
                count = count + 1
            line = logdata.readline()
        count = str(count)
        login = input("Input your login: ")
        password = input("Input your password: ")
        timenow = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
        putLogPas(count, login, password, timenow)
    elif choice == "3":
        break
    else:
        print("Wrong choice!!!")
