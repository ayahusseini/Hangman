from string import ascii_lowercase
import pathlib
import random


def get_initial_settings():
    '''
    Gets the minimum and maximum answer lengths from the user.
    Return:
        minlength,maxlength (int) 
    '''
    while True:
        minlength = input('please provide the minimum word length:')
        maxlength = input('please provide the maximum word length:')
        try:
            return int(minlength), int(maxlength)
        except:
            print('please provide positive integers')


def random_answer_generator(min_length, max_length):
    '''
    Select a random answer of length between min_length and max_length (inclusive) from words.txt. The answer will be in lowercase. 
    '''
    print(1)
    words = pathlib.Path(__file__).parent / 'words.txt'
    allowed_words = []
    print(words)
    allowed_words = []
    for word in words.read_text(encoding='utf-8').splitlines():
        if len(word) >= min_length and len(word) <= max_length:
            allowed_words.append(word.lower())

    return random.choice(allowed_words)


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
            guessed_already.add(user_guess.lower())
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
    if num_wrong == dead_hangman_tries or len(set(answer)) <= len(guessed_already):
        print('GAME OVER')
        return True
    else:
        return False


def main():

    print('HANGMAN')
    min_length, max_length = get_initial_settings()
    answer = random_answer_generator(min_length, max_length)

    # wrong guesses counter
    num_wrong = 0
    # letters already guessed
    guessed_already = set()

    while not game_over(num_wrong, answer, guessed_already):
        # display the current state
        draw_hangman(num_wrong)
        display_guessed_letters(answer, guessed_already)
        # get guess
        user_guess, guessed_already = get_input(guessed_already)
        # update the number of wrong guesses
        if user_guess in answer:
            print('correct.')
        else:
            num_wrong += 1
            print('incorrect.')
    # Decide if the user won or lost
    if guessed_already == set(answer):
        print('YOU WIN')
    else:
        print('YOU LOSE')
        if len(set(answer)) <= len(guessed_already):
            print('You guessed more letters than there are in the answer!')
        elif num_wrong == 6:
            print('you ran out of guesses')
        print(f'the correct answer was {answer}')


if __name__ == '__main__':
    main()
