class Game():

    def play(self, player1, player2):
        if player1.choice == player2.choice:
            return "DRAW"
        elif player1.choice == "rock" and player2.choice == "paper":
            return "Player 2 Wins"
        elif player1.choice == "rock" and player2.choice == "scissors":
            return "Player 1 Wins"
        elif player1.choice == "paper" and player2.choice == "rock":
            return "Player 1 Wins"
        elif player1.choice == "paper" and player2.choice == "scissors":
            return "Player 2 Wins"
        elif player1.choice == "scissors" and player2.choice == "rock":
            return "Player 2 Wins"
        elif player1.choice == "scissors" and player2.choice == "paper":
            return "Player 1 Wins"




# class Game():

#     def play(self, player1, player2):
#         return 7



