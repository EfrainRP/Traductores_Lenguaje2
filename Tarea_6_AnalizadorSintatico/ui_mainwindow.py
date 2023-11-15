from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)

from PySide6.QtWidgets import (QApplication, QHeaderView, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QTextEdit, QWidget)

from mainwindow_ui import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButton.clicked.connect(self.analizar)

    def analizar(self):
        text = self.ui.InputText.toPlainText()
        #self.inputText2.setPlainText(text)
        listLexico = self.analizadorLexico(text)
        self.ui.inputText2.setPlainText(self.analizadorSintatico(listLexico))
        for r in range(len(listLexico),self.ui.tableTokens.rowCount()):
            rowAct = self.ui.tableTokens.removeRow(len(listLexico))
        for r in range(len(listLexico)):
            rowAct = self.ui.tableTokens.rowCount()
            elemLexico = listLexico[r]
            print(elemLexico)
            itemLexema = QTableWidgetItem(listLexico[r]["lexema"])
            itemToken = QTableWidgetItem(listLexico[r]["token"])
            itemId = QTableWidgetItem(str(listLexico[r]["IDtoken"]))
            if rowAct<=r:
                self.ui.tableTokens.insertRow(rowAct)
                self.ui.tableTokens.setItem(r,0,itemLexema)
                self.ui.tableTokens.setItem(r,1,itemToken)
                self.ui.tableTokens.setItem(r,2,itemId)
            else: 
                self.ui.tableTokens.setItem(r,0,itemLexema)
                self.ui.tableTokens.setItem(r,1,itemToken)
                self.ui.tableTokens.setItem(r,2,itemId)

    def analizadorLexico(self, cadena0):
        elementos=[]
        estado=0
        indice=0
        cadena=cadena0+'$'
        while(indice<=(len(cadena)-1)  and estado==0):  
                lexema=''
                token='Error'
                IDtoken=-1
                while(indice<=(len(cadena)-1) and estado!=20):
                    if estado==0:
                        if(cadena[indice].isspace()):
                            estado=0
                        elif cadena[indice].isalpha() or cadena[indice]=='_':
                            estado=4
                            lexema+=cadena[indice]
                            token='ID'
                            IDtoken = 1
                        elif cadena[indice]==';':
                            estado=20
                            lexema+=cadena[indice]
                            token='Punto y coma'
                            IDtoken = 2
                        elif cadena[indice]=='$':
                            estado=20
                            lexema+=cadena[indice]
                            token='Pesos'
                            IDtoken=18
                        elif cadena[indice]=='=':
                            lexema+=cadena[indice]
                            token='Asignación'
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
                            token='Coma'
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
                            token='Error'
                            lexema=cadena[indice]
                        indice+=1
                    elif estado==4:
                        if cadena[indice].isdigit() or cadena[indice].isalpha() or cadena[indice]=='_':
                            estado=4
                            lexema+=cadena[indice]
                            token='ID'
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
                            lexema+=cadena[indice]
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
                elemento['token']="Condicional SI"
                elemento['IDtoken']= 9
            if elemento['lexema']=="else":
                elemento['token']="Else"
                elemento['IDtoken']= 12
            if elemento['lexema']=="int" or elemento['lexema']=="float" or elemento['lexema']=="char" or elemento['lexema']=="void":
                elemento['token']="Tipo de dato"
                elemento['IDtoken']= 0
            if elemento['lexema']=="while":
                elemento['token']="While"
                elemento['IDtoken']= 10
            if elemento['lexema']=="return":
                elemento['token']="Return"
                elemento['IDtoken']= 11
            #print(elemento)
        return elementos    # elementos({'IDtoken':IDtoken,'token':token,'lexema':lexema})

    def analizadorSintatico(self,lexicoAnalizado):  
        with open('Tarea_6_AnalizadorSintatico\GR2slrTable.txt','r') as archive: #Lectura del archivo de la tabla sintatica
            tableSintax = []
            for line in archive:
                line = line.strip() #Quito los '\n' de ambos lados de la cadena del renglon 
                line = list(map(int,line.split()[1::])) #Mapeo de la lista de cadena a enteros, omitiendo los espacios y el primer valor del texto, como es el numero de la fila
                tableSintax.append(line)    #se agrega una lista de la cadena 

        with open('Tarea_6_AnalizadorSintatico\GR2slrRulesId.txt','r') as archive:  #Lectura del archivo de las reglas gramaticales
            rulesID = []
            for line in archive:
                line = line.strip() #Quito los '\n' de ambos lados de la cadena del renglon
                subLine = line.split() #Elimina los espacios, metiendolos en lista
                rulesID.append([int(subLine[0]),int(subLine[1])])    #se agrega una lista de la cadena omitiendo los espacios y el primer valor del texto, como es el numero de la fila
        
        lexico = []
        for token in lexicoAnalizado:   #Guarda solo los tokens de la lista de diccionarios del LEXICO
            lexico.append(token['IDtoken'])
        
        indice = 0 #Indice para recorrer la sentencia/tabla de simbolos a analizar
        pila=[0]   #Pila del grafo para el analizador sintatico
        message = " -> Lexical Analysis completed\n\n -> Parse Error:  Syntax Error " #Inicializacion de mensaje Sintatico
        while(indice<=(len(lexico)-1)): #Ciclo para recorrer toda la sentancia a analizar
            fila = pila[-1] #Obtiene la fila del ultimo valor de la pila 
            columna = lexico[indice]   #Obtiene la columna de la tabla de simbolos para analizar con la tabla sintatico 
            accion = tableSintax[fila][columna] #Determina la accion mediante la tabla(arreglo) sintatico
            #print("tableSintaxAccion ",accion) 
            if (accion ==-1):   #Aceptara la sentencia
                message = "-> Lexical Analysis completed\n\n -> Sintax Analysis completed with no errors\n\n <> Process finished."
                break
            if (accion == 0): #Saldra del analisis, dando como error el analisis
                break  
            if (accion > 0): #Si es positivo la accion
                pila.append(lexico[indice]) #Apila el caracter de la sentencia
                indice+=1   #Recorre el caracter a analizar
                pila.append(accion) #Apila la accion positiva
            if (accion <-1): #Si es negativo la accion
                reduc = rulesID[abs(accion)-1] #Obtenemos la longitud de la regla a reducir
                for d in range(reduc[1]*2): #Desapila segun la (longitud * 2) de la regla
                    pila.pop()
                fila=pila[-1] #Guardar valor ultimo de la pila (ESTADO ANTERIOR)
                pila.append(reduc[0]) #Agregar el numero de regla a la pila
                columna=reduc[0] #Actualizar la columna con la regla

                if tableSintax[fila][columna]==0: #Si el valor de la tabla(arreglo) sintatico es 0 
                    break #continuara con el analisis
                else:
                    pila.append(tableSintax[fila][columna]) #Apila el valor resultante de la fila,columna
        return message #Regresara el mensaje resultante del analisis sintatico
    
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
