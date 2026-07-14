#----------------------------LOOP-----------------------------------------
# 1- while: 

x = 0
while x <= 10 :

    print(x)

    x += 1

# 2- while else:

u = -1
while u < 20 :

    print(u)

    u += 1

else :
    print("Loop Is Done!")

#---------------------------------------------------------------------------------------------------------

#==============Project============================================

thetop10 = ["Messi","Ronaldo","Nymar","Salah","Haland","Kan","Yamal","Van Dijk","Arnold","Mbappe`"]

i = 0

while i < len(thetop10) :

    print(f"#{str(i+1).zfill(2)} {thetop10[i]}")

    i +=1

else :
    print(f"The Ballon D'or Winner Is : #1 {thetop10[0]}")

#-------------------------------------------------------------------------------------

#-------------FOR AND ELSE-----------------------------------------------
myfriends = ["Ahmed","Mohamed","Yusef","Mostafa","Aya"]

for friend in myfriends :

    print(friend)

else :
    print("Loop Is Finished".center(22,"#"))

#-------------------------------------------------------------------------

# # Range()
# numbers = range(1,101)

# for number in numbers :

#     print(number)

#--------------------------------------------------
bestplayer = {
    "Real Madrid" : "Mbappe`",
    "Barcelona" : "Lamin yamal",
    "Liverpool" : "Virgil Van Dijk",
    "Arsenal" : "Bukayo Saka",
    "PSG" : "Ousmane Dembe`le`",
    "Man City" : "Erling Haaland"
}
bestplayer.update({"AC Mila" : "Rafael Leão"})
bestplayer["Man United"] = "Bruno Fernandes"

for player in bestplayer :

    print(f"The Best Player In {player} Is: {bestplayer[player]}")

else :  
    print("3mhm Klhm Leonel Messi".center(32,'#'))

#---------------------------------------------------------------------------------------

#====================project============================================

Data = {
    "Ahmed" : {
        "ID" : 100,
        "Collage" : "Engineering",
        "Grade" : 3.2,
        "Level" : 4,
        "CHours" : '110 h'
    },

    "Mohamed" : {
        "ID" : 101,
        "Collage" : "Bussines" ,
        "Grade" : 2.5 ,
        "Level" : 3 ,
        "CHours" : '90 h'
    },

    "Osama" : {
        "ID" : 102,
        "Collage" : "CS",
        "Grade" : 3.5,
        "Level" : 4,
        "CHours" : '117 h'
    },

    "Hossam" : {
        "ID" : 103,
        "Collage" : "Medicine",
        "Grade" : 3.1,
        "Level" : 6,
        "CHours" : '200 h'
    },
    
    }

for student in Data :

    print(student)

    for info in Data[student] :

        print(f"- {info}: {Data[student][info]}")

#---------------------------------------------------------------------------

# Continue

mylist = [1,2,3,4,5,6,7,8,9,10]

for number in mylist :

    if number % 2 != 0 :

        continue

    print(number)

print('#' * 50)

# Break

my2list = [0,1,2,3,11,22,33,111,222,333,1111,2222,3333]

for number2 in my2list :

    if number2 == 3333 :

        break

    print(number2)

print('#' * 50)

# Pass

my3list = [0,9,8,7,6,5,4,3,2,1]

for number3 in my3list :

    if number3 == 4 :

        pass

    print(number3)

#---------------------------------------------------------------------------------------

#==================project=================================================

Data = {
    "Ahmed" : {
        "ID" : 100,
        "Collage" : "Engineering",
        "Grade" : 3.2,
        "Level" : 4,
        "CHours" : '110 h'
    },

    "Mohamed" : {
        "ID" : 101,
        "Collage" : "Bussines" ,
        "Grade" : 2.5 ,
        "Level" : 3 ,
        "CHours" : '90 h'
    },

    "Osama" : {
        "ID" : 102,
        "Collage" : "CS",
        "Grade" : 3.5,
        "Level" : 4,
        "CHours" : '117 h'
    },

    "Hossam" : {
        "ID" : 103,
        "Collage" : "Medicine",
        "Grade" : 3.1,
        "Level" : 6,
        "CHours" : '200 h'
    },
    
    }
    

for name in Data :

    print(name)

    for child_key , child_value in Data[name].items() :

        print(f"- {child_key}: {child_value}")

#----------------------------------------------------------------------

#------------FUNCTIONS------------------------------------------------------

# Def Function :

def first_function () :
    print("Hello From My First Function In Python ")

first_function()

def second_function () :
    return "Hello From My Second Function In Python"

var = second_function()
print(var)

# Parameters & Arguments: 

def say_hello (name) :
    return (f"Hello {name}")

print(say_hello("Sief"))


def even_numbers (numbers) :
    for num in numbers :
        if num % 2 == 0 :
            print(str(num).zfill(3))
        else :
            continue
    
even_numbers(range(1,101))

# Packing And UnPacking Arguments :

def say_hello (*names) :

    for name in names :
        print(f"Hello '{name}'")


say_hello("Sief","Ramy","Fady","Tawfeek","Galal")

#===================project==========================================

loserlist = ["Nader","Ahmed","Ramy","Jhon"]
winnerlist = ["Sief","Sawy","I""brahim","Salah","Zizo","Mostafa"]



def Players (*mans) :
    for man in mans :
        if man in loserlist :
            print(f"Unfortunately '{man}', You Lost.")
        elif man in winnerlist :
            print(f"Congratulation '{man}', You Won.")
        else :
            print(f"Sorry {man}, You Are Not A Participant.")


name = input("Enter Your Name: ").strip().capitalize()
Players(name)

#-------------------------------------------------------------------

# Default Parameters 

def data (name = 'Unknown',age = 'Unknown',country = 'UnKnown') :
    print(f"Hello {name.strip().title()}, Your Age Is {str(age).strip()} And Your Country Is {country.strip().title()}")

data("Sief",20,"egypt")

#------------------------------------------------------------------------------

def repeat (stri) :

    print(stri.strip().capitalize())

condition = True

while condition :

    name = input("Enter Your Name: ")

    if not name.strip().isalpha() : 

        print("Wrong Name, Try Again")


    else : 

        repeat(name)

        condition = False

# Packing & UnPacking Agrguments (**Keyword Arguments)

def MySkills (*skills) :

    print("Your Skills Is : ")
    
    for skill in skills :

        print(f"- {skill}")

MySkills("Python","C","PS","Run")

friends = {
    "Ahmed" : 2005,
    "Mona" : 2000,
    "Samih" : 2004
}

def BirthYears (**years) :

    for name_key , year_value in years.items() :

        print(f"# {name_key} : {year_value}")

friends.update({"Sief" : 2005})

BirthYears(**friends)

#-----------------------------------------------------------------------------------------------
