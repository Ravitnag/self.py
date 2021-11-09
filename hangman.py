def head_of_game ():
    HANGMAN_ASCII_ART = """
     _    _                                         
    | |  | |                                        
    | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
    |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | |  | | (_| | | | | (_| | | | | | | (_| | | | |
    |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                         __/ |                      
                        |___ /    """

    MAX_TRIES = 6
    


    return (HANGMAN_ASCII_ART, MAX_TRIES)
def check_win(secret_word, old_letters_guessed):
    count = 0
    for secret_letter in secret_word:
         if (secret_letter in old_letters_guessed):
           count+=1
          
    if (len(secret_word) == count):
        return True;
    else:
        return False;       

secret_word = "yes"
old_letters_guessed = ['d', 'g', 'e', 'i', 's', 'k', 'y']
print(check_win(secret_word, old_letters_guessed))



title, tries = head_of_game()

