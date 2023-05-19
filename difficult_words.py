import helpers
from learn_lesson import learn_lesson
import display

# difficult = [{
#       "id": "55051f1f-b80a-45a7-afea-3e90f1da77a6",
#       "target": "trabajar",
#       "native": "to work",
#       "known": False,
#       "difficult": True
#     },
#     {
#       "id": "be02b170-e3c1-4871-ae74-29c2c7f33d85",
#       "target": "estudiar",
#       "native": "to study",
#       "known": False,
#       "difficult": True
#     },
#     {
#       "id": "e450c2dd-a8d9-46fb-9f2b-cd0e054962f7",
#       "target": "dedicarse a",
#       "native": "to work as",
#       "known": False,
#       "difficult": True
#     },
#     {
#       "id": "3937a3b0-785f-4ba3-9612-5f41bc4f041c",
#       "target": "por cierto",
#       "native": "by the way",
#       "known": False,
#       "difficult": True
#     },
#     {
#       "id": "fe10e63a-af44-4b16-bda4-172408029619",
#       "target": "\u00bfa qu\u00e9 te dedicas?",
#       "native": "what do you do?",
#       "known": False,
#       "difficult": True
#     },
#     {
#       "id": "d0d9ab56-ef88-420e-9f96-1cda10235084",
#       "target": "el profesor; la profesora",
#       "native": "professor",
#       "known": False,
#       "difficult": True
#     },
#     {
#       "id": "5f55cdfe-7d4d-4ba6-b984-a164dd21d746",
#       "target": "el m\u00e9dico; la m\u00e9dica",
#       "native": "doctor",
#       "known": False,
#       "difficult": True
#     },
#     {
#       "id": "b144bfe6-c353-4fa2-902f-26ed16dbaccd",
#       "target": "los idiomas",
#       "native": "languages",
#       "known": False,
#       "difficult": True
#     },
#     {
#       "id": "e37d5977-5d5c-4987-94f6-b783c01665f8",
#       "target": "soy estudiante",
#       "native": "I am a student",
#       "known": False,
#       "difficult": True
#     },
#     {
#       "id": "71e17f98-409c-45db-bdcc-229f499ce005",
#       "target": "estudio arquitectura",
#       "native": "I study architecture",
#       "known": False,
#       "difficult": True
#     },]

def split_list(array, length):
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
