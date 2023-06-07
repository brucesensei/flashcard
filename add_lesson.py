import helpers
import create_lesson_data
import display

message ='''
- Enter up to 10 vocabulary pairs with the target language first and native language second. 
- Separate each entry with a comma.
- Do not insert a comma following the last entry.
- Press enter when you are finished.

Example: uno, one, dos, two, te quiero, I love you
'''

def check_lesson_titles(data):
  """Takes a list of the lesson titles and compares it against the new titl"""
  lesson_titles = []
  for i in range(len(data)):
    lesson_titles.append(data[i][-1])
  while True:
    new_title = input('Enter the title for the lesson. ')
    if new_title in lesson_titles:
      print(f'The title {new_title} already exists.')
      continue
    break
  return new_title
  
def enter_new_lesson():
  print(message)
  pairs = input()
  vocab_list = pairs.split(',')
  vocab_list = [i.strip() for i in vocab_list]
  return vocab_list
 
def sort_vocab(vocab_list):
  spanish = []
  english = []
  for i in range(len(vocab_list)):
    if i % 2 == 0:
      spanish.append(vocab_list[i])
    else:
      english.append(vocab_list[i])
  return spanish, english

def add_main():
  data = helpers.read_file('lesson_data.json')
  spanish_words = helpers.read_file('spanish_list.json')
  english_words = helpers.read_file('english_list.json') 
  while True:
    while True:
      vocab_list = enter_new_lesson()
      if len(vocab_list) % 2 != 0:
        print('An entry may be missing a pair. Please re-enter the information.')
        continue
      break  
    new_title = check_lesson_titles(data)
    spn, eng = sort_vocab(vocab_list)
    new_lesson = create_lesson_data.lesson_generator(spn, eng)
    new_lesson.append(new_title)
    display.display_lesson(new_lesson)
    option_list = [['a', 'Add the new list'], ['s','Start over'],['r', 'Do nothing and return to main menu']]
    user_choice = helpers.tell_listen(title='new lesson options', menu_list=option_list)
    if user_choice == 'r':
      break
    if user_choice == 's':
      continue
    if user_choice == 'a':
      spanish_words.extend(spn)
      spanish_words =  list(set(spanish_words))
      english_words.extend(eng)
      english_words = list(set(english_words))
      data.append(new_lesson)
      helpers.write_file('spanish_list.json', spanish_words)
      helpers.write_file('english_list.json', english_words)
      helpers.write_file('lesson_data.json', data)
      print(f'{new_title} has been added.')
      break
