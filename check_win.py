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