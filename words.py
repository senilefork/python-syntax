def print_upper_words(words):
    """prints words from a list in uppercase"""

    for word in words:
        print(word.upper())

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"])

def print_upper_words2(words):
    """print words from a list that start with e"""
    for word in words:
        if(word.startswith("e") or word.startswith("E")):
            print(word)


print_upper_words2(["Earth", "Mountain", "eagle", "bear"])


def print_upper_words3(words, must_start_with):
    """print words that begin with words from must_start_with, print in upper case"""

    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                


print_upper_words3(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})