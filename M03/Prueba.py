import pymysql
#Establecer Conexion
conn=pymysql.connect(host='13.81.254.185', user='jooao', password='password',db='EDEN_ONE')


def getUsers():
    cur = conn.cursor()
    query = f"select * from usuario "
    cur.execute(query)
    rows = cur.fetchall()
    dictuser= {}
    for i in rows:
        dictuser[i[1]]= {"Password":i[2],"Id":i[0]}
    return dictuser

print(getUsers())


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

def userExists(loginName,loginPassword):
    for i getUsers():
        resultadp = 0
        if i == loginName:


print(loginUser("joao","1234567"))
