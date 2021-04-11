username = "Global AI Hub"
password = "PythonCourse"

while True:
    un = input("Please enter username : ")
    pw = input("Please enter password : ")

    if username == un and password != pw:
        print("Password wrong! Try again.")

    elif username != un and password == pw:
        print("Username wrong! Try again.")

    elif username != un and password != pw:
        print("Username and password wrong! Try again.")

    else:
        print("Successful.")
        break


# With Dictinoray
user = {
    "username" : "Global AI Hub",
    "password" : "PythonCourse",
    }

a = {}

while True:
    a.clear()
    un = input("Please enter username : ")
    a["un"] = un
    pw = input("Please enter password : ")
    a["pw"] = pw

    if user["username"] == a["un"] and user["password"] != a["pw"]:
        print("Password wrong! Try again.")

    elif user["username"] != a["un"] and user["password"] == a["pw"]:
        print("Username wrong! Try again.")

    elif user["username"] != a["un"] and user["password"] != a["pw"]:
        print("Username and password wrong! Try again.")

    else:
        print("Successful.")
        break