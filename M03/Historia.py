import pymysql
#Establecer Conexion
conn=pymysql.connect(host='13.80.242.131', user='jooao', password='password',db='EDEN_ONE')


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
# def userExists(user)
# def replay(choices)
#
def historia():
    while True:
        #Loguearse a la base de datos
        print("1)Login\n2)Create user\n3)show adventure")
        opc = input("Option:")
        def getOpt(opc):
            lista= [1,2,3,4]
            for opc in  lista:
                if opc == lista:
                    

historia()