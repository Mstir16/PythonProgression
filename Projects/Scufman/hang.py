from words import words
from visual import lives_visual_dict
import random
import string

def get_word():
    selection = random.choice(words)
    return selection

def evaluate_guessed(word,hiddenword,used_letters):
    guessedletters = []
    newword = ""
    WordCount = 0
    BuildCount = 0

    for letter in word:
        WordCount = WordCount + 1
        for guessed in used_letters:
            if letter == guessed:
                guessedletters.insert(len(guessedletters),letter)

    for letter in guessedletters:
        BuildCount = BuildCount + 1
        for letters in word:
            if letter == letters:
                newword = newword + letters

    return [newword]

def hang_game():
    word = get_word()
    lives = 7
    hangman = True
    used_letters = set()
    hiddenword = None
    customword = ""
    wordlength = 0
    hiddenlength = 0
    OldHword = None
    alphabet = set(string.ascii_lowercase)

    for letter in word:
        newletter = "_"
        wordlength = wordlength + 1
        customword = customword + newletter
    
    hiddenword = customword
    print('Welcome to hangman!')

    while hangman:
        if word == hiddenword and hiddenlength == wordlength:
            print(f'Success! you guessed the word: {word}!')
            hangman = False
            break

        if lives < 0 and hangman != False:
            print(f'Game over! the word was {word}')
            hangman = False
            break
        print(lives_visual_dict[lives])
        print(f'word: {hiddenword} | lives: {lives} | letters guessed: {hiddenlength}/{wordlength}')
        userguess = input("choose a letter a-z: ")
        if userguess not in alphabet:
            print('not a valid letter')
            continue

        if userguess not in used_letters:
            used_letters.add(userguess)
        else:
            print('You already guessed this!')
            continue

        results = evaluate_guessed(word,hiddenword,used_letters)
        hiddenword = results[0]
        if OldHword != None:
            if hiddenword == OldHword:
                lives -= 1
                OldHword = hiddenword
                continue
            OldHword = hiddenword
        elif OldHword == None:
            OldHword = hiddenword

        if results[0] != "":
            hiddenlength = hiddenlength +1
            continue

        elif results[0] == "":
            lives -= 1
            continue



hang_game()
