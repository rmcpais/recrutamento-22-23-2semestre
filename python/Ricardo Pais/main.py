from tkinter import *
from tkinter import messagebox
import itertools, random

class Cartas:
    def __init__(self,tamanho):
        self.tamanho = tamanho
        self.reset()
    
    def tirar_carta(self):
        carta = random.choice(self.baralhos)
        self.baralhos.remove(carta)
        return carta[0], carta[1]

    def reset(self):
        self.baralhos = list(itertools.product(range(1, 14), ["Copas", "Paus", "Ouros", "Espadas"], range(self.tamanho)))


class Jogador:
    def __init__(self, cash):
        self.cash = cash
        self.reset()

    def add_carta(self, carta):
        self.mao.append(carta)
        print(self.mao)
    
    def val_mao(self):
        val = 0
        s = 0
        for x in self.mao:
            if x[0] == 11:
                s = s + 1
            val = val + self.valor_carta(x[0])

        while val > 21 and s > 0:
            val = val - 10
            s = s - 1
        
        return val
    

    def valor_carta(self, n):
        if n == 1:
            return 11
        if n > 10:
            return 10 
        else:
            return n
        

    def ganhos(self, win):
        match win:
            case 0:
                self.cash = self.cash - self.aposta
            case 1:
                self.cash = self.cash + self.aposta
            case 2:
                self.cash = self.cash + self.aposta * 1.5
            case 4:
                self.cash = self.cash + self.aposta * 0.5

    def aposta(self, cash):
        if self.cash <= 0:
            return 0
        else:
            self.aposta = cash
    
    
    def reset(self):
        self.mao = list()
        #self.aposta = 0

    def mostrar_mao(self):
        output = ""
        for x in self.mao:
            match x[0]:
                case 1:
                    carta = "Ás"
                case 11:
                    carta = "Valete"
                case 12:
                    carta = "Dama"
                case 13:
                    carta = "Rei"
                case _:
                    carta = str(x[0])
            output += carta + " de " + str(x[1]) + ", "
        return output


class BlackJack:
    def __init__(self):
        pass

    def bjack(self, val, mao):
        if (val == 21 and len(mao)== 2):
            return 1
        else:
            return 0
    
    def bust(self, val):
        if val > 21:
            return 1
        else:
            return 0

    def win_lose(self, j_v, d_v, j_bj, d_bj):
        if j_bj or d_bj:
            if j_bj and not d_bj:
                return 2
            else:
                return 0
        elif j_v > d_v:
            return 1
        elif j_v == d_v:
            return 3
        else:
            return 0

        
def comecar():
    global menu, jogador, baralho, dealer, b
    cash = float(cash_entry.get()) #Quando tento repetir o jogo dá um erro de tipo e eu não consegui a perceber a razão
    tam = int(baralho_tam_entry.get())
    if cash > 0 and 0<tam<=8:
        jogador= Jogador(cash)
        baralho = Cartas(tam)
    else:
        jogador= Jogador(1000)
        baralho = Cartas(1)
    dealer = Jogador(0)
    b = BlackJack()
    menu = 1
    menuj.destroy()

def temp_text1(e):
    cash_entry.delete(0,"end")

def temp_text2(e):
    baralho_tam_entry.delete(0,"end")

def temp_text3(e):
    aposta_entry.delete(0,"end")


def inicio():
    j_bar.set("")
    j_val.set("")
    d_bar.set("")
    d_val.set("")
    dinheiro.set("Dinheiro: " + str(jogador.cash))

    jogador.reset()
    dealer.reset()
    baralho.reset()
    
    jogador.add_carta(baralho.tirar_carta())
    jogador.add_carta(baralho.tirar_carta())
    j_bar.set(jogador.mostrar_mao())
    j_val.set(jogador.val_mao())

    dealer.add_carta(baralho.tirar_carta())
    d_bar.set(dealer.mostrar_mao() + "Carta Desconhecida")
    d_val.set(dealer.val_mao())
    
    if b.bjack(jogador.val_mao(), jogador.mao):
        pass_but["state"] = "normal"
        j_bstate = 1
    else:
        if(jogador.cash >= jogador.aposta*2):
            dup_but["state"] = "normal"
        tirar_but["state"] = "normal"
        pass_but["state"] = "normal"
        des_but["state"] = "normal"



def final():
    estado = b.win_lose(jogador.val_mao(), dealer.val_mao(), j_bstate, d_bstate)
    jogador.ganhos(estado)
    match estado:
            case 0:
                messagebox.showinfo("BlackJack", "Perdeste")
            case 1:
                messagebox.showinfo("BlackJack", "Ganhaste")
            case 2:
                messagebox.showinfo("BlackJack", "BlackJack")
            case 3:
                messagebox.showinfo("BlackJack", "Empataste")
    aposta_but["state"] = "normal"
    aposta_entry["state"] = "normal"
    dinheiro.set("Dinheiro: " + str(jogador.cash))
    if jogador.cash <= 0:
        messagebox.showinfo("BlackJack", "Ficaste sem dinheiro")
        root.destroy()
    
    



def vez_dealer():
    dealer.add_carta(baralho.tirar_carta())
    d_bar.set(dealer.mostrar_mao())
    d_val.set(dealer.val_mao())
    if b.bjack(dealer.val_mao(), dealer.mao):
        d_bstate = 1
    else:
        while(dealer.val_mao() < 17):
            dealer.add_carta(baralho.tirar_carta())
            d_bar.set(dealer.mostrar_mao())
            d_val.set(dealer.val_mao())
            if b.bust(dealer.val_mao()):
                d_val.set("BUST")
                dealer.reset()
                final()
                return
    final()

        

def passar():
    dup_but["state"] = "disabled"
    tirar_but["state"] = "disabled"
    pass_but["state"] = "disabled"
    des_but["state"] = "disabled"
    vez_dealer()



def apostar():
    print(aposta_entry.get())
    aposta = float(aposta_entry.get())
    print(aposta)
    if jogador.cash >= aposta > 0 :
        jogador.aposta(aposta)
        aposta_but["state"] = "disabled"
        aposta_entry["state"] = "disable"
        inicio()
    else:
        aposta_entry.delete(0,"end")
        aposta_entry.insert(0, "Coloca um valor válido")


def desistir():
    jogador.ganhos(4)
    messagebox.showinfo("BlackJack", "Desististe")
    
    dup_but["state"] = "disabled"
    tirar_but["state"] = "disabled"
    pass_but["state"] = "disabled"
    des_but["state"] = "disabled"

    aposta_but["state"] = "normal"
    aposta_entry["state"] = "normal"

def tirar_carta():
    jogador.add_carta(baralho.tirar_carta())
    j_bar.set(jogador.mostrar_mao())
    j_val.set(jogador.val_mao())
    if b.bust(jogador.val_mao()):
        j_val.set("BUST")
        jogador.reset()
        final()

def duplicar():
    jogador.aposta = jogador.aposta * 2
    jogador.add_carta(baralho.tirar_carta())
    j_bar.set(jogador.mostrar_mao())
    j_val.set(jogador.val_mao())
    if b.bust(jogador.val_mao()):
        j_val.set("BUST")
        jogador.reset()
        final()
    passar()


menu = 0
menuj = Tk()
menuj.title('Blackjack')

menuj.geometry('800x600')
menuj.configure(background = "green")
menup_frame = Frame(menuj, bg='green')
menup_frame.pack(pady=20)

menu_frame = LabelFrame(menup_frame, text = "                 BlackJack", bd = 0, width= 200, bg = "green")
menu_frame.grid(row=0, column= 0, pady= 10, ipady=10)

cash_entry = Entry(menup_frame)
cash_entry.grid(row= 1, column=0)
cash_entry.insert(0,"Dinheiro inicial")

baralho_tam_entry= Entry(menup_frame)
baralho_tam_entry.grid(row= 2, column=0)
baralho_tam_entry.insert(0, "Nº de baralhos (max= 8)")

cash_entry.bind("<FocusIn>", temp_text1)
baralho_tam_entry.bind("<FocusIn>", temp_text2)

comecar_but = Button(menup_frame, text="Click Here", command=comecar)
comecar_but.grid(row=3,column=0)

menuj.mainloop()



if menu:
    global j_val, j_bar, d_val, d_bar, j_bstate, d_bstate
    j_bstate = 0
    d_bstate = 0

    root = Tk()
    root.title('Blackjack')
    root.geometry('800x600')
    root.configure(background = "green")
    main_frame = Frame(root, bg='green')
    main_frame.pack(pady=20)

    j_bar = StringVar(root, "")
    j_val = StringVar(root, "")
    d_bar = StringVar(root, "")
    d_val = StringVar(root, "")
    dinheiro = StringVar(root, jogador.cash)

    aposta_entry= Entry(main_frame)
    aposta_entry.grid(row= 0, column=2)
    aposta_entry.insert(0, "Aposta")
    aposta_entry.bind("<FocusIn>", temp_text3)

    aposta_but = Button(main_frame, text = "apostar", command= apostar)
    aposta_but.grid(row=1, column=2, ipady = 10)
    


    dealer_frame = LabelFrame(main_frame, text = "Dealer", bd = 0)
    dealer_frame.grid(row=0, column=0, pady= 10, ipady = 10)

    jog_frame = LabelFrame(main_frame, text= "Jogador", bd=0)
    jog_frame.grid(row=1, column=0, pady=80, ipady = 10)

    dealer_frame = LabelFrame(main_frame, text = "Dealer", bd = 0)
    dealer_frame.grid(row=0, column=0, ipady = 10)


    dealer_label = Label(dealer_frame,textvariable= d_val)
    dealer_label.grid(row=0, column=0, ipady = 10)

    jog_label = Label(jog_frame, textvariable=j_val)
    jog_label.grid(row=0, column=0, ipady = 10)

    dealer_baralho = LabelFrame(main_frame, text = "Mão", bd = 0)
    dealer_baralho.grid(row=0, column=1, ipady = 50, ipadx= 100)

    jog_baralho = LabelFrame(main_frame, text = "Mão", bd = 0)
    jog_baralho.grid(row=1, column=1, ipady = 50, ipadx= 100)

    jog_b_label = Label(jog_baralho, textvariable= j_bar)
    jog_b_label.grid(row=0, column=0, ipady = 10)

    dealer_b_label = Label(dealer_baralho, textvariable= d_bar)
    dealer_b_label.grid(row=0, column=0, ipady = 10)

    tirar_but = Button(main_frame, text = "tirar carta", state= "disabled", command= tirar_carta)
    tirar_but.grid(row=3, column=0, ipady = 10)

    pass_but = Button(main_frame, text = "passar", state= "disabled", command=passar)
    pass_but.grid(row=4, column=2, ipady = 10)

    des_but = Button(main_frame, text = "desistir da ronda", state= "disabled", command= desistir)
    des_but.grid(row=4, column=1, ipady = 10)

    dup_but = Button(main_frame, text = "duplicar a aposta", state= "disabled", command= duplicar)
    dup_but.grid(row=4, column=0, ipady = 10)

    dinheiro_label = Label(main_frame, textvariable = dinheiro)
    dinheiro_label.grid(row=3, column=1, ipadx = 10)

    root.mainloop()