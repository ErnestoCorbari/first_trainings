import time #for type_out (see below)
import random #for type_out (see below)
import numpy as np #for randomly-generated matrix (mine_field_hidden)

def type_out(text):
    for letter in text:
        delay = random.uniform(0.05, 0.18) 
        print(letter, end='', flush=True)
        time.sleep(delay)

mine_field_hidden = np.random.randint(0, 3, (10, 10))
#it creates a random matrix

mine_field_visible = [
    [" * ", ' 1 ',' 2 ',' 3 ',' 4 ', ' 5 ', ' 6 ', ' 7 ', ' 8 ', ' 9   '],
    [" 1", '|  ','|  ','|  ','|  ', '|  ', '|  ', '|  ', '|  ', '|   |'],
    [" 2", '|  ','|  ','|  ','|  ', '|  ', '|  ', '|  ', '|  ', '|   |'],
    [" 3", '|  ','|  ','|  ','|  ', '|  ', '|  ', '|  ', '|  ', '|   |'],
    [" 4", '|  ','|  ','|  ','|  ', '|  ', '|  ', '|  ', '|  ', '|   |'],
    [" 5", '|  ','|  ','|  ','|  ', '|  ', '|  ', '|  ', '|  ', '|   |'],
    [" 6", '|  ','|  ','|  ','|  ', '|  ', '|  ', '|  ', '|  ', '|   |'],
    [" 7", '|  ','|  ','|  ','|  ', '|  ', '|  ', '|  ', '|  ', '|   |'],
    [" 8", '|  ','|  ','|  ','|  ', '|  ', '|  ', '|  ', '|  ', '|   |'],
    [" 9", '|  ','|  ','|  ','|  ', '|  ', '|  ', '|  ', '|  ', '|   |'],
]

array_treasures = [
" Congratulations! The box contains AN UNORTHODOX MARXIST IDEOLOGY!\n",
" Congratulations! The box contains SWEET MEMORIES OF NON-EXISTING OLD GOOD TIMES!\n",
" Congratulations! The box contains A HEAVY AND INCURABLE ADDICTION TO KETAMINE!\n",
" Congratulations! The box contains A CURIOUS PLEASURE FOR PUTTING OBJECTS INTO YOUR NOSE!\n",
" Congratulations! The box contains A COMPLETELY USELESS BUT REALLY NICE BIRTH CERTIFICATE FROM YUGOSLAVIA!\n",
" Congratulations! The box contains THE SECRET RECIPE OF LEGENDARY YOUR GRANDMA'S CROQUETAS!\n",
" Congratulations! The box contains FEELING THAT NOTHING BUT PUTTING BOMBS SELECTIVELY REALLY HAS SENSE!\n",
" Congratulations! The box contains THE STRONGEST MUNCHIES EVER EXPERIENCED BY A HUMAN BEING!\n"
]      

#INTRO
type_out(" Welcome to the Minefield. Welcome to hell. \n")
go_on = input(" Press Enter when you're ready (to die).")
if go_on == "":
    type_out(" Let's go.\n\n")
else:
    type_out(" Don't be a chicken. Press fucking Enter.")

for i in mine_field_visible:
    result = ' '.join(i)
    print(result)
#it allows to print a list (the visible minefield) without commas and inverted commas. 

for step in mine_field_hidden:
    type_out("\n Choose where to step.\n")
    step_row = int(input(" First choose the raw. "))
    step_column = int(input(" Now choose the column. "))
    
    #BOMBS
    if mine_field_hidden[step_row][step_column] == 1:
        type_out(" BOOOOOOOOOOOM! (You just died)")
        mine_field_visible[step_row][step_column] =  '| 1'
        for i in mine_field_visible:
            result = ' '.join(i)
            print(result)     
        go_on = input("\n You can blame arms industry.\n Now press Enter to exit.")
        if go_on == "":
            break #it ends the game
    
    #EMPTY FIELD
    elif mine_field_hidden[step_row][step_column] == 0:
            type_out(" No bombs here! You can continue exploring. \n")
            mine_field_visible[step_row][step_column] =  '| 0'
            for i in mine_field_visible:
                result = ' '.join(i)
                print(result)
            continue
    
    #MISTERIOUS BOXES 
 
    else:
        arrNumeros = list()
        type_out(" You found a misterous box! Open it and continue exploring.\n")
        mine_field_visible[step_row][step_column] = '| X' #it marks the place with an X 
        open = input(" Press Enter to open the misterous box.")
        if open == "":
            aleatorio = random.randint(0, len(array_treasures) - 1)
            if aleatorio in arrNumeros:   
                continue #avoid to repeat a treasure
            else:
                treasure = array_treasures[aleatorio]
                print(treasure)
        else:
            open = input(" Don't be a chicken, press Enter and open the fucking box.")
            if open == "":
                aleatorio = random.randint(0, len(array_treasures) - 1)
            if aleatorio in arrNumeros:   
                continue #avoid to repeat a treasure
            else:
                treasure = array_treasures[aleatorio]
                print(treasure)

    for i in mine_field_visible:
            result = ' '.join(i)
            print(result)
            
    go_on = input("\n Press Enter to continue exploring.")
    if go_on == "":
        continue