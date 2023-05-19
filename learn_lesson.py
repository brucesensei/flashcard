import random
import helpers
import index_gen
import questions
import display

unit = helpers.read_file('lesson_data.json')
english_list = helpers.read_file('english_list.json')
spanish_list = helpers.read_file('spanish_list.json')

def learn_lesson(vocab, kind='p'):
  """Uses two lists of index values to cycle through learning vocabulary and present different
  question types to the user."""
  if kind == 'p':
    vi = index_gen.vocab_indexes_practice(vocab)
    qi = index_gen.question_indexes_practice(vocab)
  if kind == 's':
    vi = [i for i in range(len(vocab))]
    random.shuffle(vi)
    qi = [4 for i in range(len(vocab))]
  if kind == 'e':
    vi = [i for i in range(len(vocab))]
    random.shuffle(vi)
    qi = [3 for i in range(len(vocab))]
  
  for i in range(len(vi)): # type: ignore
    vocab_index = vi[i] # type: ignore
    question_index = qi[i] # type: ignore
    if question_index == 0:
      display.training_word_display(vocab=vocab, index=vocab_index) # type: ignore
    if question_index == 1:
      questions.multiple_choice(word_list=spanish_list, vocab=vocab, 
        index=vocab_index, word_1='target', word_2='native') # type: ignore
    if question_index == 2:
      questions.multiple_choice(word_list=english_list, vocab=vocab, 
        index=vocab_index, word_1='native', word_2='target')  # type: ignore
    if question_index == 3: # type english word
      questions.type_word(vocab=vocab, index=vocab_index, word_1='target', word_2='native') # type: ignore
    if question_index == 4: # type spanish word
      questions.type_word(vocab=vocab, index=vocab_index, word_1='native', word_2='target') # type: ignore

def learn_main(unit, lesson_choice):
  lesson = display.get_lesson(unit, lesson_choice)
  practice_choices = [['e', 'Type English'], ['s', 'Type Spanish'], ['r', 'Regular practice']]
  if lesson[0] != 'date_visited':
    print('This lesson has been viewed.')
    lesson = display.display_lesson(lesson, marker='known')
    vocab = display.get_vocab(lesson)
    vocab = [i for i in vocab if i['known'] == False]
    user_choice = helpers.tell_listen(title='practice menu', menu_list=practice_choices)
    if user_choice == 'e':
      learn_lesson(vocab, kind='e')
    if user_choice == 's':
      learn_lesson(vocab, kind='s')
    if user_choice == 'r':
      learn_lesson(vocab)  
  else:
    lesson = display.display_lesson(lesson)
    vocab = display.get_vocab(lesson)
    pause = input('Press any key to continue')
    learn_lesson(vocab)
    learn_lesson(vocab, kind='e')
    learn_lesson(vocab, kind='s')
    helpers.set_date(lesson)
  lesson = display.display_lesson(lesson, marker='known')
  lesson = display.display_lesson(lesson, marker='difficult')
  unit[lesson_choice] = lesson
  helpers.write_file('lesson_data.json', unit) 
 