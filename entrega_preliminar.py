# Librerias
from cProfile import label
from email.mime import image
import random, tkinter
from tkinter import *
from tkinter import Label, PhotoImage, ttk
from tkinter import messagebox

# Tk Inter (Menú y demás)
main=tkinter.Tk()
style = ttk.Style()
style.configure("Title.Label", foreground="black", font=("Arial", 24), background="green")
style.configure("Text.Label", foreground="black", font=("Arial", 16))
# Imagenes
img1=PhotoImage(file="img/fondo.png")
img2=PhotoImage(file="img/npc.png")
img3=PhotoImage(file="img/logo.png")

# Arreglos
player=[]
npc=[]
# Aqui se almacena las mismas cartas pero para display
dnpc=[]
dplayer=[]
# /////
global jg, tnpc, rp, rnpc1
rp=3
tnpc=0
rnpc1=3

# Crea la interfaz de Jugadores
def menuJugadores():
    borrarMenu()
    pad=10
    esp=65
    global l1,l2,e1,imp2,cb1,cb2,cb3,cb4,cb5
    global boton5,boton6,boton7,boton8,boton9,boton10
    imp2=Label(main,image=img2, background="green")
    imp2.pack()
    l1 = ttk.Label(text="Contra cuantos NPC desea jugar:", style="Title.Label")
    l1.pack()
    boton6 = ttk.Button(text="1 CPU", command=npc1, padding=pad)
    boton6.pack()
    boton7 = ttk.Button(text="2 CPUS", command=npc2, padding=pad)
    boton7.pack()
    boton8 = ttk.Button(text="3 CPUS", command=npc3, padding=pad)
    boton8.pack()
    boton9 = ttk.Button(text="4 CPUS", command=npc4, padding=pad)
    boton9.pack()
    boton10 = ttk.Button(text="5 CPUS", command=npc5, padding=pad)
    boton10.pack()
    boton5 = ttk.Button(text="Atras", command=deJuegoaMenu, padding=pad)
    boton5.place(x=720-2*esp, y=540-(esp))

def npc1():
    global npc, jg
    borrarJugadores()
    npc, jg= numJugadores(1);
    repartir(npc,player,jg)
    main.destroy()
    crearTablero()
    tablero()
def npc2():
    global npc, jg
    borrarJugadores()
    npc, jg = numJugadores(2);
    repartir(npc,player,jg)
    main.destroy()
    crearTablero()
    tablero()
def npc3():
    global npc, jg
    borrarJugadores()
    npc, jg= numJugadores(3);
    repartir(npc,player,jg)
    main.destroy()
    crearTablero()
    tablero()
def npc4():
    global npc, jg
    borrarJugadores()
    npc, jg= numJugadores(4)
    repartir(npc,player,jg)
    main.destroy()
    crearTablero()
    tablero()
def npc5():
    global npc, jg
    borrarJugadores()
    npc, jg= numJugadores(5);
    repartir(npc,player,jg)
    main.destroy()
    crearTablero()
    tablero()

# Crea las listas de los jugadores
def numJugadores(x):
    for i in range(x):
        npc.append([])
        dnpc.append([])
    print(f'\nSe crean las listas de los NPC vacías: {npc}\n')
    return npc, x

# Funcion botón Atrás 
def deJuegoaMenu():
    borrarJugadores()
    menu()

# Borra la Interfaz de menuJugadores
def borrarJugadores():
    l1.destroy()
    imp2.destroy()
    boton5.destroy();boton6.destroy();boton7.destroy();boton8.destroy();boton9.destroy();boton10.destroy(); 

# Reparte las Cartas a los NPC y los jugadores
def repartir(npc,player,jg):
    # Llenar listas
    print("Empieza el juego:\n")
    for i in range(jg):
        for j in range(2):
            n=random.randint(1,11)
            npc[i].append(n)
            dnpc[i].append(n)
    for i in range(2):
        n=random.randint(1,11)
        player.append(n)
        dplayer.append(n)

    reemplazarNPC(npc,jg)
    reemplazarPlayer(player)
    '''
    print(f'Las cartas de los NPC: {npc}\n')
    print(f'Las cartas de los NPC: {dnpc}')
    print("")
    print(f'Las cartas del jugador son: {player}\n')
    print(f'Las cartas del jugador son: {player}')
    '''
    return npc, player

def reemplazarNPC(npc,jg):
    # Para las cartas
    letras=["K", "Q", "J", 10]
    # Reemplaza por letras si 10 y por A si 1 u 11
    for i in range(jg):
        for j in range(2):
            if npc[i][j] == 10:
                y=random.choice(letras)
                dnpc[i].pop(j)
                dnpc[i].insert(j, y)
            elif npc[i][j] == 1:
                dnpc[i].pop(j)
                dnpc[i].insert(j, "A")
    '''
    print(npc)
    print(" ")
    print(dnpc)
    '''
    
def reemplazarPlayer(player):
    # Para las cartas
    letras=["K", "Q", "J"]
    
    for i in range(2):
        if player[i] == 10:
            y=random.choice(letras)
            dplayer.pop(i)
            dplayer.insert(i, y)
        elif player[i] == 1:
            dplayer.pop(i)
            dplayer.insert(i, "A")
    '''
    print(" ")
    print(player)
    print(dplayer)
    '''

# Crea la ventana de juego, después de repartir():
def crearTablero():
    global inside
    inside=tkinter.Tk()
    inside.geometry("720x640")
    inside.title("BlackJack Criollo")
    inside.resizable(False,False)
    inside.configure(background='green')

# Esta funcion asigna un simbolo a cada número o letra con su respectivo color
# si es ♤♣ es negro y si es ♥♦ rojo :D
def icono():
        iconos=["♥", "♤", "♣", "♦"]
        o=random.choice(iconos)
        if o=="♤" or o=="♣":
            color="black"
        elif o=="♥" or o=="♦":
            color="red"
        return o, color

# Esto crea el tablero como tal
def tablero():
    # Divide el tablero en 5 columnas y 6(7) filaspara acomodar todo 👍
    for r in range(6):
        for c in range(0, 5):
            cell = Label(text="", font=("Arial", 24), background="green")
            cell.grid(padx=10, pady=10, row=r, column=c)
         
    # ♥  ♤  ♣  ♦
    
    #Para ocultar la carta coloreo el fondo de Label del mismo color que la letra
    ttk.Label(text="CPU 1:", style="Title.Label", font=("Arial", 14), background="green").grid(row=0, column=0, pady=20, padx=20)
    o, color = icono()
    ttk.Label(text=f' {dnpc[0][0]} {o}\n', font=("Arial", 24), foreground=color, padding=10).grid(row=1, column=0)
    o, color = icono()
    ttk.Label(text=f' {dnpc[0][1]} {o}\n', font=("Arial", 24), foreground=color, padding=10, background=color).grid(row=2, column=0)

    if jg>=2:
        ttk.Label(text="CPU 2:", style="Title.Label", font=("Arial", 14), background="green").grid(row=0, column=1, pady=20, padx=20)
        o, color = icono()
        ttk.Label(text=f'{dnpc[1][0]} {o}\n', font=("Arial", 24), foreground=color, padding=10).grid(row=1, column=1)
        o, color = icono()
        ttk.Label(text=f'{dnpc[1][1]} {o}\n', font=("Arial", 24), foreground=color, padding=10, background=color).grid(row=2, column=1)

    if jg>=3:
        ttk.Label(text="CPU 3:", style="Title.Label", font=("Arial", 14), background="green").grid(row=0, column=2, pady=20, padx=20)
        o, color = icono()
        ttk.Label(text=f' {dnpc[2][0]} {o}\n', font=("Arial", 24), foreground=color, padding=10).grid(row=1, column=2)
        o, color = icono()
        ttk.Label(text=f' {dnpc[2][1]} {o}\n', font=("Arial", 24), foreground=color, padding=10, background=color).grid(row=2, column=2)

    if jg>=4:
        ttk.Label(text="CPU 4:", style="Title.Label", font=("Arial", 14), background="green").grid(row=0, column=3, pady=20, padx=20)
        o, color = icono()
        ttk.Label(text=f' {dnpc[3][0]} {o}\n', font=("Arial", 24), foreground=color, padding=10).grid(row=1, column=3)
        o, color = icono()
        ttk.Label(text=f' {dnpc[3][1]} {o}\n', font=("Arial", 24), foreground=color, padding=10, background=color).grid(row=2, column=3)

    if jg>=5:
        ttk.Label(text="CPU 5:", style="Title.Label", font=("Arial", 14), background="green").grid(row=0, column=4, pady=20, padx=20)
        o, color = icono()
        ttk.Label(text=f' {dnpc[4][0]} {o}\n', font=("Arial", 24), foreground=color, padding=10).grid(row=1, column=4)
        o, color = icono()
        ttk.Label(text=f' {dnpc[4][1]} {o}\n', font=("Arial", 24), foreground=color, padding=10, background=color).grid(row=2, column=4)


    ttk.Label(text="JUGADOR:", style="Title.Label", font=("Arial", 24), background="green").grid(row=0, column=5, pady=10, padx=10)
    o, color = icono()
    ttk.Label(text=f' {dplayer[0]} {o}\n', font=("Arial", 24), foreground=color, padding=10).grid(row=1, column=5)
    o, color = icono()
    ttk.Label(text=f' {dplayer[1]} {o}\n', font=("Arial", 24), foreground=color, padding=10).grid(row=2, column=5)
    
    global supremacia
    supremacia=ttk.Button(text="Turno de los CPU", command=sumarNPC, padding=5).place(x=10, y=640-(40))
    inside.mainloop()
    
# Función para que los NPC tomen cartas e intenten ganar
def sumarNPC():
    for i in range(jg):
        print(i)
        if i==0:
            proceso(npc[i],i)
        elif i==1:
            proceso(npc[i],i)
        elif i==2:
            proceso(npc[i],i)
        elif i==3:
            proceso(npc[i],i)
        elif i==4:
            proceso(npc[i],i)
    # Después de que los NPC cojan cartas se habilitan los otros botones
    ttk.Button(text="Coger carta", command=sumarJugador, padding=5).place(x=130, y=640-(40))
    ttk.Button(text="Finalizar Turno", command=menuFinal, padding=5).place(x=210, y=640-(40)) 

# Funcion complemento de la anterior, solo que aqui es para cualquier lista en caso NPC[i] pq es una matriz
def proceso(list,x):
    if sum(list)==14:
        print('')
        #print('\nTengo 20 y media, me quedo\n')
    elif sum(list)==21:
        print('')
        #print('Ya tengo 21 mani\n')
    else:
    #la tendencia es tomar una carta hasta 18, pues depues de 18 es muy facil pasarse de 21 y perder
        rnpc=3
        while sum(list)<18:
            n=random.randint(1,11)
            list.append(n)
            dnpc[x].append(n)
            o, color = icono()
            ttk.Label(text=f' {dnpc[x][len(list)-1]} {o}\n', font=("Arial", 24), foreground=color, padding=10).grid(row=rnpc, column=x)
            rnpc=rnpc+1
        # print(list)
    return list

def sumarJugador(): #el input va a ser reemplazado con botones
    if sum(player)<21:
        n=random.randint(1,11)
        player.append(n)
        if n == 10:
            letras=["K", "Q", "J", 10]
            dplayer.append(random.choice(letras))
        elif n==1 or n==11:
            dplayer.append("A")
        else:
            dplayer.append(n)
        global rp
        #print(f'el rp: {rp}')
        o, color = icono()
        ttk.Label(text=f' {dplayer[len(player)-1]} {o}\n', font=("Arial", 24), foreground=color, padding=10).grid(row=rp, column=5)
        rp=rp+1
        #print(f'EL RP: {rp}')
    elif sum(player)==21:
        # print("Tienes 21 ya")
        ttk.Label(text="Tienes 21 ya", font=("Arial", 10), foreground="red").grid(row=rp, column=5)
    elif sum(player)>21:
        ttk.Label(text=" TE PASASTE\n(PERDISTE)", font=("Arial", 10), foreground="red").grid(row=rp, column=5)
    # print(player)
    
# Al finalizar la ronda, se determinan los resultados (sumatoria)
def quienGana():
    # AQUI SE GUARDAN LOS RESULTADOS
    resultados=[]
    # AQUI SE GUARDA EL TOTAL DEL JUGADOR, CON SU IDENTIFICADOS (JG+1)
    jugador=[sum(player), jg+1]
    for i in range(jg):
        resultados.append([])
    for i in range(jg):
        for j in range(1):
            resultados[i].append(sum(npc[i]))
            resultados[i].append(i+1)
    # SE AGREGA A LA MATRIZ DE ULTIMO AL JUGADOR
    resultados.append(jugador)
    # Este método de arreglos permite organizar de mayor a menor, asi saber quien saco mas de 21 o menos
    resultados.sort(reverse=True)
    print(f'\nLos resultados de la partida son: {resultados}')
    # Resultados para imprimir
    global dresultados, ganador
    dresultados=[]
    # Condicionesen general para saber quien pasó o perdió
    for i in range(jg+1):
        # uso p para saber si es un jugador o NPC
        p=resultados[i][1]
        o=resultados[i][0]
        if p<jg+1:
            if o>21:
                print(f'El CPU {resultados[i][1]}, sacó {o} y se pasó')
                dresultados.append(f'El CPU {resultados[i][1]}, sacó {o} y se pasó ⛔ ')
            elif o==14:
                print(f'El CPU {resultados[i][1]} sacó 20 y media')
                dresultados.append(f'El CPU {resultados[i][1]} sacó 20 y media ⚠ ')
            elif o==21:
                print(f'El CPU {resultados[i][1]} sacó 21')
                dresultados.append(f'El CPU {resultados[i][1]} sacó 21 ✅ ')
            elif o<21:
                print(f'El CPU {resultados[i][1]} sacó {o}')
                dresultados.append(f'El CPU {resultados[i][1]} sacó {o}  ')
        elif p==jg+1:
            if o>21:
                print(f'El Jugador sacó {o} y se pasó')
                dresultados.append(f'El Jugador, sacó {o} y se pasó ⛔')
            elif o==14:
                print(f'El Jugador sacó 20 y media')
                dresultados.append(f'El Jugador sacó 20 y media ⚠')
            elif o==21:
                print(f'El Jugador sacó 21')
                dresultados.append(f'El Jugador sacó 21 ✅✅ ')
            elif o<21:
                print(f'El Jugador sacó {o}')
                dresultados.append(f'El Jugador sacó {o}  ')
    # print(dresultados)
    # Saber el ganador ser como:
    for i in range(jg+1):
        # print(resultados[i][0])
        n=resultados[i][0]
        if n>21:
            resultados[i][0]=0
        elif n==14:
            resultados[i][0]=20.5
        else:
            print('')
    resultados.sort(reverse=True)
    if jg+1>resultados[0][1]:
        ganador=f'CPU {resultados[0][1]}'
    elif jg+1==resultados[0][1]:
        ganador=f'El jugador, felicidades'
    else:
        ganador='Nadie ganó'
    return dresultados, ganador

def menuFinal():
    quienGana()
    for i in range(jg):
        o, color = icono()
        ttk.Label(text=f' {dnpc[i][1]} {o}\n', font=("Arial", 24), padding=10, background="white").grid(row=2, column=i)
    global entonces
    entonces=messagebox.askyesnocancel(title='Resultados', message=f'{dresultados}\n\nEn conclusión ganó: {ganador}\n\nDesea jugar otra vez? ')
    jugarOtro(entonces)
    # No sé como se pueden tener 2 ventanas de tkinter al tiempo
    # Así que tocó hacerlo con un messagebox
    '''
    outside=tkinter.Tk()
    outside.geometry("340x340")
    outside.title("Resultados")
    outside.resizable(False,False)
    outside.configure(background='white')
    for r in range(6):
        for c in range(0, 5):
            cell = outside.Label(text="", font=("Arial", 24), background="green")
            cell.grid(padx=10, pady=10, row=r, column=c)
    '''
def juego():
    menuJugadores()

def salida():
    main.destroy()

def jugarOtro(bool):
    if bool==True:
        inside.destroy()
        npc.clear()
        dnpc.clear()
        numJugadores(jg)
        global rp
        rp=3
        tnpc=0
        rnpc1=3
        player.clear()
        dplayer.clear()
        repartir(npc,player,jg)
        crearTablero()
        tablero()
    elif bool==False:
        inside.destroy()
    else:
        print('')


# Crea la ventana PRINCIPAL
def crearVentana():
    main.geometry("720x540")
    main.title("BlackJack Criollo")
    main.resizable(False,False)
    global fondo
    img1=PhotoImage(file="img/fondo.png")
    fondo=Label(main,image=img1, background="green").place(x=-3,y=-3)
    menu()

# Crea la interfaz del menu Principal
def menu():
    global pad, esp
    pad=10
    esp=65
    global boton1, boton2, boton3, boton4, logo
    #img3=PhotoImage(file="img/logo.png")
    logo=Label(main,image=img3, background="green")
    logo.pack()
    boton1= ttk.Button(text="Jugar", command=juego, padding=pad)
    boton1.place(x=(720/2)-45, y=(540/3)+(esp))
    boton2 = ttk.Button(text="Reglas", command=reglas, padding=pad)
    boton2.place(x=(720/2)-45, y=(540/3)+(esp*2))
    boton3 = ttk.Button(text="Créditos", command=creditos, padding=pad)
    boton3.place(x=(720/2)-45, y=(540/3)+(esp*3))
    boton4=ttk.Button(text="Salir", command=salida, padding=pad)
    boton4.place(x=(720/2)-45, y=(540/3)+(esp*4))
    #main.mainloop()
def reglas():
    messagebox.showinfo(message="Reglas:\n\n1.Se reparten 2 cartas a todos los jugadores, 1 es visible y la otra estará tapada hasta que finalice el juego\n\n2.La gracia es llegar a 21 o menos, si sacas mas de 21 pierdes\n\n3.Puedes quedarte con 20 y media(14 con DOS cartas)\n\n4.Gana el jugador que tenga 21 o el mayor número entre los jugadores sin pasarse de 21", title="Créditos")
def creditos():
    messagebox.showinfo(message="Facultad de Ingeniería  -  Universidad nacional de colombia\n\nCPG21 2022-1S\n\nJulian Mateo Vargas Riveros\nJuana Sofía Alvarado Neira\nJulian Barbosa Gonzales\nRicardo Velandia Cruz", title="Créditos")
# Borra la interfaz de Menú
def borrarMenu():
    boton1.destroy();boton2.destroy();boton3.destroy();boton4.destroy();logo.destroy();

crearVentana()
main.mainloop()