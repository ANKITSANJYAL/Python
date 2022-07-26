
import random
def hangman():
    x = "y"
    while x == "y":
        word = random.choice(["albert" , "radhe" , "rekha" , "bandariya" , "bawleni" , "pareshe" , "umeshe", "bishale" , "rohane" , "ashim" , "saggy" , "ankit" , "ear" ,  "sometimes" ,  "described", "as" , "his" , "annus" ,"mirabilis", 'miracle',' year', 'Einstein' ,"published" ,"four" ,'groundbreaking' ,'papers' , 'These' , 'outlined' ,'the' , 'theory' ,'ofthe' ,'photoelectric' ,'effect', 'explained', 'Brownian', 'motion', 'introduced' ,'special' , 'relativity'])
        valid_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"     # WHAT THE USER CAN INPUT
        turns = 10          # MAXIMUM NUMBER OF TURNS
        guessmade = ""   # THIS IS THE GUESSMADE VARIABLE
        
        
        
                    #LOOPING IS VERY IMPORTANT
                    
                    
                    
                    
                    
        while len(word)>0:
            main = ""
            missed = 0
            
            
            
                 # CHANGING THE FONT OF THE WORD WITH THE CHANGE OF NUMBER OF TURNS
                 
                 
                 
            for letter in word :
                if letter in guessmade:
                    main = main + letter
                else:
                    main = main + "_" + ""
                    
                    
                    
                    #CONDITION OF WIN
            
            
            
            
            
            if main == word or main == word.upper():
                print("------------------------")
                print("|!! CONGRATULATIONS !! |")
                print("|       YOU WON        |")
                print("|          !!!         |")
                print("------------------------")
                break
            
            
            
                    # WHAT ABOUT THE INPUT WORD
            
            print("please enter the guess word:" , main)
            guess = input()
            
            
                    # WHAT IF THE INPUT WORD IS NOT VALID 
            
            
            
            
            if guess in valid_letters:
                guessmade = guessmade + guess
            else:
                guess = input("plese enter the valid letter")
                
                
                
                
                
                
                           # CONDITION TO HANG THE PLAYER
                
                 
            if guess not in word:
                turns = turns - 1
                
                
                
               
                
                           # THE HANGING MAN IS TO BE MADE
                
                
                
                
                
                
                if turns == 9:
                    print("you have 9 turns left")
                    print("---------------")
               
                if turns == 8:
                    print("8 turns remaining")
                    print(" ------------- ")
                    print("       0       ")
                if turns == 7:
                    print("7 turns remaining")
                    print(" ------------- ")
                    print("        0      ")
                    print("        |      ")
                if turns == 6:
                    print("6 turns remaining")
                    print(" ------------- ")
                    print("        0      ")
                    print("        |      ")
                    print("       /       ")
                if turns == 5:
                    print("5 turns remaining")
                    print(" ------------- ")
                    print("        0      ")
                    print("        |      ")
                    print("       / \     ")
                if turns == 4:
                    print("4 turns remaining hurry up!")
                    print(" ------------- ")
                    print("      \ 0      ")
                    print("        |      ")
                    print("       / \     ")
                if turns == 3:
                    print("3 turns remaining hurry up!")
                    print(" ------------- ")
                    print("      \ 0 /    ")
                    print("        |      ")
                    print("       / \     ")
                if turns == 2:
                    print("on;y 2 turns remaining hurry up!")
                    print(" ------------- ")
                    print("      \ 0| /   ")
                    print("        |      ")
                    print("       / \     ")
                if turns ==  1:
                    print("you have last chance now take care")
                    print(" ------------- ")
                    print("      \ 0_|/   ")
                    print("        |      ")
                    print("       / \     ")
                if turns == 0:
                    print("lol you let the kind man die")
                    print("--------------you loose------------")
                    print(" ------------- ")
                    print("        0 _|   ")
                    print("      / | \    ")
                    print("       / \     ")
                    print("the required word was" , word) 
                    break
        x = input("do you wanna play again? y for yes and n for no")            
            
            
            
            
            
                    ## INTERFACE OF THE PROGRAM




          
print("------------------------------HANGMAN -----GAME----------------------------------------")
name = input("hey buddy please enter your name")
print("WELCOME TO THE HANGMAN GAME " , name.upper())
print("you will be having only 10 chances so check before choosing the word")
hangman()
print()
        
        