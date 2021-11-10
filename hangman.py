## return the headline of the game

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

    

    return HANGMAN_ASCII_ART;

 

## print intruction

def instruction ():

    print ("please enter: ")

    file_path = input ("the path for the file .txt with words int it: ");

    index = int(input ("the index of the secret word: "))

    return (file_path, index);

 

## print the paint of the hangman on given num_of_tries

def print_hangman():

    HANGMAN_PHOTOS = {

        1: """x-------x""",

        2: """x-------x

|

|

|

|

|

""",

        3: """x-------x

|       |

|       0

|

|

|   """,

        4:  """x-------x

|       |

|       0

|       |

|

|""",

        5: """x-------x

|       |

|       0

|      /|\\

|

|""",

        6: """x-------x

|       |

|       0

|      /|\\

|      /

|""",

        7:"""x-------x

|       |

|       0

|      /|\\

|      / \\

|

"""}

    return HANGMAN_PHOTOS;

 

## for given word (a string) and list of char we check if all the letters in the word are on the list. 

# if yes - return true, else - false;

def check_win(secret_word, old_letters_guessed):

    count = 0

    for secret_letter in secret_word:

         if (secret_letter in old_letters_guessed):

           count+=1

          

    if (len(secret_word) == count):

        return True;

    else:

        return False; 

## return a string of letters that discovered from secret_word by old_letters_guessed,

#  and '_' for letter that havn't been discovered yes

def show_hidden_word(secret_word, old_letters_guessed):

    word = ''

    for secret_letter in secret_word:

         if (secret_letter in old_letters_guessed):

           word += secret_letter + ' ' 

         else:

           word += '_ ' 

    return word[:-1];   

 

## return False if the letter_guessed is not valid or if it it already guessed.

# return True if this letter is valid for guessing.

def check_valid_input(letter_guessed, old_letters_guessed):

      if (len(letter_guessed) > 1) or (not(letter_guessed.isalpha()) or (letter_guessed.lower() in old_letters_guessed)):

       return False;

      else:

       return True;

 

## return False if check_valid_input is false 

# return True if check_valid_input is true

# if True -  add the letter to the old_letters_guessed list.

def try_update_letter_guessed(letter_guessed, old_letters_guessed):

    if (check_valid_input(letter_guessed, old_letters_guessed)): 

          old_letters_guessed.append(letter_guessed)

          return True;

    else:

        print ('X') ;

        old_letters_guessed.sort();

        print (" -> ".join(old_letters_guessed))

        return False;      

 

## return the word on the given index in file_path

def choose_word (file_path, index):

    words_open_file = open (file_path, 'r')

    words_file = words_open_file.read().split()

    return words_file[(index-1) % len(words_file)];

## main

def main():

    HEAD_OF_GAME = head_of_game();

    MAX_TRIES = 6

    num_of_tries = 1

    print (HEAD_OF_GAME)

    print (MAX_TRIES)

    ## to change when it ready:

    file_path,index = (instruction())

    HANGMAN_PHOTOS = print_hangman()

    print (HANGMAN_PHOTOS[num_of_tries])

    secret_word = choose_word(file_path,index)

    old_letters_guessed = []

    word = show_hidden_word(secret_word, old_letters_guessed)   

    print (word)

    

 

    while ((num_of_tries <= MAX_TRIES) and (not(check_win(secret_word,old_letters_guessed)))):

        letter = input ("print your next guess letter: ")

        if (try_update_letter_guessed(letter, old_letters_guessed)):

            if (not(letter in secret_word)):

                num_of_tries+=1

                print (":(")

                print (HANGMAN_PHOTOS[num_of_tries])

            word = show_hidden_word(secret_word, old_letters_guessed)   

            print (word) 

 

    if (check_win(secret_word,old_letters_guessed)):

        print ("WIN")

    else:

        print ("LOSE")

            

 

if __name__ == "__main__":

    main()