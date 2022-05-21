# ***************           PYTHON FOR DATA SCIENCE          *************** #

# ***************             CASE STUDY - CYPHER            *************** #

# Exercise 1
#  Create a dictionary letters with keys consisting of the numbers
#  from 0 to 26, and values consisting of the lowercase letters of
#  the English alphabet, including the space ' ' at the end.

# Let's look at the lowercase letters.
import string
# string.ascii_lowercase
#
# # We will consider the alphabet to be these letters, along with a space.
# alphabet = string.ascii_lowercase + " "
#
# # create `letters` here!
# letters = {i:alphabet[i] for i in range(27)}

# Exercise 2
#  alphabet and letters are already defined. Create a dictionary encoding
#  with keys being the characters in alphabet and values being numbers
#  from 0-26, shifted by an integer encryption_key=3. For example, the key
#  a should have value encryption_key, key b should have value
#  encryption_key + 1, and so on. If any result of this addition is less
#  than 0 or greater than 26, you can ensure the result remains within
#  0-26 using result % 27.

alphabet = string.ascii_lowercase + " "
# code_tip_py3_dict_creation_with_enumerate
letters = dict(enumerate(alphabet))

# encryption_key = 3
# encoding = {letters[i]:(encryption_key + i) % 27 for i in letters.keys()}

# Exercise 3
#
# * alphabet and letters are preloaded from the previous exercise.
#   Write a function caesar(message, encryption_key) to encode a
#   message with the Caesar cipher.
# * Use your code from Exercise 2 to find the value of encoding for
#   each letter in message.
# * Use these values as keys in the dictionary letters to determine
#   the encoded letter for each letter in message.
# * Your function should return a string consisting of these encoded letters.
# * Use caesar to encode message using encryption_key = 3, and save the
#   result as encoded_message.
# * Print encoded_message.

message = "hi my name is caesar"


def caesar(message, encryption_key):
    encoding = {letters[i]: (encryption_key + i) % 27 for i in letters.keys()}
    encoded_message = ''.join(letters[encoding[letter]] for letter in message)
    return encoded_message


encoded_message = caesar(message, encryption_key=3)
print(encoded_message)

# Exercise 4
#
# * Note that encoded_message is already loaded from the previous problem.
#   Use caesar to decode encoded_message using encryption_key = -3.
# * Store your decoded message as decoded_message.
# * Print decoded_message. Does this recover your original message?

decoded_message = caesar(encoded_message, encryption_key=-3)
print(decoded_message)
decoded_message == message
