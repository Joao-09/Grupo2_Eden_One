import pymysql
#Establecer Conexion
conn=pymysql.connect(host='13.81.254.185', user='jooao', password='password',db='EDEN_ONE')
# def get_answers_bystep_adventure()
# def get_adventures_with_chars()
# def get_id_bystep_adventure()
# def get_first_step_adventure()
# def get_characters()
# def getReplayAdventures()
# def getChoices()
# def getIdGames()
# def insertCurrentGame(idGame,idUser,isChar,idAdventure)
# def getUserIds()
# def insertUser(id, user,password)
# def get_table(query)
# def setIdGame()
# def insertCurrentChoice(idGame,actual_id_step,id_answer)
# def formatText(text,lenLine,split)
# def getFormatedBodyColumns(tupla_texts,tupla_sizes,margin=0)
# def getFormatedAdventures(adventures)
# def getFormatedAnswers(idAnswer,text,lenLine,leftMargin)
# def getHeadeForTableFromTuples(t_name_columns,t_size_columns,title="")
# def getTableFromDict(tuple_of_keys,weigth_of_columns,dict_of_data)
# def getFormatedTable(queryTable,title="")
# def replay(choices)
#Opciones del menu dentro de su rango
def getOpt(op,lista):
    resultado = 0
    for i in lista:
        # print(i)
        if op == i:
            resultado = 1
            break
        else:
            resultado = 0
    return resultado
lista = [1, 2, 3, 4]

#Mostrar toda la lista de usuarios
def getUsers():
    cur = conn.cursor()
    query = f"select * from usuario "
    cur.execute(query)
    rows = cur.fetchall()
    dictuser= {}
    for i in rows:
        dictuser[i[1]]= {"password":i[2],"Id":i[0]}
    return dictuser
# Comprobar si el usuario entra en al base de usuarios
def userExists(loginName):
    resultado = 0
    for i in getUsers():
        if i == loginName:
            return 1
        else:
         resultado = 0
    return resultado
#Comprobamos que si el usuario esta en mysql, verificar si la contraseña es la misma que tiene asignado
def loginUser(loginName,loginPassword):
    resultado = 0
    for i in getUsers():
        if i == loginName:
            for x in getUsers():
                if getUsers()[x]["password"] == loginPassword:
                    resultado = 1
                else:
                    resultado = 0
        else:
            resultado = 0
    return resultado
#Mostrar la opciones de historias
def displayAdventures():
    cur = conn.cursor()
    query = f"select * from aventura "
    cur.execute(query)
    rows = cur.fetchall()
    dictaventura = {}
    for i in rows:
        dictaventura[i[0]] = {"name": i[1],"descripcion": i[2]}
    return dictaventura

#Condicion del usuario para darle valido y continuar con la contraseña
def checkUser(creacionUser):
    resultado = 0
    while True:
        if len(creacionUser)<5 or len(creacionUser)>11:
            print("Length of username have to be longer than 5 and shorter than 11")
            resultado = 0
        if creacionUser.isalpha():
            print("there must be a number")
            resultado = 0
        else:
            resultado = 1
        return resultado
# Si la contraseña cumple con las condiciones que le pedimos
def checkPassword(creacionPassword):
    while True:
        validar = False
        numero = False
        espacio = False
        minuscula = False
        mayuscula = False
        correcto = True
        for char in creacionPassword:
            if char.isdigit() == True:
                numero = True
            if char.isspace() == True:
                espacio = True
            if char.isupper() == True:
                minuscula = True
            if char.islower() == True:
                mayuscula = True
        if espacio == True:
            print("password cannot contain spaces")
        else:
            validar = True
        if numero == False:
            print("Password has contain some digit")
        if mayuscula == False or minuscula == False:
            print("Password have to incluide some uppercas and some lowercase")
        if len(creacionPassword) < 8 or len(creacionPassword) > 12 and validar == True:
            print("Length of password is not correct")
            validar = False
        if numero == True and mayuscula == True and minuscula == True and validar == True:
            validar = True
        if validar == True and correcto == True:
            return True
        break
def insertUser(username,password):
    cur = conn.cursor()
    query = f"insert into usuario (username,password) values ('{username}','{password}')"
    cur.execute(query)
    conn.commit()
    conn.close()

def playUser():
    print(displayAdventures())
    op = input("What adventure do you want to play:\n(0 Go to back) ")

def historia():
    menuPrincipal = True
    menuLogin = False
    menuCreacion = False
    menuPrincipalUser = False
    #Menu de la Historia
    while menuPrincipal:
        print("                        _           __           ______    __              ____    ")
        print("    ____  _________    (_)__  _____/ /_____     / ____/___/ /__  ____     / __ \____  __")
        print("   / __ \/ ___/ __ \  / / _ \/ ___/ __/ __ \   / __/ / __  / _ \/ __ \   / / / / __ \/ _ \ ")
        print("  / /_/ / /  / /_/ / / /  __/ /__/ /_/ /_/ /  / /___/ /_/ /  __/ / / /  / /_/ / / / /  __/")
        print(" / .___/_/   \____/_/ /\___/\___/\__/\____/  /_____/\__,_/\___/_/ /_/   \____/_/ /_/\___/")
        print("/_/              /___/    ")
        print("")
        if menuPrincipalUser == False:
          print("1)Login")
          print("2)Create user")
          print("3)Adventure")
          print("4)Reports\n")

        else:
            print("1)Logout")
            print("2)Play")
            print("3)show Adventure")
            print("4)Reports\n")
        op = input("Elige tu opción:\n")
        #elegirimos la opciones que tenemos en el menu
        if not op.isdigit():
            print("="*10+" Invalid Option"+"="*10)
            input("Press enter to Continue")
            print()
            print()
        elif op == "1" and menuPrincipalUser == False: #Login
            getOpt(op,lista)
            menuPrincipal = False
            menuLogin = True
            while menuLogin:
                # Pedir al usuario que inserte un usuario y contraseña ya registrado en  la base de datos
                loginName = input("Username:")
                if userExists(loginName) == 1:
                    #Si el usuario insertado coincide con la base de datos pedir contraseña
                    loginPassword = input("Password:")
                    if loginUser(loginName, loginPassword) == 1:
                        print("Login correct\n")
                        print(playUser())

                    else:
                        print("El nombre de usuario no coincide con la contraseña")
                else:
                    print("Nombre de usuario no vàlido")
        else:
            print()
        if op == "1" and menuPrincipalUser == True: #Logout
            print("Has cerrado session\n")

        if op == "2" and menuPrincipalUser == True: #Play
            print("Let's go")
            print(playUser())
            break
        if op == "2" and menuPrincipalUser == False: #Create user
            menuPrincipal = False
            menuCreacion = True
            while menuCreacion and menuPrincipal == False:
                username = input("Create Username:\n")
                if checkUser(username) == True:
                    password = input("Create Password:\n")
                    if checkPassword(password) == True:
                        print("User created")
                        input("Enter to continue\n")
                        insertUser(username, password)
                        menuPrincipal = True
                        menuPrincipalUser = True
                        break
                    else:
                        print("Insert user and password")
                else:
                    print("User Invalid")

print(historia())
