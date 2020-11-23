# a function that takes client names as input and logs/retrieves data entered by the person.

def getdate():
    import datetime
    return datetime.datetime.now()


def log():
    global filename
    global task
    #write the data to the file
    with open(filename, "a") as f:
        if task == 1:
            q = input("enter the exercise done today: ")
        elif task == 2:
            q = input("enter the diet you took today: ")
        f.write("\n" + q)
        a = str(getdate())
        f.write(" - "+ a)
    return

def retrieve():
    #read the data fed into the file
    with open(filename) as f:
        print(f.read())
    return


def selection():
    #Log/retrieve
    mode = int(input("please select an input: \n1- Log \n2- Retrieve -- "))
    while mode != 1 or 2:
        if mode == 1:
            log()
            break
        elif mode == 2:
            retrieve()
            break
        mode = int(input("Invalid Input... Please select an input: \n1- Log \n2- Retrieve -- "))
    return

def mainfunc():
    global filename
    global task
    #main program starts here
    client_name = input("enter the client name: ")
    task = int(input("what do you want record/retrieve : \n1- Exercise \n2- Diet -- "))
    while task != 1 or 2:
        if task == 1:
            filename = client_name+"_exercise.txt"
            break
        elif task == 2:
            filename = client_name+"_diet.txt"
            break
        task = int(input("Invalid Input.. what do you want record/retrieve : \n1- Exercise \n2- Diet -- "))
    selection()

    return


print("______Health Management System starts here_______")
mainfunc()
