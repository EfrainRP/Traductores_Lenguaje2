cadena0=" var var variable1 _varae2 3_varaible varia#ble 1234243 ==   *20/20 > True if else  != 22 9@int"
cadena1="asdsadsasdadssa"
cadena2="XDXDXDXDXDXD"
cadena3="if ( n==1 ): \n\tprint(h)   else"
cadena4="1.233..."
lexicosimple=1

elementos=[]
estado=0
indice=0
cadena=cadena0+'$'
while(indice<=(len(cadena)-1)  and estado==0):  
        lexema=''
        token='error'
        IDtoken=-1
        while(indice<=(len(cadena)-1) and estado!=20):
            if estado==0:
                if(cadena[indice].isspace()):
                    estado=0
                elif cadena[indice].isalpha() or cadena[indice]=='_':
                    estado=4
                    lexema+=cadena[indice]
                    token='id'
                    IDtoken = 1
                elif cadena[indice]==';':
                    estado=20
                    lexema+=cadena[indice]
                    token='punto y coma'
                    IDtoken = 2
                elif cadena[indice]=='$':
                    estado=20
                    lexema+=cadena[indice]
                    token='pesos'
                    IDtoken=18
                elif cadena[indice]=='=':
                    lexema+=cadena[indice]
                    token='asignación'
                    IDtoken = 8
                    estado=5 
                elif cadena[indice]=='|' or cadena[indice]=='&':   
                    lexema+=cadena[indice]
                    estado=6    
                elif cadena[indice]=='<' or cadena[indice]=='>':   
                    lexema+=cadena[indice]
                    token='opRelacional'
                    IDtoken=17
                    estado=7             
                elif cadena[indice]=='!':   
                    lexema+=cadena[indice]
                    estado=8             
                elif cadena[indice].isdigit():
                    lexema+=cadena[indice]
                    token='Constante'
                    IDtoken=13
                    estado=9    
                elif cadena[indice]=='+' or cadena[indice]=='-':
                    estado=20
                    lexema+=cadena[indice]
                    token='opSuma' 
                    IDtoken=14        
                elif cadena[indice]=='*' or cadena[indice]=='/':
                    estado=20
                    lexema+=cadena[indice]
                    token='opMultiplicacion'
                    IDtoken=16         
                elif cadena[indice]==',':
                    estado=20
                    lexema+=cadena[indice]
                    token='coma'
                    IDtoken = 3         
                elif cadena[indice]=='(':
                    estado=20
                    lexema+=cadena[indice]
                    token='Parentesis Izq' 
                    IDtoken = 4        
                elif cadena[indice]==')':
                    estado=20
                    lexema+=cadena[indice]
                    token='Parentesis Der'
                    IDtoken = 5        
                elif cadena[indice]=='{':
                    estado=20
                    lexema+=cadena[indice]
                    token='Llave Izq'     
                    IDtoken = 6   
                elif cadena[indice]=='}':
                    estado=20
                    lexema+=cadena[indice]
                    token='Llave Der'    
                    IDtoken = 7    
                else:
                    estado=20
                    token='error'
                    lexema=cadena[indice]
                indice+=1
            elif estado==4:
                if cadena[indice].isdigit() or cadena[indice].isalpha() or cadena[indice]=='_':
                    estado=4
                    lexema+=cadena[indice]
                    token='id'
                    IDtoken=1
                    indice+=1
                else:
                    estado=20
            elif estado==5:
                if cadena[indice]!='=':
                    estado=20
                else:
                    estado=20
                    lexema+=cadena[indice]
                    token='opRelacional'
                    IDtoken=17
                    indice+=1
            elif estado==6:
                if cadena[indice]=='|' or cadena[indice]=='&':
                    estado=20
                    token='opLogico'
                    indice+=1
                    IDtoken=15
                else:
                    estado=20
            elif estado==7:
                if cadena[indice]!='=':
                    estado=20
                else:
                    estado=20
                    lexema+=cadena[indice]
                    token='opRelacional'
                    IDtoken=17
                    indice+=1 
            elif estado==8:
                if cadena[indice]=='=':
                    estado=20
                    lexema+=cadena[indice]
                    token='opRelacional'
                    IDtoken=17
                    indice+=1  
                else:
                    estado=20
            elif estado==9:
                if cadena[indice].isdigit():
                    estado=9
                    lexema+=cadena[indice] 
                    token='Constante'
                    IDtoken=13
                    indice+=1
                else:
                    estado=20
        estado=0
        elementos.append({'IDtoken':IDtoken,'token':token,'lexema':lexema})

for elemento in elementos:
    if elemento['lexema']=="if":
        elemento['token']="condicional SI"
        elemento['IDtoken']= 9
    if elemento['lexema']=="else":
        elemento['token']="else"
        elemento['IDtoken']= 12
    if elemento['lexema']=="int" or elemento['lexema']=="float" or elemento['lexema']=="char" or elemento['lexema']=="void":
        elemento['token']="tipo de dato"
        elemento['IDtoken']= 0
    if elemento['lexema']=="while":
        elemento['token']="while"
        elemento['IDtoken']= 10
    if elemento['lexema']=="return":
        elemento['token']="return"
        elemento['IDtoken']= 11
    if elemento['lexema']=="while":
        elemento['token']="iterativo"
        elemento['IDtoken']= 10
    if elemento['lexema']=="while":
        elemento['token']="iterativo"
        elemento['IDtoken']= 10
    print(elemento)