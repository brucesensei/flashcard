import helpers

def get_vocab(lesson):
  """Takes the lesson list. Removes list items containing lesson metadata. Returns a list of lesson vocab."""
  return lesson[2:-1]

def display_lessons(unit):
  """Takes the unit list. Displays the lesson index and the lesson title. Returns nothing"""
  for i in range(len(unit)):
    # this is the index of the list of numbers determining review day spacing
    if len(unit[i][1]) == 1:
      message = 'Completed'
    elif 'date_visited' != unit[i][0]:
      message = 'Learning'
    else:
      message = ''
    print(f'{i} {unit[i][-1]}  {message}')

def get_lesson(unit, user_choice):
  """Takes the unit list and the user_choice as an int. Returns the chosen lesson"""
  return unit[user_choice]

def toggle_known(vocab, lesson):
  """Takes a lesson to pass to display_lesson. Takes vocab and allows the user to mark
  the vocabulary word as either known or not by toggling the 'known' key. displays the
  lesson back to the user and breaks out of the loop with keyboard prompt 's'. Returns nothing."""
  while True:
    message = 'Enter a word number to mark or unmark a word as KNOWN or press "s" to contiune.'
    user_choice = helpers.tell_listen(ordered_list=vocab , menu_list=['s', 'start'], message=message, tell=False)
    if user_choice != 's':
      word = vocab[user_choice]
      if word['known'] == True:
        word['known'] = False
        word['difficult'] = False
      else:
        word['known'] = True
        word['difficult'] = False
      display_lesson(lesson)
    else:
      return lesson
 
def toggle_difficult(vocab, lesson):
  """Takes a lesson to pass to display_lesson. Takes vocab and allows the user to mark
  the vocabulary word as either difficult or not by toggling the 'difficult' key. displays the
  lesson back to the user and breaks out of the loop with keyboard prompt 's'. Returns nothing."""
  while True:
    message = 'Enter a word number to mark or unmark a word as DIFFICULT or press "s" to continue.'
    user_choice = helpers.tell_listen(ordered_list=vocab , menu_list=['s', 'start'], message=message, tell=False)
    if user_choice != 's':
      word = vocab[user_choice]
      if word['difficult'] == True:
        word['difficult'] = False
        word['known'] = False
      else:
        word['difficult'] = True
        word['known'] = False
      display_lesson(lesson)
    else:
      return lesson
  
def display_word(vocab, index=''):
  """Takes a list of vocab words and an int for the vocab list index.
  Displays 'target', 'native', and if true, 'known' in a formatted string. Returns nothing."""
  message = ''
  if vocab[index]['known']:
    message = '... known'
  if vocab[index]['difficult']:
    message = '... difficult'
  print(f"\
{index} \
{vocab[index]['target']}\
{'.' * (80 - len(vocab[index]['target']) - len(vocab[index]['native']))}\
{vocab[index]['native']} {message}\n")
    
def word_wrapper(func, vocab, index=''):
  """Wraps a function's print statement in lines and white space. Takes a function, the word list
  and the index to access the word in the word list."""
  def wrapper():
    print(f'\n\n\n\n{"=" * 85}\n')
    func(vocab, index)
    print(f'\n{"=" * 85}\n\n\n\n\n\n\n\n\n')
  return wrapper

def training_word_display(vocab='', index=''):
  word_wrapper(display_word, vocab, index)()
  input('Continue')

def display_lesson(lesson, marker=''):
  """Takes a lesson list. uses (get_vocab, display_word, toggle_known) to display only lesson vocab
  and gives the user the options to mark words KNOWN / diffictult. optionally eturns MARKED vocab list"""
  title = lesson[-1]
  if type(title) == dict:
    # case where words are only dict items.
    title = 'difficult words'
    vocab = lesson
  else:
    # case where words contains meta data other than dict items.
    title = lesson[-1]
    vocab = get_vocab(lesson)
  print(title.upper())
  print("=" * len(title),"\n")
  for i in range(len(vocab)):
    display_word(vocab, index=i) # type: ignore
  if marker == 'known':
    lesson = toggle_known(vocab, lesson)
    return lesson
  if marker == 'difficult':
    lesson = toggle_difficult(vocab, lesson)
  return lesson