import helpers
import display
from time import sleep

stored = helpers.read_file('store.json')
unit = helpers.read_file('lesson_data.json')


def view_stored_main():
  while True:
    display.display_lessons(stored)
    option_list = [['g', 'Go back to the main menu'],
                   ['r', 'Restore the lesson'],
                   ['d', 'delete lesson'],
                   ]
    user_choice = helpers.tell_listen(
      title='Stored lessons',
      menu_list=option_list, 
      )
    if user_choice == 'g':
        break
    
    display.display_lessons(stored)
    if user_choice == 'd':
      lesson_choice = helpers.tell_listen(
        message = 'Enter the number of the lesson to delete. This action is permanent.',
        ordered_list=stored,
        show_ordered_list=False
      )
      lesson = stored.pop(lesson_choice)
      title = lesson[-1]
      print(f'{title} has been deleted')
      helpers.write_file('store.json', stored)
      sleep(3)
    
    if user_choice == 'r':      
      lesson_choice = helpers.tell_listen(
        message='Enter the number of the lesson to restore.',
        ordered_list=stored,
        show_ordered_list=False
      )
      lesson = stored.pop(lesson_choice)
      title = lesson[-1]
      unit.append(lesson)
      helpers.write_file('store.json', stored)
      helpers.write_file('lesson_data.json', unit)
      print(f'{title} has been restored to the main lessons')
      sleep(3)

    
    