# The 6.00 Word Game

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList

def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    score = 0
    for char in word:
        score = score + SCRABBLE_LETTER_VALUES[char]
    score *= len(word)
    if (len(word) == n):
        score += 50
    return score

getWordScore('toy',7)
    # TO DO ... <-- Remove this comment when you code this function



#
# Problem #2: Make sure you understand how this function works and what it does!
#
def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter,end=" ")       # print all on the same line
    print()                             # print an empty line

#
# Problem #2: Make sure you understand how this function works and what it does!
#
def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    numVowels = n // 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
def updateHand(hand, word):
      output = hand.copy()
      for char in word:
        if output.get(char,0) != 0:
            output[char]-=1
      return output       
            


#
# Problem #3: Test word validity
#
def isValidWord(word, hand, wordList):
 
    count=0
    handtemp=hand.copy()
    if word=='':
        return False
    else:
        if word in wordList:
            for char in word:
                if char in handtemp and handtemp.get(char)!=0:
                    count=count+1
                    handtemp[char]=handtemp.get(char)-1
            return count==len(word)
        else:
            return False
        
def calculateHandlen(hand):
    len=0
    for i in hand.values():
        len+=i
    return len


def playHand(hand, wordList, n):
    score = 0
    while calculateHandlen(hand) > 0:
    # Display the hand
        print('Current Hand:', end=' '); displayHand(hand)     
        # Ask user for input
        guess = str(input('Enter word, or a "." to indicate that you are finished: '))        
        # If the input is a single period:
        if guess == '.':        
            # End the game (break out of the loop)
            break            
        # Otherwise (the input is not a single period):
        else:        
            # If the word is not valid:
            if isValidWord(guess, hand, wordList) == False:            
                # Reject invalid word (print a message followed by a blank line)
                print('Invalid word, please try again.', '\n')
            # Otherwise (the word is valid):
            else:
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                score += getWordScore(guess, n)
                print('"'+guess+'"', "earned", getWordScore(guess, n), "points. Total:", score, "points", '\n')
                # Update the hand 
                hand = updateHand(hand, guess)               

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    if guess == '.':
        print('Total score:', score, 'points.')
    else:
        print('Run out of letters. Total score:', score, 'points.')
    if score<40:
        print('You failed, Play Again')
    elif score<60:
        print('You belong to level 1')
    elif score<70:
        print('You belong to level 2')
    elif score<80:
        print('You belong to level 1')
    else:
        print('Brlliant, You have become a pro at WordGame.')
    print('Invite Your Friends. Thank You')


def playGame(wordList):
      while True:
        user_input = str(input('Enter n to deal a new hand, r to replay the last hand, or e to end game: '))
        if user_input == 'e':
            break
        elif user_input == 'n':
            hand = dealHand(HAND_SIZE)
            playHand(hand, wordList, HAND_SIZE)
        elif user_input == 'r':
            try:
                playHand(hand, wordList, HAND_SIZE)
            except:
              print('You have not played a hand yet. Please play a new hand first!')                           
        else:
            print('Invalid command.')    



#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
