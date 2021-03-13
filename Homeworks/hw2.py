cv = {
    "Name & Surname" : "",
    "Address" : "",
    "Tel" : "",
    "Email" : "",
    "Apply for" : "",
    "Nationality" : "",
    "Sex" : "",
    "Marital Status" : "",
    "Date Of Birth" : "",
    "Place Of Birth" : "",
    "Education" : "",
    "Experience" : "",    
    }

applications = {}

for i in range(5):

    ns = input("Name & Surname : ")
    cv["Name & Surname"] = ns
    adr = input("Address : ")
    cv["Address"] = adr
    tel = int(input("Tel : "))
    cv["Tel"] = tel
    email = input("Email : ")
    cv["Email"] = email
    af = input("Apply for :")
    cv["Apply for"] = af
    nat = input("Nationality : ")
    cv["Nationality"] = nat
    sex = input("Sex : ")
    cv["Sex"] = sex
    ms = input("Marital Status : ")
    cv["Marital Status"] = ms
    db = input("Date Of Birth : ")
    cv["Date Of Birth"] = db
    pb = input("Place Of Birth : ")
    cv["Place Of Birth"] = pb
    edu = input("Education : ")
    cv["Education"] = edu
    exp = input("Experience : ")
    cv["Experience"] = exp

    applications[i] = cv.copy()

for x in applications:
    a = applications.get(x)
    for q,w in a.items():
        print(q, " : " , w)
