# A test script for PyEcho
# By Scott Vanderlind, December 31 2014

import PyEcho, getpass

email = raw_input("Email: ")
password = getpass.getpass()
echo = PyEcho.PyEcho(email, password)

if echo:
   tasks = echo.tasks()
   print tasks
   for task in tasks:
      res = echo.delete_task(task)
      print res
      print res.text

