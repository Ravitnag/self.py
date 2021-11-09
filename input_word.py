def show_hidden_word(secret_word, old_letters_guessed):
    word = ''
    for secret_letter in secret_word:
         if (secret_letter in old_letters_guessed):
           word += secret_letter + ' ' 
         else:
           word += '_ ' 
    return word[:-1];   
            
secret_word = "mammals"
old_letters_guessed = ['s', 'p', 'j', 'i', 'm', 'k']
print(show_hidden_word(secret_word, old_letters_guessed))