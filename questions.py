import random
import helpers

def multiple_choice(word_list='', vocab='', index='', word_1='', word_2=''):
  """Takes a word list to choose random words for multiple choice generation. Takes the vocab list
  to get the quiz words. Takes the index as the index for the quiz word. Takes 'target', or 'native'
  for word_1 and _word to to access the target or native vocabulary on the word. Returns nothing"""
  key_word = vocab[index][word_1] # type: ignore
  quiz_word = vocab[index][word_2] # type: ignore
  multiple_choices = random.choices(word_list, k=3)
  multiple_choices.append(key_word)
  random.shuffle(multiple_choices)
  print(f'The meaning of: {quiz_word}')
  for i in range(len(multiple_choices)):
    print(f'{i}   {multiple_choices[i]}')
  user_choice = helpers.tell_listen(ordered_list=multiple_choices, tell=False)
  if multiple_choices[user_choice] == key_word: # type: ignore
    print('correct\n\n\n\n\n')
  else:
    print(f'The answer is: {key_word}\n\n\n\n\n')

def type_word(vocab='', index='', word_1='', word_2=''):
  """Takes the vocab list to get the word for the question. Takes the index to get the specific
  word from the vocab list. takes 'target', or 'native' to supply the target or natvie word.
  Returns nothing"""
  key_word = vocab[index][word_1] # type: ignore
  quiz_word = vocab[index][word_2] # type: ignore
  print(key_word)
  attempt = input()
  if attempt == quiz_word:
    print('Correct\n\n\n\n\n')
  else:
    print(f'The answer is: {quiz_word}\n\n\n\n\n')