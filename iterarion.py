students = ("jim", "nicolas", "meg", "robert", "keanu", "chris", "johnny", "orlando", "margot", "amy")
mystudents = iter(students)

print(next(mystudents))
print(next(mystudents))
print(next(mystudents))
print(next(mystudents))
print(next(mystudents))
print(next(mystudents))
print(next(mystudents))
print(next(mystudents))
print(next(mystudents))
print(next(mystudents))


for x in students:
  print(x)