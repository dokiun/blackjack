import random, tkinter
from tkinter import Label, PhotoImage, ttk

main=tkinter.Tk()
style = ttk.Style()
style.configure("Title.Label", foreground="black", font=("Arial", 24))
style.configure("Text.Label", foreground="black", font=("Arial", 16))
player=[]

def menuJugadores():
    borrarMenu()
    pad=10
    esp=65
    global l1,l2,e1,imp2,cb1,cb2,cb3,cb4,cb5
    global boton5,boton6,boton7,boton8,boton9,boton10
    img2=PhotoImage(file="img/npcs.png")
    imp2=Label(main,image=img2)
    imp2.pack()
    l1 = ttk.Label(text="Contra cuantos NPC desea jugar:", style="Title.Label")
    l1.pack()
    boton6 = ttk.Button(text="1 NPC", command=npc1, padding=pad)
    boton6.pack()
    boton7 = ttk.Button(text="2 NPCS", command=npc2, padding=pad)
    boton7.pack()
    boton8 = ttk.Button(text="3 NPCS", command=npc3, padding=pad)
    boton8.pack()
    boton9 = ttk.Button(text="4 NPCS", command=npc4, padding=pad)
    boton9.pack()
    boton10 = ttk.Button(text="5 NPCS", command=npc5, padding=pad)
    boton10.pack()
    boton5 = ttk.Button(text="Atras", command=deJuegoaMenu, padding=pad)
    boton5.place(x=720-2*esp, y=540-(esp))

def npc1():
    borrarJugadores()
    npc, jg= numJugadores(1);
    repartir(npc,player,jg)
    turno(npc,jg)
    quienGana(jg,npc)
    jugarOtro()
def npc2():
    borrarJugadores()
    npc, jg= numJugadores(2);
    repartir(npc,player,jg)
    turno(npc,jg)
    quienGana(jg,npc)
    jugarOtro()
def npc3():
    borrarJugadores()
    npc, jg= numJugadores(3);
    repartir(npc,player,jg)
    turno(npc,jg)
    quienGana(jg,npc)
    jugarOtro()
def npc4():
    borrarJugadores()
    npc, jg= numJugadores(4)
    repartir(npc,player,jg)
    turno(npc,jg)
    quienGana(jg,npc)
    jugarOtro()
def npc5():
    borrarJugadores()
    npc, jg= numJugadores(5);
    repartir(npc,player,jg)
    turno(npc,jg)
    quienGana(jg,npc)
    jugarOtro()
    
def numJugadores(x):
    npc=[]
    for i in range(x):
        npc.append([])
    #print(f'\nSe crean las listas de los NPC vacías: {npc}\n')
    main.mainloop()
    return npc, x

def deJuegoaMenu():
    borrarJugadores()
    menu()

def borrarJugadores():
    l1.destroy()
    imp2.destroy()
    boton5.destroy();boton6.destroy();boton7.destroy();boton8.destroy();boton9.destroy();boton10.destroy(); 

def fondito():
    img7=PhotoImage(file="img/fondo.png")
    fondo=Label(main,image=img7).place(x=-7,y=-7)

def repartir(npc,player,jg):\
    # Interfaz
    esp=16
    fondito()
    for i in range(jg):
        for j in range(1):
            img5=PhotoImage(file="img/carta.png")
            fondo=Label(main,image=img5).place(x=120+i*esp,y=20)
    # Llenar listas
    #print("Empieza el juego:\n")
    for i in range(jg):
        for j in range(2):
            n=random.randint(1,11)
            npc[i].append(n)
    for i in range(2):
        n=random.randint(1,11)
        player.append(n)
    #print(f'Las cartas de los NPC: {npc}')
    #print("")
    #print(f'Las cartas del jugador son: {player}\n')
    

def sumarNPC(list): #XDD aqui me toca hacer mera inteligencia artificial
    if sum(list)==14:
        print('\nTengo 20 y media, me quedo\n')
    elif sum(list)==21:
        print('Ya tengo 21 mani\n')
    else:
        while sum(list)<18: #la tendencia es tomar una carta hasta 18, pues depues de 18 es muy facil pasarse de 21 y perder
            n=random.randint(1,11)
            list.append(n)
    #print(list)
    return list

def sumarJugador(): #el input va a ser reemplazado con botones
    if sum(player)<19:
        n=random.randint(1,11)
        player.append(n)
    else:
        sumarJugador()
    #print(player)


def quienGana(jg,npc):
    resultados=[]
    jugador=[sum(player), jg+1]
    for i in range(jg):
        resultados.append([])
    for i in range(jg):
        for j in range(1):
            resultados[i].append(sum(npc[i]))
            resultados[i].append(i+1)
    resultados.append(jugador)
    resultados.sort(reverse=True)
    print(f'\nLos resultados de la partida son: {resultados}')

    for i in range(jg+1):
        p=resultados[i][1]
        o=resultados[i][0]
        if p<jg+1:
            if o>21:
                print(f'El CPU {resultados[i][1]}, sacó {o} y se pasó')
            elif o==14:
                print(f'El CPU {resultados[i][1]} sacó 20 y media')
            elif o==21:
                print(f'El CPU {resultados[i][1]} sacó 21')
            elif o<21:
                print(f'El CPU {resultados[i][1]} sacó {o}')
        elif p==jg+1:
            if o>21:
                print(f'El Jugador, sacó {o} y se pasó')
            elif o==14:
                print(f'El Jugador sacó 20 y media')
            elif o==21:
                print(f'El Jugador sacó 21')
            elif o<21:
                print(f'El Jugador sacó {o}')

def turno(npc,jg):
    for i in range(jg):
        sumarNPC(npc[i])
    sumarJugador()

def juego():
    menuJugadores()
    
def salida():
    main.destroy()

def jugarOtro():
    x=(input("\nDesea jugar otra vez? (Y/N)\n"))
    if x=="Y" or x=="y":
        player.clear()
        juego()
    elif x=="N" or x=="n":
        salida()
    else:
        jugarOtro()

def crearVentana():
    main.geometry("720x540")
    main.title("BlackJack Criollo")
    main.resizable(False,False)
    global fondo
    img1=PhotoImage(file="img/fondo.png")
    #fondo=Label(main,image=img1).place(x=-3,y=-3)
    menu()

def menu():
    pad=10
    esp=65
    global boton1, boton2, boton3, boton4, logo
    img3=PhotoImage(file="img/logo.png")
    logo=Label(main,image=img3)
    logo.pack()
    boton1= ttk.Button(text="Jugar", command=juego, padding=pad)
    boton1.place(x=(720/2)-45, y=(540/3)+(esp))
    boton2 = ttk.Button(text="Reglas", command=reglas, padding=pad)
    boton2.place(x=(720/2)-45, y=(540/3)+(esp*2))
    boton3 = ttk.Button(text="Créditos", command=reglas, padding=pad)
    boton3.place(x=(720/2)-45, y=(540/3)+(esp*3))
    boton4=ttk.Button(text="Salir", command=salida, padding=pad)
    boton4.place(x=(720/2)-45, y=(540/3)+(esp*4))
    main.mainloop()

def borrarMenu():
    boton1.destroy();boton2.destroy();boton3.destroy();boton4.destroy();logo.destroy()

def reglas():
    borrarMenu()
    pad=10
    esp=65
    global boton5
    boton5 = ttk.Button(text="Atras", command=deReglasaMenu, padding=pad)
    boton5.place(x=720-2*esp, y=540-(esp))
    main.mainloop()

def creditos():
    borrarMenu()
    pad=10
    esp=65
    boton5 = ttk.Button(text="Atras", command=deCreditosaMenu, padding=pad)
    boton5.place(x=720-2*esp, y=540-(esp))
    main.mainloop()

def deReglasaMenu():
    boton5.destroy()
    menu()

def deCreditosaMenu():
    boton5.destroy()
    menu()

crearVentana()
main.mainloop()