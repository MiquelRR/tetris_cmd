import os
import platform
import random

class Console():
    """
    esta clase controla cuanto caracteres imprimimos en la terminal , para borrar con \b
    y hacer una pseudo pantalla, volviendo a imprimir en el mismo sitio
    """
    bold = '\033[1m'
    green = '\033[92m'
    yellow = '\033[93m'
    blue = '\033[94m'
    endcol = '\033[0m'
    cyan = '\033[96m'
    red = '\033[91m'
    low='\033[2m'
    def __init__(self) -> None:
        self.screen=""
        self.maxChar=6000
    def printConsole(self, text):

        self.screen+=str(text)
    def showScreen(self):
        print(self.screen)
    def clearDisplay(self): # Dependiendo del SO borra la pantalla de una manera u otra
        if platform.system() == "Windows":
            os.system("cls")
        elif any('jupyter' in arg for arg in platform.sys.argv):
            print('\b'*(len(self.screen)+self.screen.count("\n")))
        elif platform.system() == "Linux" or platform.system() == "Darwin":
            os.system("clear")
    def clearScreen(self):
        self.clearDisplay()
        self.screen=""
    def validateInput(self,questText,evaluableCondition=False) -> list:
        """
        validamos una input del usuario, la condicion que pongamos se evalua en referencia a la variable res
        si no es válido "borramos" y volvemos a preguntar, la funcion devuelve una variable o una lista si hay comas
        ejemplos de paramentros para evaluableCondition=
        'res.isdigit' ,
        'res.split(",")[0].isalpha() and res.split(",")[1].isdigit() and int(res.split(",")[1]) in range(0,14)'
        'res=isalpha()
        """
        dev=[]
        while True:
            self.clearDisplay()
            self.showScreen()
            print(questText)
            res=input(">")
            try:
                if eval(evaluableCondition):
                    res=res.split(",")
                    for l in res:
                        dev.append(int(l) if l.strip().isdigit() else l.strip())
                    self.clearDisplay()
                    print(dev, dev[0])
                    return dev if len(dev)>1 else dev[0] #una lista, si el string lleva comas
                else:
                    pass
            except Exception:
                pass

class Piece():
    """
    clase que maneja fichas aleatorias

    """
    cubo=((1,1),(1,1))
    barra=((1,1,1,1),)
    zeta=((1,1,0),(0,1,1))
    ese=((0,1,1),(1,1,0))
    gancho=((1,1,1),(0,0,1))
    ganchoR=((1,1,1),(1,0,0))
    peine=((1,1,1),(0,1,0))
    ele=((1,1),(0,1))

    piece_set=[cubo,barra,zeta,ese,gancho,ganchoR,peine,ele]

    def __init__(self) -> None:
        self ._piece=()

    def rnd_choice(self):
        self._piece=random.choice(self.piece_set)

    def __str__(self) -> str:
        tx=""
        for line in self._piece:
            for col in line:
                ch="██" if col else "  "
                tx+=ch
            tx+="\n"
        return tx

    @property
    def shape(self):
        return self._piece

    @shape.setter
    def shape(self, sh):
        self._piece=sh

    def rotate(self):
        rot_piece=[]
        for lin in range(len(self._piece[0])-1,-1,-1): #ange(len(self._piece[0])-1,-1,-1):
            r_lin=[]
            for col in range(len(self._piece)):
                r_lin.append(self._piece[col][lin])
            rot_piece.append(r_lin)
        self.shape=rot_piece

    @property
    def width(self):
        #devuelve el ancho de la pieza
        return len(self._piece[0])

    @property
    def height (self):
        #devuelve el alto de la pieza
        return len(self._piece)



class Board():
    """
    Clase que contiene un tablero y maneja su representación
    self.board es una matriz con 0-> Vacio 1-> pieza movil 3-> pieza fijada 4-> colisión
    """
    def __init__(self,con)  -> None:
        self.con=con
        self.width=10
        self.height=10
        self.board = [[0]*self.width for i in range(self.height)]
        self.score=0
        self.graphics=("  ",self.con.yellow+"██"+self.con.endcol, self.con.cyan+"██"+self.con.endcol , self.con.red+"██"+self.con.endcol)
        self.empty, self.on_move, self.fixed,self.collision=0,1,2,3 # estados de piezas en tablero, corresponde con indices de self.graphics

    def showBoard(self):
        """
        Imprime por terminal el tablero
        """
        gameTitle=f"{self.con.cyan}╔════════════╗╔═══════╗\n║ {self.con.blue}TETRIS CMD {self.con.cyan}║║{self.con.green}SCO:{self.score:03d}{self.con.cyan}║\n╚════════════╝╚═══════╝\n{self.con.endcol}"
        self.con.clearScreen()
        self.con.printConsole(gameTitle)
        self.con.printConsole(self.con.cyan+"╔═"+"══"*self.width+"╗\n"+self.con.endcol)

        for lin in self.board:
            self.con.printConsole(self.con.cyan+"║ ")
            for ele in lin:
                self.con.printConsole(self.graphics[ele]+self.con.endcol)
            self.con.printConsole(self.con.cyan+"║\n"+self.con.endcol)
        self.con.printConsole(self.con.cyan+"╚═"+"══"*self.width+"╝\n"+self.con.endcol)

    def change(self,a,b): #helper que substituye valor a en la ocurrencias de valor b en la matriz board
        self.board = [[b if x==a else x for x in line] for line in self.board]

    def clear_float(self):import os
import platform
import random

class Console():
    """
    esta clase controla cuanto caracteres imprimimos en la terminal , para borrar con \b
    y hacer una pseudo pantalla, volviendo a imprimir en el mismo sitio
    """
    bold = '\033[1m'
    green = '\033[92m'
    yellow = '\033[93m'
    blue = '\033[94m'
    endcol = '\033[0m'
    cyan = '\033[96m'
    red = '\033[91m'
    low='\033[2m'
    def __init__(self) -> None:
        self.screen=""
        self.maxChar=6000
    def printConsole(self, text):

        self.screen+=str(text)
    def showScreen(self):
        print(self.screen)
    def clearDisplay(self): # Dependiendo del SO borra la pantalla de una manera u otra
        if platform.system() == "Windows":
            os.system("cls")
        elif any('jupyter' in arg for arg in platform.sys.argv):
            print('\b'*(len(self.screen)+self.screen.count("\n")))
        elif platform.system() == "Linux" or platform.system() == "Darwin":
            os.system("clear")
    def clearScreen(self):
        self.clearDisplay()
        self.screen=""
    def validateInput(self,questText,evaluableCondition=False) -> list:
        """
        validamos una input del usuario, la condicion que pongamos se evalua en referencia a la variable res
        si no es válido "borramos" y volvemos a preguntar, la funcion devuelve una variable o una lista si hay comas
        ejemplos de paramentros para evaluableCondition=
        'res.isdigit' ,
        'res.split(",")[0].isalpha() and res.split(",")[1].isdigit() and int(res.split(",")[1]) in range(0,14)'
        'res=isalpha()
        """
        dev=[]
        while True:
            self.clearDisplay()
            self.showScreen()
            print(questText)
            res=input(">")
            try:
                if eval(evaluableCondition):
                    res=res.split(",")
                    for l in res:
                        dev.append(int(l) if l.strip().isdigit() else l.strip())
                    self.clearDisplay()
                    print(dev, dev[0])
                    return dev if len(dev)>1 else dev[0] #una lista, si el string lleva comas
                else:
                    pass
            except Exception:
                pass

class Piece():
    """
    clase que maneja fichas aleatorias

    """
    cubo=((1,1),(1,1))
    barra=((1,1,1,1),)
    zeta=((1,1,0),(0,1,1))
    ese=((0,1,1),(1,1,0))
    gancho=((1,1,1),(0,0,1))
    ganchoR=((1,1,1),(1,0,0))
    peine=((1,1,1),(0,1,0))
    ele=((1,1),(0,1))

    piece_set=[cubo,barra,zeta,ese,gancho,ganchoR,peine,ele]

    def __init__(self) -> None:
        self ._piece=()

    def rnd_choice(self):
        self._piece=random.choice(self.piece_set)

    def __str__(self) -> str:
        tx=""
        for line in self._piece:
            for col in line:
                ch="██" if col else "  "
                tx+=ch
            tx+="\n"
        return tx

    @property
    def shape(self):
        return self._piece

    @shape.setter
    def shape(self, sh):
        self._piece=sh

    def rotate(self):
        rot_piece=[]
        for lin in range(len(self._piece[0])-1,-1,-1): #ange(len(self._piece[0])-1,-1,-1):
            r_lin=[]
            for col in range(len(self._piece)):
                r_lin.append(self._piece[col][lin])
            rot_piece.append(r_lin)
        self.shape=rot_piece

    @property
    def width(self):
        #devuelve el ancho de la pieza
        return len(self._piece[0])

    @property
    def height (self):
        #devuelve el alto de la pieza
        return len(self._piece)



class Board():
    """
    Clase que contiene un tablero y maneja su representación
    self.board es una matriz con 0-> Vacio 1-> pieza movil 3-> pieza fijada 4-> colisión
    """
    def __init__(self,con)  -> None:
        self.con=con
        self.width=10
        self.height=10
        self.board = [[0]*self.width for i in range(self.height)]
        self.score=0
        self.graphics=("  ",self.con.yellow+"██"+self.con.endcol, self.con.cyan+"██"+self.con.endcol , self.con.red+"██"+self.con.endcol)
        self.empty, self.on_move, self.fixed,self.collision=0,1,2,3 # estados de piezas en tablero, corresponde con indices de self.graphics

    def showBoard(self):
        """
        Imprime por terminal el tablero
        """
        gameTitle=f"{self.con.cyan}╔════════════╗╔═══════╗\n║ {self.con.blue}TETRIS CMD {self.con.cyan}║║{self.con.green}SCO:{self.score:03d}{self.con.cyan}║\n╚════════════╝╚═══════╝\n{self.con.endcol}"
        self.con.clearScreen()
        self.con.printConsole(gameTitle)
        self.con.printConsole(self.con.cyan+"╔═"+"══"*self.width+"╗\n"+self.con.endcol)

        for lin in self.board:
            self.con.printConsole(self.con.cyan+"║ ")
            for ele in lin:
                self.con.printConsole(self.graphics[ele]+self.con.endcol)
            self.con.printConsole(self.con.cyan+"║\n"+self.con.endcol)
        self.con.printConsole(self.con.cyan+"╚═"+"══"*self.width+"╝\n"+self.con.endcol)

    def change(self,a,b): #helper que substituye valor a en la ocurrencias de valor b en la matriz board
        self.board = [[b if x==a else x for x in line] for line in self.board]

    def clear_float(self):
        self.change(self.on_move,self.empty)

    def fix_float(self):
        """
        substituye las ocurrencias de self.on_move por self.fix en el tablero
        """
        self.change(self.on_move,self.fixed)

    def place(self, p:Piece) -> bool:
        """
        Coloca la pieza en el cursor, y devuelve colisión si la hubiese o si se sale
        """
        coll =  self.cur_x+p.width > self.width or self.cur_y+p.height > self.height or self.cur_x<0
        # "si no se sale del tablero"
        self.clear_float()
        if not coll:
            for yp, lin  in enumerate(p.shape):
                for xp,p in enumerate(lin):
                    if p==1 :
                        if self.board[self.cur_y+yp][self.cur_x+xp] == self.empty :
                            self.board[self.cur_y+yp][self.cur_x+xp] = self.on_move
                        else:
                            #self.board[yp][self.cur_x+xp] = self.collision
                            coll=True
        return coll



    def place_new(self, p : Piece)-> bool:
         """
         coloca una pieza en la posición inicial en el tablero, y devuelve colisión si la hubiese
         """
         self.cur_x=(self.width-p.width)//2
         self.cur_y=0
         return self.place(p)



    def move(self, p : Piece, direction = 'down') -> bool :
        """
        Desplaza una ficha izquierda, derecha o abajo si es posible
        Devuelve True si la pieza se congela
        """
        coll=False
        back_x,back_y=self.cur_x,self.cur_y
        self.cur_y+=1
        if direction=="rotate":
            rp=Piece()
            rp.shape=p.shape
            rp.rotate()
            if self.place(rp):
                if self.place(p):  #si no se puede colocar, rectificamos tambien el eje "y" y congelamos la pieza
                    self.cur_y=back_y
                    self.place(p)
                    self.fix_float()
                    coll=True
            else: #si se puede colocar cambiamos la pieza por la rotada
                p.shape=rp.shape

        else:
            if direction=="right":
                self.cur_x+=1
            if direction=="left":
                self.cur_x-=1
            if direction=="down":
                pass
            if self.place(p):  #si no se puede colocar, rectificamos x y probamos
                self.cur_x=back_x
                if self.place(p):  #si no se puede colocar, rectificamos tambien el eje "y" y congelamos la pieza
                    self.cur_y=back_y
                    self.place(p)
                    self.fix_float()
                    coll=True

        return coll
2224


"""
TETRIS PARA LINEA DE COMANDOS
PRACTICA DE POO2
"""

ky={4:"left", 6:"right", 2: "down" ,8:"rotate"}

scr=Console()
b=Board(scr)
new_piece=True



while True:
    if  new_piece:
        p=Piece()
        p.rnd_choice()
        new_piece=False
        if b.place_new(p): #si hay colision al poner pieza nueva, se acabó
            b.showBoard()
            scr.showScreen()
            break
    b.showBoard()
    user_mov=scr.validateInput("4 <  6 >  2 \/  8(Rotate)", "res in ['4','6','2','8']")
    new_piece=b.move(p,ky[user_mov])