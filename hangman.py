#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# just a little hangman,game for educcational puurpose only
import random

trial = 7
letter_found ="" 
display = ""
level = 1

# Todo ! several lists with increasing dificculties // several game levels

word_list1 = ["mac", "osx", "dos","bsd","foo","csh","zsh"]
word_list2 = ["free", "bytes", "alpha","kilo","root","bash"]
word_list3 = ["blender", "photoshop", "gimp", "illustrator", "python","amigaos"]
word_list4 = ["procrastinator", "perpendicular", "supercalifragistics","kaleidoscopes","computationally" ]


print(">> Bienvenue dans le pendu <<")
level = int(input("Choisissez votre difficulté : [1,2,3,4])"))

word_tuple = word_list1 #default value

if level > 0:
    word_tuple = word_list1
if level > 1:
    word_tuple = word_list2
if level > 2:
    word_tuple = word_list3
if level > 3:
    word_tuple = word_list4
    


solution = random.choice(word_tuple) # we pick one word from the list above


# We print as many "-" than letters in "solutionn"
for l in solution:
    display= display + "_ "







# Gamelogic
while trial > 0:    
    print("Mot à deviner :\n", display + "  : " +  str(len(solution))+ " lettres")
    
    # Only 1 char Alpha 
    guess = input("Proposez une lettre : ")[0:1].lower()
    if guess.isalpha() == False:
        guess = input("Merci de ne taper que des lettre : ")[0:1].lower()
    
    if guess in solution:
        letter_found = letter_found + guess
        print("-> Bien vu!")


    else:
        trial = trial - 1
        print("-> Nope\n")
        print("Essai(s) restant(s) : " + str(trial))
        if trial==0:
            print(" ==========Y= ")
        if trial<=1:
            print(" ||/       |  ")
        if trial<=2:
            print(" ||        0  ")
        if trial<=3:
            print(" ||       /|\ ")
        if trial<=4:
            print(" ||       /|  ")
        if trial<=5:                    
            print("/||           ")
        if trial<=6:
            print("==============\n")


        
    display = ""
    
    for x in solution:
        if x in letter_found:
            display += x + " "
        else:
            display += "_ "
            
    if "_" not in display:
        print(">>> Gagné! <<<")
        
        break

print("\n    * Fin de la partie *    ")
print("Le mot recherché était : "+ solution +" !")