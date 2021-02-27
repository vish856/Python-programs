print("welcome to the Database admin program")

logoninfo={
    'vish':'all00',
    'dish':'all01',
    'lish':'all03',
    'kish':'all04',
}
username=input("Enter your username :")
if username in logoninfo.keys():
    password=input("Enter your password: ")
    if password == logoninfo[username]:
        print("Hello "+username+ "!!you are looged in")
        if username == 'kish':
            print("\n here is the cureent user data base : ")
            for key, value in logoninfo.items():
                print("username : "+key+"\t\t Password:"+value)
        else:
            password_change = input("would you like to change your passwd(yes/n0").title().strip()
            if password_change=='yes':
                new_password=input("what would like to be your password min 8 character:")
                if len(new_password)>=8:
                    logoninfo[username]=new_password
                else:
                    print(new_password+"is not the minumum eight characters.")
                print("\n"+username+"your password is "+logoninfo[username]+".")
            else:
                print("thank you, good bye.")
    else:
        print("username not in database, good bye")
