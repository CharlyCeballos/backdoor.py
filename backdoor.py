from datetime import datetime
import os, shutil
os.system('cls') # TODO: delete this

def add_months(current_date, months_to_add):
  new_date = datetime(current_date.year + (current_date.month + months_to_add - 1) // 12,
                      (current_date.month + months_to_add - 1) % 12 + 1,
                      current_date.day, current_date.hour, current_date.minute, current_date.second)
  return new_date

def datetime_to_hex(datetime):
  timestamp = datetime.timestamp()
  hexa = hex(int(round(timestamp)))
  return hexa


print('****************************') # TODO: delete this
file_name = '99934jhdiej894039d'
current_date = datetime.now()
archive_data = datetime_to_hex(current_date)


current_directory = os.getcwd()
root = current_directory.split('\\')[0]
users = current_directory.split('\\')[1]
current_user = current_directory.split('\\')[2]
new_path = f'{root}\\{users}\\{current_user}'
os.chdir(new_path)

if os.path.exists(f'{new_path}\\{file_name}.png'):
  shutil.copy(f'{file_name}.png', f'{file_name}.txt')

  new_file = open(f'{file_name}.txt', 'r')
  content = new_file.read()
  new_file.close()
  os.remove(f'{file_name}.txt')

  months_to_add = 1
  print(int(content, 16))
  datetime_to_timestamp = datetime.fromtimestamp(int(content, 16))
  new_date = add_months(datetime_to_timestamp, months_to_add)
  check_date = datetime_to_hex(new_date)
  print(int(check_date, 16))
  print(content)
  print(check_date)

  if int(content, 16) <= int(check_date, 16):
    print('REAL')
  else:
    print('FAKE')

  
else:
  print(archive_data)
  file = open(f"{file_name}.png","x")
  file.write(archive_data)
  file.close()








# https://www.epochconverter.com/