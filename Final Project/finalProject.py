Q = ["What's the biggest animal in the world?" , "What is the largest country in the world?" , "In which ocean is the island of Madagascar?" , "Which country has the longest coastline in the world?" , "What is the world's most populated country?" , "In which country is the world's highest waterfall?" , "What country has the greatest number of active volcanoes?" , "What is the World's Smallest Country?" , "The Sierra Madre Oriental is a mountain range in which country?" , "Where was the hottest temperature ever recorded?"]
A = ["THE BLUE WHALE" , "RUSSIA" , "INDIAN" , "CANADA" , "CHINA" , "VANEZUELA" , "INDONESIA" , "VATICAN CITY" , "MEXICO" , "DEATH VALLEY"]
answers = list()
t=0

for i in range(10):
    x = input(Q[i])
    a = x.replace("İ","I")
    answers.append(a.upper())

for j in range(10):
    if A[j] == answers[j]:
        print(Q[j],answers[j], "It's true.")
        t+=1
    else:
        print(Q[j],answers[j], "Wrong. It's :", A[j])
   

if t>5:
    print("Congrats! You got ", t*10 , "points.")
else:
    print("Upps! You failed. You got", t*10 , "points.")
