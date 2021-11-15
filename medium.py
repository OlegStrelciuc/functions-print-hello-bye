# define the function
def hi( lang ):
    if lang == "en":
        print("Hello!!!")
    elif lang == "ro":
        print("Salut!!!")
    elif lang == "ru":
        print("Privet!!!")
    else :
        print("Hello!!!")

def bye( lang ):
    if lang == "en":
        print("Bye!!!")
    elif lang == "ro":
        print("Pa!!!")
    elif lang == "ru":
        print("Poka!!!")
    else :
        print("Bye!!!")
# call the function
print("---------------------")
hi( "en" )
hi( "ro" )
hi( "ru" )
hi( "fr" )
print("---------------------")
bye( "en" )
bye( "ro" )
bye( "ru" )
bye( "fr" )
print("---------------------")
