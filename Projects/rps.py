# Rock,Paper Scissors vs the Computer
from random import choice

def getWinner(player,computer):
    if player == "r" and computer == "s":
        return "player"
    elif computer == "r" and player == "s":
        return "computer"
    
    if player == "s" and computer == "p":
        return "player"
    elif computer == "s" and player == "p":
        return "computer"
    
    if player == "p" and computer == "r":
        return "player"
    elif computer == "p" and computer == "r":
        return "computer"

    return "redo"

plrScore = 0
comScore = 0
rps = True

while rps:
    computerC = choice(["r","p","s"])
    print('Choose Rock, Paper, or Scissors!')
    playerC = input("Pick [R],[P], or [S]: ").lower()
    
    if playerC != "r" and playerC != "p" and playerC != "s":
        print('invalid choice!')
        continue

    if plrScore != 3 and comScore != 3:
        winner = getWinner(playerC,computerC)

        if winner == "player":
            plrScore += 1
            if plrScore == 3:
                print(f'💡 Player Wins! {plrScore}-{comScore}')
                rps = False
                break

            print(f'💡 Player: {plrScore} 💻 Computer: {comScore} | 💡 Player Point!')
        elif winner == "computer":
            comScore += 1
            if comScore == 3:
                print(f'💻 Computer Wins! {comScore}-{plrScore}')
                rps = False
                break
            print(f'💡 Player: {plrScore} 💻 Computer: {comScore} | 💻 Computer Point!')
        elif winner == "redo":
            print(f'🤷‍♂️ No one won. 💡{plrScore}-{comScore}💻')
            continue
