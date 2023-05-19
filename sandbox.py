import datetime as dt

# date takes year month day. returns the format: 2023-05-03
some_date = dt.date(2023, 5, 3)

# returns the current date in the format: 2023-05-15 with no arguments.
this_day = dt.date.today()

# compute the difference in dates. Most recent first. returns the number of days.
delta = this_day - some_date # expected output: difference in days as an int.

# formats:  %Y=year as 2023   %m=month as 01,02,..   %d=day as 01,02,..
# strftime(format) method on a datetime object that returns a string of the date.
string_day = this_day.strftime('%Y-%m-%d')
# expected output: <class 'str'>

#strptime(date_string, format): parse a string into a datetime object
date_obj = dt.datetime.strptime(string_day, '%Y-%m-%d')
# expected output: <class 'datetime.datetime'>

array = list('copperloa')
 
def split_list(array, length):
  split_lists = []
  if len(array) <= length:
    return array
  while len(array) > 0:
    if len(array) <= length:
      length = len(array)
    inner_list = array[(length * -1):]
    split_lists.append(inner_list)
    del array[(length * -1):]
  return split_lists

# arr =split_list(array, 4)
# print(arr)
# print(array)