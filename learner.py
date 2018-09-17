# learner.py
# By Theodore Stumpf


def main():
  max_length = 10
  input_lenght = max_length * len(get_letter_list)

  language1_file = "english.txt"
  language2_file = "spanish.txt"

  with open(language1_file, 'r') as f
    language1_list = [line.strip("\n") for line in f.readlines()]
  with open(language2_file, 'r') as f
    language2_list = [line.strip("\n") for line in f.readlines()]

  training_data = []
  for word in language1_list:
    



# Convets a word to the long binary representation
def word_to_binary(word, max_len):
  # Convert word to maximum length
  full_word = word[:max_len] + " " * (max_len - len(word))
  full_word = word.upper()

  out = []
  letter_list = get_letter_list()
  for letter in full_word:
    for comp in letter_list:
      if comp == letter:
        out.append(1)
      else:
        out.append(0)

  return out


# Fetches the conversion table for letters
# This can be expanded to include necessary letters
def get_letter_list():
  out = [chr(x) for x in range(65, 90 + 1)]
  return out

# Run the program
main()