# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Assignment 1 : Blackjack Game ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from random import randint

# game opening, asking player's name and displaying both of the scores and current round.
print("Welcome to the game!")
player_name = input("Please enter your name.\n")
score_of_the_d = 1000
score_of_the_p = 1000
round_no = 1  # I create a variable named round_no with its value 1 and at the end of each round it increases 1.
while score_of_the_d > 0 and score_of_the_p > 0:  # I used while to continue the game until one of the player's
    # score became less than or equal to 0.
    print("===================================\n" + "==============ROUND", str(round_no) + "==============\n"
          + "===================================")
    print("          CURRENT POINTS:              \n"
          + "           Dealer:", str(score_of_the_d) + "\n" + "           " + str(player_name) + ":",
          str(score_of_the_p))

    bet = input("Enter a bet less than or equal the scores.\n")  # asking player for a bet
    # and creating a variable 'bet' to it.
    while int(bet) > score_of_the_d or int(bet) > score_of_the_p or int(bet) < 0:  # pre-test
        bet = input("Your enter does not match the requirements. Enter a bet again.")  # asking bet one
        # more time.

    # 2 cards for player. I use the same code to give the player cards in the whole code:

    card_for_p = str(min(10, randint(1, 13)))  # I use the given function 'randint' to give player and dealer cards.
    card_for_p += " " + str(min(10, randint(1, 13)))  # for each new card I add it to previous cards
    hand_p = card_for_p.split(" ")  # making cards separate to calculate the total value.
    sum_p = 0
    # a special part for ace(1) because its value differs depends on the other cards.
    # firstly, I create a variable named as_count_of_p.
    ace_count_of_p = 0
    for card_p in hand_p:
        if card_p == '1':  # In for function whenever there exist an element "1" the as_count_of_p increases 1.
            ace_count_of_p += 1
        sum_p += int(card_p)
    while sum_p <= 11 and ace_count_of_p > 0:  # if the sum of cards is less or equal to 11 and there is an ace in hand,
        sum_p += 10  # it can use as 11, so I add 10 to previous sum
        ace_count_of_p -= 1  # and decreased as_count_of_p 1 because I used one of the aces in the hand.

    # 2 cards for dealer (one is the hidden one (?)). I use the same code to give the dealer cards in the whole code:

    d_ = min(10, randint(1, 13))  # I create a variable for the hidden card.
    # It will be shown to player when player's turn ends each round.
    card_for_d = str(min(10, randint(1, 13)))  # second card.
    hand_d = card_for_d.split(" ")  # making cards separate elements to calculate the total value.
    sum_d_pre = 0  # this variable is the sum of all cards except the hidden card.
    sum_d = 0  # this variable is the sum of all cards.
    ace_count_of_d = 0
    for card_d in hand_d:
        if card_d == '1':
            ace_count_of_d += 1
        sum_d_pre += int(card_d)
    sum_d = sum_d_pre + d_  # calculating the real total value.
    while sum_d <= 11 and ace_count_of_d > 0:
        sum_d_pre += 10
        ace_count_of_d -= 1

    # displaying hands:
    print("Your hand:", card_for_p, "(Total:", sum_p, ")")
    print("Dealer's hand: ?", card_for_d)

    # asking player the option 1:
    option_1 = input("Do you want to take just one card and double the bet? (y/n)")

    while option_1 != "y" and option_1 != "n":  # pre-test
        option_1 = input("Do you want to take just one card and double the bet? (y/n)")

    if option_1 == 'y':  # if the player choose option 1 as 'yes' this part of code will execute

        bet = int(bet) * 2  # doubling the bet

        # giving player 1 card and displaying the hand of player:
        card_for_p += " " + str(min(10, randint(1, 13)))
        hand_p = card_for_p.split(" ")  # making cards separate elements to calculate the total value.
        sum_p = 0
        ace_count_of_p = 0
        for card_p in hand_p:
            if card_p == '1':  # a special part for ace(1) because its value differs depends on the other cards.
                ace_count_of_p += 1
            sum_p += int(card_p)
        while sum_p <= 11 and ace_count_of_p > 0:
            sum_p += 10
            ace_count_of_p -= 1
        print("Your hand:", card_for_p, "(Total: ", sum_p, ")")

        # if player's total value is greater than 21; player lose, the scores calculate again and round_no increase 1.
        if sum_p > 21:
            print("You lost. This round's winner is the dealer.")
            score_of_the_p -= int(bet)
            score_of_the_d += int(bet)
            round_no += 1

        # if player's total value is not greater than 21, it's dealer's turn.
        else:
            print("It's dealer's turn.")

            # checking the total value before the while loop.
            if sum_d > sum_p:  # if dealer's total is greater than player's total, dealer win.
                print("Dealer's hand:", d_, card_for_d)
                print("Dealer's hand is greater than you (Total:", sum_d, "). This round's winner is the dealer.")
                score_of_the_p -= int(bet)
                score_of_the_d += int(bet)
                round_no += 1
            elif sum_d == sum_p:  # if both total values are equal, it's a draw.
                print("Dealer's hand:", d_, card_for_d)
                print("The sum of dealer's and your cards are same(Dealer's hand total:", sum_d,
                      "). It's a draw!")
                round_no += 1

            while sum_d < sum_p:  # dealer will draw a card until its total value became greater than
                # or equal to player's total value.
                card_for_d += " " + str(min(10, randint(1, 13)))
                hand_d = card_for_d.split(' ')
                sum_d_pre = 0
                sum_d = 0
                ace_count_of_d = 0
                for card_d in hand_d:
                    if card_d == '1':
                        ace_count_of_d += 1
                    sum_d_pre += int(card_d)
                sum_d = sum_d_pre + d_
                while sum_d <= 11 and ace_count_of_d > 0:
                    sum_d += 10
                    ace_count_of_d -= 1

                # displaying dealer's hand, this time the hidden card will be open.
                print("Dealer's hand:", d_, card_for_d)

                # this section is for determining the winner.
                if sum_d > 21:
                    print("Dealer's hand exceed 21 (Total:", sum_d, ")")
                    print("Dealer lost. This round's winner is you.")
                    score_of_the_p += int(bet)
                    score_of_the_d -= int(bet)
                    round_no += 1
                elif sum_d == sum_p:
                    print("The sum of dealer's and your cards are same(The dealer's hand total:", sum_d,
                          "). It's a draw!")
                    round_no += 1
                elif sum_p < sum_d:
                    print("Dealer's hand is greater than you (Total:", sum_d, "). This round's winner is the dealer.")
                    score_of_the_p -= int(bet)
                    score_of_the_d += int(bet)
                    round_no += 1

    else:  # if player choose the option 1 as 'n' option 2 will be asked:
        option_2 = "y"
        while option_2 == "y":  # a while loop for option 2 because it's not a one-time process,
            # it will be executed until user does not want to draw a card.
            option_2 = input("Do you want a new card? (y/n)")

            while option_2 != "y" and option_2 != "n":  # pre-test
                option_2 = input("Do you want a new card? (y/n)")

            if option_2 == 'n':  # if player does not want a new card,
                # it will be dealer's turn and this section is same as the previous one.
                print("It's dealer's turn.")
                if sum_d > sum_p:
                    print("Dealer's hand:", d_, card_for_d)
                    print("Dealer's hand is greater than you (Total:", sum_d,
                          "). This round's winner is the dealer.")
                    score_of_the_p -= int(bet)
                    score_of_the_d += int(bet)
                    round_no += 1
                elif sum_d == sum_p:
                    print("Dealer's hand:", d_, card_for_d)
                    print("The sum of dealer's and your cards are same(Dealer's hand total:", sum_d, "). It's a draw!")
                    round_no += 1

                while sum_d < sum_p:
                    card_for_d += " " + str(min(10, randint(1, 13)))
                    hand_d = card_for_d.split(' ')
                    sum_d_pre = 0
                    sum_d = 0
                    ace_count_of_d = 0
                    for card_d in hand_d:
                        if card_d == '1':
                            ace_count_of_d += 1
                        sum_d_pre += int(card_d)
                    sum_d = sum_d_pre + d_
                    while sum_d <= 11 and ace_count_of_d > 0:
                        sum_d += 10
                        ace_count_of_d -= 1
                    print("Dealer's hand:", d_, card_for_d)
                    if sum_d > 21:
                        print("Dealer's hand exceed 21 (Total:", sum_d, ")")
                        print("Dealer lost. This round's winner is you.")
                        score_of_the_p += int(bet)
                        score_of_the_d -= int(bet)
                        round_no += 1
                    elif sum_d == sum_p:
                        print("The sum of dealer's and your cards are same(Dealer's hand total:", sum_d,
                              "). It's a draw!")
                        round_no += 1
                    elif sum_p < sum_d:
                        print("Dealer's hand is greater than you (Total:", sum_d,
                              "). This round's winner is the dealer.")
                        score_of_the_p -= int(bet)
                        score_of_the_d += int(bet)
                        round_no += 1
                break  # I use the function 'break' to exit the while loop.

            # giving player a new card and displaying the hand of player:
            card_for_p += " " + str(min(10, randint(1, 13)))
            hand_p = card_for_p.split(" ")  # making cards separate elements to calculate the total value.
            sum_p = 0
            ace_count_of_p = 0
            for card_p in hand_p:
                if card_p == '1':
                    ace_count_of_p += 1
                sum_p += int(card_p)
            while sum_p <= 11 and ace_count_of_p > 0:
                sum_p += 10
                ace_count_of_p -= 1
            print("Your hand:", card_for_p, "(Total: ", sum_p, ")")
            if sum_p > 21:
                print("You lost. This round's winner is the dealer.")
                score_of_the_p -= int(bet)
                score_of_the_d += int(bet)
                round_no += 1
                break

# displaying the last scores and the winner of the game.
print("=================================")
print("============GAME OVER============")
print("=================================")
print("           LAST POINTS:              \n"
      + "           Dealer:", str(score_of_the_d) + "\n" + "           " + str(player_name) + ":",
      str(score_of_the_p))
if score_of_the_d <= 0:
    print("Congratulations! You win!")

elif score_of_the_p <= 0:
    print("Game over. You lost!")
    
