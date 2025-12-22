# Question 6: The Semordnilap Detector
# Please DO NOT modify the given function except the TODO part
# You may have your own functions if necessary


OFFICIAL_WORD_LIST = {
    "stop", "pots", "stressed", "desserts", "live", "evil",
    "drawer", "reward", "straw", "warts", "level", "madam",
    "racecar", "dog", "god", "hello", "python", "nametag",
    "gateman", "flow", "wolf", "war", "raw", "diaper", "repaid"
}


# ============================================================
# Base Class: Word
# ============================================================
class Word:
    """Base class for a word, handling basic string operations."""

    def __init__(self, text):
        """
        Initialize the Word object.
        Convert the input text to lowercase.
        """
        # TODO part
        # ------- Your code start here -------
        self.text = text.lower()
        # ------- End of your code -----------

    def get_reverse(self):
        """
        Returns the reversed form of the word's text.
        """
        # TODO part
        # ------- Your code start here -------
        return self.text[::-1]
        # ------- End of your code -----------

    def is_palindrome(self):
        """
        Checks if the word is a palindrome.
        Hint: Use the get_reverse() method.
        """
        # TODO part
        # ------- Your code start here -------
        return self.text == self.get_reverse()
        # ------- End of your code -----------

    def __str__(self):
        """
        Returns the string representation of the word.
        """
        # TODO part
        # ------- Your code start here -------
        return self.text
        # ------- End of your code -----------


# ============================================================
# Derived Class: ValidWord
# ============================================================
class ValidWord(Word):
    """
    A word that can be validated against an official dictionary.
    """

    # Class attribute: shared word list for all instances
    WORD_LIST = OFFICIAL_WORD_LIST

    def __init__(self, text):
        """
        Initialize the ValidWord object.
        Must call the parent constructor.
        """
        # TODO part
        # ------- Your code start here -------
        super().__init__(text)
        # ------- End of your code -----------

    def is_valid(self):
        """
        Checks if the word exists in the official word list.
        Returns True if valid, False otherwise.
        """
        # TODO part
        # ------- Your code start here -------
        return self.text in self.WORD_LIST
        # ------- End of your code -----------


# ============================================================
# Derived Class: Semordnilap
# ============================================================
class Semordnilap(ValidWord):
    """
    A class that represents a semordnilap.
    It inherits validity checking from ValidWord and
    basic string operations from Word.
    """

    def __init__(self, text):
        """
        Initialize the Semordnilap object.
        Must call the parent constructor.
        """
        # TODO part
        # ------- Your code start here -------
        super().__init__(text)
        # ------- End of your code -----------

    def is_semordnilap(self):
        """
        Determines whether the current word is a true semordnilap.

        A word is a semordnilap if and only if:
            1. The word itself is valid.
            2. The word is NOT a palindrome.
            3. The reversed word is also a valid word.

        Hint:
            - Use self.is_valid(), self.is_palindrome(), and self.get_reverse().
            - You may create a new ValidWord object for the reversed text.
        """
        # TODO part
        # ------- Your code start here -------
        reversedword = ValidWord(self.get_reverse())
        validity = reversedword.is_valid()
        return f"'{self.text}' : {self.is_valid() and not self.is_palindrome() and validity}"
        # ------- End of your code -----------


# ============================================================
# Main Testing Section
# ============================================================
if __name__ == "__main__":
    print("--- Semordnilap Check ---")

    test_words = [
        "stop", "stressed", "live", "drawer",
        "level", "dog", "madam", "hello", "python", "war", "diaper"
    ]

    # TODO: Loop through each word in test_words
    # 1. Create a Semordnilap object.
    # 2. Call is_semordnilap().
    # 3. Print results in the format: '<word>': True/False

    for word in test_words:
        # TODO part
        # ------- Your code start here -------
        obj = Semordnilap(word)
        print(obj.is_semordnilap())
        # ------- End of your code -----------
