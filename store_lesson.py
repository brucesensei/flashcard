import helpers
import display
from time import sleep


def store_main():
  unit = helpers.read_file('lesson_data.json')
  storage_file = helpers.read_file('store.json')
  while True:
    display.display_lessons(unit)
    option_list = [['r', 'Return to main menu or']]
    message = 'Choose the number of the lesson to store.'
    user_choice = helpers.tell_listen(title='Store lesson',
      message=message,
      ordered_list=unit,
      menu_list=option_list,
      show_ordered_list=False
      )
    if user_choice == 'r':
        break
    else:
      lesson = unit.pop(user_choice)
      title = lesson[-1]
      storage_file.append(lesson)
      helpers.write_file('store.json', storage_file)
      helpers.write_file('lesson_data.json', unit)
      print(f'{title} has been stored')
      sleep(3)
