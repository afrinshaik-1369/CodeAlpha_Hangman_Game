import random
import Hangman_stages
import word_file
#word_list = ["apple","banana","potato"]
lives = 6
chosen_word = random.choice(word_file.words)
print(chosen_word)
display=[]
for i in range(len(chosen_word)):#0 1 2 3 4 5
    display+='_'
print(display)
game_over=False
while not game_over:
    guessed_letter=input("guess a letter:").lower() #t
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter==guessed_letter:
           display[position]=guessed_letter
    print(display)
    if guessed_letter not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("you lose!!")
    if'_'not in display:
        game_over = True
        print("you win")
    print(Hangman_stages. stages [lives])




