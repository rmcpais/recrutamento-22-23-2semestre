from tkinter import *
import random
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo



root = Tk()
root.title('Codemy.com - Card Deck')
#root.iconbitmap('c:/gui/codemy.ico')
root.geometry("1200x800")
root.configure(background="green")


#ask bet
def bet(money):
    global aposta
    aposta = int(askstring('Bet', 'How much money do you want to bet?'))
    money -= aposta
    money_label = Label(button_frame, text = f"{money}$")
    money_label.grid(row=0, column=3)
    return money


#stand
def stand():
    global player_total, dealer_total, player_score

    player_total = 0
    dealer_total = 0

    for score in dealer_score:
                #Add up score
                dealer_total += score

    for score in player_score:
                #Add up score
                player_total += score            

    card_button.config(state="disabled")
    stand_button.config(state="disabled")

    if dealer_total >= 17:
        #Check if bust
        if dealer_total > 21:
            messagebox.showinfo("Player Wins!!", f"Player Wins! You win {2*aposta}$ Dealer: {dealer_total} pLayer: {player_total}")
            money_label = Label(button_frame, text = f"{money+aposta*2}$")
            money_label.grid(row=0, column=3)
            
        elif dealer_total == player_total:
            messagebox.showinfo("Its a tie", f"Tie! You get your money back! Dealer: {dealer_total} pLayer: {player_total}")
            money_label = Label(button_frame, text = f"{money+aposta}$")
            money_label.grid(row=0, column=3)
            money = money + aposta
        elif dealer_total > player_total:          
            #dealer wins
            messagebox.showinfo("Dealer Wins!!", f"Dealer Wins! Dealer: {dealer_total} pLayer: {player_total}")
        elif dealer_total < player_total:          
            #player wins
            messagebox.showinfo("Player Wins!!", f"Player Wins! You win {2*aposta}$ Dealer: {dealer_total} Player: {player_total}")
            money_label = Label(button_frame, text = f"{money+aposta*2}$")
            money_label.grid(row=0, column=3)
            money = money + aposta* 2
    else:
        #add card to dealer
        dealer_hit()
        #recalculate Stuff
        stand()    

#Test for balckjack on shuffle
def blackjack_shuffle(player):
    global player_total, dealer_total, player_score
    
    player_total = 0
    dealer_total = 0

    if player == "dealer":
        if len(dealer_score) ==2:
            if dealer_score[0]+dealer_score[1] == 21:
                blackjack_status["dealer"] = "yes"
                #messagebox.showinfo("Dealer Wins!", "Blackjack!")
                #disable buttons
                #card_button.config(state="disabled")
                #stand_button.config(state="disabled")

    if player == "player":
        if len(player_score) ==2:
            if player_score[0]+player_score[1] == 21:
                blackjack_status["player"] = "yes"
        else:
            #loop thru player score
            for score in player_score:
                #Add up score
                player_total += score
                if player_total == 21:
                    blackjack_status["player"] = "yes"
                elif player_total >21:
                    #Ace conversion
                    for card_number, card in enumerate(player_score):
                        if card == 11:
                            player_score[card_number] = 1
                            player_total = 0
                            for score in player_score:
                                #Add up score
                                player_total += score
                            if player_total > 21:    
                                blackjack_status["player"] = "bust"

            else:
                if player_total == 21:
                    blackjack_status["player"] = "yes"
                if player_total > 21:               
                    blackjack_status["player"] = "bust"


    if len(dealer_score) == 2 and len(player_score) == 2:
        #check for tie
        if blackjack_status["dealer"] == "yes" and blackjack_status["player"] == "yes":
            messagebox.showinfo("Its a tie", "Tie! You get your money back!")
            card_button.config(state="disabled")
            stand_button.config(state="disabled")
            money_label = Label(button_frame, text = f"{money+aposta}$")
            money_label.grid(row=0, column=3)

        #check for delaer win
        elif blackjack_status["dealer"] == "yes" :
            messagebox.showinfo("Dealer Wins!", "Blackjack! Dealer Wins!")
            card_button.config(state="disabled")
            stand_button.config(state="disabled")
            

        #check for player win
        elif blackjack_status["player"] == "yes" :
            messagebox.showinfo("Player Wins!", f"Blackjack! Player Wins! You win {aposta*2.5}$ ")
            card_button.config(state="disabled")
            stand_button.config(state="disabled")
            money_label = Label(button_frame, text = f"{money+aposta*2.5}$")
            money_label.grid(row=0, column=3) 
            money = money + aposta* 2.5 

    else:
        #check for tie
        if blackjack_status["dealer"] == "yes" and blackjack_status["player"] == "yes":
            messagebox.showinfo("Its a tie" "Tie! You get your money back!")
            money_label = Label(button_frame, text = f"{money+aposta*2.5}$")
            card_button.config(state="disabled")
            stand_button.config(state="disabled")
            money = money + aposta* 2.5
        #check for delaer win
        elif blackjack_status["dealer"] == "yes" :
            messagebox.showinfo("Dealer Wins!", "Blackjack! Dealer Wins!")
            card_button.config(state="disabled")
            stand_button.config(state="disabled") 

        #check for player win
        elif blackjack_status["player"] == "yes" :
            messagebox.showinfo("Player Wins!", f"Blackjack! Player Wins! You win {aposta*2.5}$ ")
            money_label = Label(button_frame, text = f"{money+aposta*2.5}$")
            card_button.config(state="disabled")
            stand_button.config(state="disabled")
            money = money + aposta* 2.5
    
    #check for player bust                     
    if blackjack_status["player"] == "bust":
        messagebox.showinfo("Player Busts!", f"Player Loses! {player_total}")
        card_button.config(state="disabled")
        stand_button.config(state="disabled")


#Resize Card
def resize_cards(card):
    #Open the image
    our_card_img = Image.open(card)
    
    #Resize The image
    our_card_resize_image = our_card_img.resize((150,218))
    #output the card
    global our_card_image
    our_card_image = ImageTk.PhotoImage(our_card_resize_image)
    
    #return the card
    return our_card_image


#shuffle the cards:
def shuffle():
    #keep track of winning
    global blackjack_status, player_total, dealer_total, money
    money = bet(money)
    


    player_total = 0
    dealer_total = 0

    blackjack_status = {"dealer":"no", "player":"no"}
                         

    card_button.config(state="normal")
    stand_button.config(state="normal")
    #Clear
    dealer_label_1.config(image='')
    dealer_label_2.config(image='')
    dealer_label_3.config(image='')
    dealer_label_4.config(image='')
    dealer_label_5.config(image='')

    player_label_1.config(image='')
    player_label_2.config(image='')
    player_label_3.config(image='')
    player_label_4.config(image='')
    player_label_5.config(image='')


    suits = ["diamonds", "clubs","hearts", "spades"]
    values = range(2,15)
    
    global deck
    deck = []
    
    for suit in suits:
        for value in values:
            deck.append(f'{value}_of_{suit}')
    
    
    #create players
    global dealer, player, dealer_spot, player_spot, dealer_score, player_score
    dealer = []
    player = []
    dealer_score = []
    player_score = []   
    dealer_spot = 0
    player_spot = 0
    

    #Shuffle two cards for player and dealer
    dealer_hit()
    dealer_hit()

    player_hit()
    player_hit()

    #Put number of remain card in title bar
    root.title(f'Codemy.com - {len(deck)} Cards Left')

def dealer_hit():
    global dealer_spot , player_total, dealer_total, player_score

    if dealer_spot < 5:
        try:
            #get the player card
            dealer_card = random.choice(deck)
            #remove card from deck
            deck.remove(dealer_card)
            #append cart to player
            dealer.append(dealer_card)
            #append to dealer score list
            dcard = int(dealer_card.split("_",1)[0])
            if dcard == 14:
                dealer_score.append(11)
            elif dcard >= 11:
                dealer_score.append(10)
            else:
                dealer_score.append(dcard)        

            #Outpout card to screen
            global dealer_image1, dealer_image2, dealer_image3, dealer_image4, dealer_image5

            if dealer_spot ==0:
                dealer_image1 = resize_cards(f'cards/{dealer_card}.png')
                dealer_label_1.config(image = dealer_image1)
                #Increment our player spot counter
                dealer_spot +=1
            elif dealer_spot == 1:
                dealer_image2 = resize_cards(f'cards/{dealer_card}.png')
                dealer_label_2.config(image = dealer_image2)
                #Increment our player spot counter
                dealer_spot +=1
            elif dealer_spot == 2:
                dealer_image3 = resize_cards(f'cards/{dealer_card}.png')
                dealer_label_3.config(image = dealer_image3)
                #Increment our player spot counter
                pdealer_spot +=1 
            elif dealer_spot == 3:
                dealer_image4 = resize_cards(f'cards/{dealer_card}.png')
                dealer_label_4.config(image = dealer_image4)
                #Increment our player spot counter
                dealer_spot +=1 
            elif dealer_spot == 4:
                dealer_image5 = resize_cards(f'cards/{dealer_card}.png')
                dealer_label_5.config(image = dealer_image5)
                #Increment our player spot counter
                dealer_spot +=1

                #See if 5 card bust
                # Grab ou «r totals
                player_total = 0
                dealer_total = 0

                #get player score
                for score in player_score:
                       player_total += score
                for score in dealer_score:
                       dealer_total += score            

                if dealer_total <=21:
                    card_button.config(state="disabled")
                    stand_button.config(state="disabled")
                    messagebox.showinfo("Dealer Wins!", f"Dealer Wins! Dealer: {dealer_total} pLayer: {player_total}")
            #Put number of remain card in title bar
            root.title(f'Codemy.com - {len(deck)} Cards Left')
        except:
            root.title(f'Codemy.com - {len(deck)} Cards Left')

        blackjack_shuffle("dealer")    

def player_hit():
    global player_spot , player_total, dealer_total, player_score

    if player_spot < 5:
        try:
            #get the player card
            player_card = random.choice(deck)
            #remove card from deck
            deck.remove(player_card)
            #append cart to player
            player.append(player_card)

            pcard = int(player_card.split("_",1)[0])
            if pcard == 14:
                player_score.append(11)
            elif pcard >= 11:
                player_score.append(10)
            else:
                player_score.append(pcard)  

            #Outpout card to screen
            global player_image1, player_image2, player_image3, player_image4, player_image5

            if player_spot ==0:
                player_image1 = resize_cards(f'cards/{player_card}.png')
                player_label_1.config(image = player_image1)
                #Increment our player spot counter
                player_spot +=1
            elif player_spot == 1:
                player_image2 = resize_cards(f'cards/{player_card}.png')
                player_label_2.config(image = player_image2)
                #Increment our player spot counter
                player_spot +=1
            elif player_spot == 2:
                player_image3 = resize_cards(f'cards/{player_card}.png')
                player_label_3.config(image = player_image3)
                #Increment our player spot counter
                player_spot +=1 
            elif player_spot == 3:
                player_image4 = resize_cards(f'cards/{player_card}.png')
                player_label_4.config(image = player_image4)
                #Increment our player spot counter
                player_spot +=1 
            elif player_spot == 4:
                player_image5 = resize_cards(f'cards/{player_card}.png')
                player_label_5.config(image = player_image5)
                #Increment our player spot counter
                player_spot +=1             

                                #See if 5 card bust
                # Grab ou «r totals
                player_total = 0
                dealer_total = 0

                #get player score
                for score in player_score:
                       player_total += score
                for score in dealer_score:
                       dealer_total += score            

                if player_total <=21:
                    card_button.config(state="disabled")
                    stand_button.config(state="disabled")
                    messagebox.showinfo("Player Wins!", f"Player Wins! Dealer: {dealer_total} pLayer: {player_total}")
         
            #Put number of remain card in title bar
            root.title(f'Codemy.com - {len(deck)} Cards Left')
        except:
            root.title(f'Codemy.com - {len(deck)} Cards Left')

        blackjack_shuffle("player")
#Deal out Cards    
def deal_cards():
    try:
        #get the dealer card
        card = random.choice(deck)
        #remove card from deck
        deck.remove(card)
        #append cart to dealer
        dealer.append(card)
        #Outpout card to screen
        #Outpout card to screen
        global dealer_image
        dealer_image = resize_cards(f'cards/{card}.png')
        dealer_label.config(image = dealer_image)
        #dealer_label.config(text=card)        
        
        #get the player card
        card = random.choice(deck)
        #remove card from deck
        deck.remove(card)
        #append cart to player
        player.append(card)
        #Outpout card to screen
        global player_image
        player_image = resize_cards(f'cards/{card}.png')
        player_label.config(image = player_image)
        #player_label.config(text=card)
        
        #Put number of remain card in title bar
        root.title(f'Codemy.com - {len(deck)} Cards Left')        
        
    except:
        root.title(f'Codemy.com - No Cards in Deck')



my_frame = Frame(root, bg="green")
my_frame.pack(pady=20)

dealer_Frame = LabelFrame(my_frame, text="Dealer", bd=0)
dealer_Frame.pack(padx=20, ipadx=20)

player_frame = LabelFrame(my_frame, text="Player", bd=0)
player_frame.pack(ipadx=20, pady = 10)

#Put card in frames
dealer_label_1 = Label(dealer_Frame, text='')
dealer_label_1.grid(row=0, column=0, pady=20, padx=20)

dealer_label_2 = Label(dealer_Frame, text='')
dealer_label_2.grid(row=0, column=1, pady=20, padx=20)

dealer_label_3 = Label(dealer_Frame, text='')
dealer_label_3.grid(row=0, column=2, pady=20, padx=20)

dealer_label_4 = Label(dealer_Frame, text='')
dealer_label_4.grid(row=0, column=3, pady=20, padx=20)

dealer_label_5 = Label(dealer_Frame, text='')
dealer_label_5.grid(row=0, column=4, pady=20, padx=20)

player_label_1 = Label(player_frame, text='')
player_label_1.grid(row=1, column=1, pady=20, padx=20)

player_label_2 = Label(player_frame, text='')
player_label_2.grid(row=1, column=2, pady=20, padx=20)

player_label_3 = Label(player_frame, text='')
player_label_3.grid(row=1, column=3, pady=20, padx=20)

player_label_4 = Label(player_frame, text='')
player_label_4.grid(row=1, column=4, pady=20, padx=20)

player_label_5 = Label(player_frame, text='')
player_label_5.grid(row=1, column=5, pady=20, padx=20)


#Create Button Frame
button_frame = Frame(root, bg="green")
button_frame.pack(pady=20)


money = int(askstring('Money', 'How much money do you have?'))

money_label = Label(button_frame, text = f"{money}$")
money_label.grid(row=0, column=3)

#Create a couple buttons
Play_button = Button(button_frame, text="Play", font =("Helvetica", 14), command = shuffle)
Play_button.grid(row=0, column=0)

card_button = Button(button_frame, text="Hit!", font =("Helvetica", 14), command = player_hit)
card_button.grid(row=0, column=1, pady=10)

stand_button = Button(button_frame, text = "Stand!", font=("Helvetica", 14), command= stand)
stand_button.grid(row=0, column=2)


root.mainloop()