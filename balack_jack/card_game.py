#____black_jack or 29 game
import random

#____The planning phase

#____Dealer card
dealer_card = []

#____player card
player_card = []

#____Deal the card
#____Display the cards

#____Dealer cards
length=0
while len(dealer_card) != 2:
    dealer_card.append(random.randint(1,11))
    length = len(dealer_card)
    if length == 2:
        print("Dealer has X &",dealer_card[1])

#player cards
while len(player_card) != 2:
    player_card.append(random.randint(1,11))
    if len(player_card)==2:
        print("Ypu have",player_card)


#____Sum of the Dealer card
if sum(dealer_card)==21:
    print("Dealer has 21 and wins..!")
elif sum(dealer_card)>21:
    print("Dealer has busted..!")

#____Sum of the player card
while sum(player_card) < 21:
    action_taken = str(input("Do you want to stay or hit..?"))
    if action_taken == "hit":
        player_card.append(random.randint(1,11))
        print("You now have a total of " + str(sum(player_card)) + "from these card ", player_card)
    else:
        print("The dealer has a total of" + str(sum(dealer_card)) + "with", dealer_card)
        print("You have a total of" + str(sum(player_card)) + "with", player_card)
        if sum(dealer_card) > sum(player_card):
            print("Dealer wins")
        else:
            print("You win")
            break

if sum(player_card) > 21:
    print("You BUSTED.! Dealehitr wins.")
elif sum(player_card) == 21:
    print("You win BLACKJACK.! You win.!! 21")


#____Compear the sum of the cards between D v P
#____if p card sum is greater then 21 = Bust
#____if p card sum is less then 21 = Option Hit or stay
#____If P option stay compare sum of D v P
#____if P sum < 21 && > D The P Wins !
#____If P Sum < D Sum Then P Loses