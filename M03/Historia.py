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
# def checkUserbdd(user,password)
# def setIdGame()
# def insertCurrentChoice(idGame,actual_id_step,id_answer)
# def formatText(text,lenLine,split)
# def getHeader(text)
# def getFormatedBodyColumns(tupla_texts,tupla_sizes,margin=0)
# def getFormatedAdventures(adventures)
# def getFormatedAnswers(idAnswer,text,lenLine,leftMargin)
# def getHeadeForTableFromTuples(t_name_columns,t_size_columns,title="")
# def getTableFromDict(tuple_of_keys,weigth_of_columns,dict_of_data)
# def getFormatedTable(queryTable,title="")
# def checkPassword(password)
# def checkUser(user)
# def replay(choices)

print("                        _           __           ______    __              ____    ")
print("    ____  _________    (_)__  _____/ /_____     / ____/___/ /__  ____     / __ \____  __")
print("   / __ \/ ___/ __ \  / / _ \/ ___/ __/ __ \   / __/ / __  / _ \/ __ \   / / / / __ \/ _ \ ")
print("  / /_/ / /  / /_/ / / /  __/ /__/ /_/ /_/ /  / /___/ /_/ /  __/ / / /  / /_/ / / / /  __/")
print(" / .___/_/   \____/_/ /\___/\___/\__/\____/  /_____/\__,_/\___/_/ /_/   \____/_/ /_/\___/")
print("/_/              /___/    ")
print("")

def getUsers():
    cur = conn.cursor()
    query = f"select * from usuario "
    cur.execute(query)
    rows = cur.fetchall()
    dictuser= {}
    for i in rows:
        dictuser[i[1]]= {"password":i[2],"Id":i[0]}
    return dictuser

def loginUser(loginName,loginPassword):
    resultado = 0
    for i in getUsers():
        if i == loginName:
            for x in getUsers():
                if getUsers()[x]["Password"] == loginPassword:
                    resultado = 1
                else:
                    resultado = 0
        else:
            resultado = 0
    return resultado
#
# def userExists(loginName):
#     for i in getUsers():
#         if i == loginName:
#             return 1
#         else:
#          return 0

menulogin = False

def historia():
    menuprincipal = True

    menulogin1 = False
    menuCreate = False
    #Loguearse a la base de datos
    while menuprincipal:
        print("1)Login\n2)Create user\n3)show adventure\n4)Exit")
        op = input("elige tu opción:\n")
        if len(op)<1 or len(op)>4:
            input("Invalid")
            print()
            print()
        elif op.isalpha():
            input("Invalid")
            print()
            print()
        else:
            op = int(op)
            if op == 1:
                menuprincipal = False
                menulogin = True
                while menulogin:
                    loginName = input("Username:")
                    loginPassword = input("password")
                    if loginUser(loginName,loginPassword) == 1:
                        menulogin = False
                        menulogin1 = True
                        while menulogin1:
                            print()
                    else:
                        print("usuario no  valido")


print(historia())
