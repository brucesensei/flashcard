import helpers
from learn_lesson import learn_lesson
import display


def split_list(array, length):
  """Splits a list of vocab dictionaries into shorter lists. takes an array and list
  length and returns a list of lists containing vocab dictionaries"""
  split_lists = []
  if len(array) <= length:
    split_lists.append(array)
    return split_lists
  while len(array) > 0:
    if len(array) <= length:
      length = len(array)
    inner_list = array[(length * -1):]
    split_lists.append(inner_list)
    del array[(length * -1):]
  return split_lists

def update_unit(difficult_list, unit):
  """matches the difficult vocabulary to the unit vocabulary on the vocab id and
  updates them."""
  for update in difficult_list:
    for lesson in unit:              
      for i in range(len(lesson)):
        if type(lesson[i]) == dict:  
          if lesson[i]['id'] == update["id"]:
            lesson[i] = update
  return unit

def difficult_main(unit, difficult):
  # displays a list of the created lessons
  lessons = split_list(difficult, 4)
  for i in range(len(lessons)):
    print(f'Lesson  {i}')
  # gets the user choice for the lesson to practice.
  lesson_choice = helpers.tell_listen(ordered_list=lessons, tell=False, show_ordered_list=False)
  # get the lesson from the list
  lesson = display.get_lesson(lessons, lesson_choice)
  # display the words in the lesson
  display.display_lesson(lesson)
  puase = input('Press any key to start.')
  learn_lesson(lesson)
  lesson = display.display_lesson(lesson, marker='difficult')
  unit = update_unit(lesson, unit)
  helpers.write_file('lesson_data.json', unit)
