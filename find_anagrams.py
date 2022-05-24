def find_anagrams(word1, word2):
    """
    Check if two words are anagrams 

    Input: Two strings
    Returns:
        True: if both strings are anagrams
        False: if they are not
    """
    if sorted(word1.replace(" ", "").lower()) == sorted(word2.replace(" ", "").lower()):
        print(True)
    else:
        print(False)

## Implementation
# Will keep looping until user no longer wants to play.
play_again=True

print("*** ANAGRAM CHECK ***\n")
print("You will put in a word then the anagram of that word and we'll tell you if your anagram was correct.\n")
print("READY? GO!")

while play_again==True:

    first_word = str(input("Enter your first word: "))
    second_word = str(input(f"Now enter an anagram for - '{first_word}': "))

    find_anagrams(first_word, second_word)

    another_play = input("Play Again? Yes/No: ")
    if another_play.lower()=="yes" or another_play.lower()=="y":
        play_again=True
    elif another_play.lower()=="no" or another_play.lower()=="n":
        play_again=False
    else:
        print("Enter Yes or No")
        another_play = input("Play Again? Yes/No: ")

