from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(792, 558)
        icon = QIcon()
        icon.addFile(u"Tarea_6_AnalizadorSintatico\interfaz\PNG\image.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.lexico = QWidget(MainWindow)
        self.lexico.setObjectName(u"lexico")
        self.pushButton = QPushButton(self.lexico)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(360, 60, 81, 41))
        self.pushButton.clicked.connect(self.analizar)
        self.tableTokens = QTableWidget(self.lexico)
        self.tableTokens.setObjectName(u"tableTokens")
        self.tableTokens.setColumnCount(3)
        self.tableTokens.setRowCount(0)
        
        header = self.tableTokens.horizontalHeader()
        headerRow = self.tableTokens.verticalHeader()
        font = QFont()
        font.setBold(True)
        header.setFont(font)
        headerRow.setFont(font)
        self.tableTokens.setHorizontalHeaderLabels(["Lexemas","Tokens","Numero"])
        self.tableTokens.setGeometry(QRect(20, 310, 741, 221))

        self.InputText = QTextEdit(self.lexico)
        self.InputText.setObjectName(u"InputText")
        self.InputText.setGeometry(QRect(30, 20, 281, 271))
        self.inputText2 = QTextEdit(self.lexico)
        self.inputText2.setObjectName(u"inputText2")
        self.inputText2.setGeometry(QRect(480, 20, 281, 271))
        MainWindow.setCentralWidget(self.lexico)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Analizar", None))
    # retranslateUi

    def analizar(self):
        text = self.InputText.toPlainText()
        #self.inputText2.setPlainText(text)
        listLexico = self.analizadorLexico(text)
        self.inputText2.setPlainText(self.analizadorSintatico(listLexico))
        for r in range(len(listLexico),self.tableTokens.rowCount()):
            rowAct = self.tableTokens.removeRow(len(listLexico))
        for r in range(len(listLexico)):
            rowAct = self.tableTokens.rowCount()
            elemLexico = listLexico[r]
            print(elemLexico)
            if rowAct<=r:
                self.tableTokens.insertRow(rowAct)
                self.tableTokens.setItem(r,0,QTableWidgetItem(listLexico[r]["lexema"]))
                self.tableTokens.setItem(r,1,QTableWidgetItem(listLexico[r]["token"]))
                self.tableTokens.setItem(r,2,QTableWidgetItem(str(listLexico[r]["IDtoken"])))
            else: 
                self.tableTokens.setItem(r,0,QTableWidgetItem(listLexico[r]["lexema"]))
                self.tableTokens.setItem(r,1,QTableWidgetItem(listLexico[r]["token"]))
                self.tableTokens.setItem(r,2,QTableWidgetItem(str(listLexico[r]["IDtoken"])))
        

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

        #print("lexico ",lexico)        
        '''fila = pila[-1]
        columna = lexico[indice]   #lexico[cont]
        accion = int(tableSintax[fila][columna])
        print("fila ",fila)
        print("columna ",columna)
        print("tableSintaxAccion ",accion) #-2'''
        
        indice = 0
        pila=[0]
        message = "Analisis sintatico FALLIDA"
        while(indice<=(len(lexico)-1)):
            fila = pila[-1]
            columna = lexico[indice]   #lexico[cont]
            '''print("pila ", pila)
            print("fila ", fila, type(fila))'''
            accion = tableSintax[fila][columna]
            #print("tableSintaxAccion ",accion) 
            if (accion ==-1):   #Aceptar
                message = "Analisis sintatico EXITOSA"
                break
            if (accion == 0): #Salir error
                break  

            if (accion > 0):
                pila.append(lexico[indice])
                indice+=1
                pila.append(accion)
            if (accion <-1):
                reduc = rulesID[abs(accion)-1]
                for d in range(reduc[1]*2):
                    pila.pop()
                fila=pila[-1] #Guardar valor ultimo de la pila ESTADO ANTERIOR
                pila.append(reduc[0]) #Agregar regla a la pila
                columna=reduc[0] #Actualizar 

                if tableSintax[fila][columna]==0:
                    break
                else:
                    pila.append(tableSintax[fila][columna])
        return message

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
