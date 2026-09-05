

# add code below ...
def palindrome(word):
  """Check if the given word is a palindrome.
  Args:
    word (str): The word to check.

    Returns:
      bool: True if the word is a palindrome, False otherwise.
  """
  punctuations = [",", ".", "?", "!", '"', "'", ":", ";", "-", "_", "(", ")", "[", "]", "{", "}", " "]
  cleaned_word = word.lower()

  for punctuation in punctuations:
    cleaned_word = cleaned_word.replace(punctuation, "")

  reversed_word = cleaned_word[::-1]
  return cleaned_word == reversed_word


def parentheses(sequence):
  """Check if the given sequence has balanced parentheses.
    Args:
      sequence (str): The sequence to check.

    Returns:
      bool: True if the sequence has balanced parentheses, False otherwise.
  """
  stack = []
  for char in sequence:
    if char == "(":
      stack.append(char)
    elif char == ")":
      # return False if there is no prior opening parentheses to match with
      if len(stack) == 0: 
        return False 
      stack.pop()
  return len(stack) == 0 