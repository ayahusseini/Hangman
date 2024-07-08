from string import ascii_lowercase

guessed_already = []


def validate_input(user_guess, guessed_already):
    '''
    check that the user's guess is a single letter and hasn't been guessed already.
    Returns True if the input is correct and False otherwise
    '''
    if len(user_guess) != 1 or user_guess.lower() not in ascii_lowercase:
        print('please supply a single letter')
        return False
    if user_guess in guessed_already:
        print('You already guessed this letter')
        return False
    else:
        return True


def get_input(guessed_already):
    '''
    Takes repeated inputs until a valid guess is supplied.  Updates the guessed_already list to reflect the new guess (if it's valid).
    Returns:
        user_guess (str): the user input as a lowercase letter.
        guessed_already (list): an updated set of letters already guessed
    '''
    while True:
        user_guess = input('Try a letter: ')
        if validate_input(user_guess, guessed_already):
            guessed_already.append(user_guess.lower())
            return user_guess.lower(), guessed_already


def draw_hangman(num_failed_guesses):
    '''
    Prints a string showing the state of the hangman board based on the number of failed guesses'''
    hangman_pictures = [
        r'''
        x-------x
        |       |
                |
                |
                |
                |
                |
        --------x
        ''',
        r'''
        x-------x
        |       |
        0       |
                |
                |
                |
                |
        --------x
        ''',
        r'''
        x-------x
        |       |
        0       |
        |       |
                |
                |
                |
        --------x
        ''',
        r'''
        x-------x
        |       |
        0       |
        |\      |
                |
                |
                |
        --------x
        ''',
        r'''
        x-------x
        |       |
        0       |
       /|\      |
                |
                |
                |
        --------x
        ''',
        r'''
        x-------x
        |       |
        0       |
       /|\      |
       /        |
                |
                |
        --------x
        ''',
        r'''
        x-------x
        |       |
        0       |
       /|\      |
       / \      |
                |
                |
        --------x
        '''
    ]
    print(hangman_pictures[num_failed_guesses])


def display_guessed_letters(answer, guessed_already):
    '''
    Prints a string representing the current state of the answer board, based on what has been guessed already. 
    For example, if answer = 'games' and guessed_already is the set {'a','m','l'} then the string '- a m - -' is returned 
    '''
    display_string = []

    for letter in answer:
        if letter in guessed_already:
            display_string.append(letter)
            print(display_string)
        else:
            display_string.append('-')
        display_string.append(' ')
    print(' '.join(display_string))


def game_over(num_wrong, answer, guessed_already):
    '''
    Stops the game if the number of unique letters in the answer is less than the number of unique guessed letters
    Returns True if the game is over, and False otherwise
    '''
    dead_hangman_tries = 6  # number of incorrect attempts that kill hangman
    if num_wrong == dead_hangman_tries:
        return True
    if len(set(answer)) <= len(guessed_already):
        return True
    else:
        return False
