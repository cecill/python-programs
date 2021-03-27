while True: 
  print(' Who are you?')
  name = str(input())
  if name != 'Joe':
      continue
  print(' Hello, Joe. What is the password? (It is a fish.)')
  password = str(input())
  if password == 'swordfish':
      break
print(' Access granted.')



stop = str(input())

# this is something new 
