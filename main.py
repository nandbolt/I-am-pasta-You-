# Personality scores
hardy = 10     #1
docile = 10    #2
brave = 10     #3
jolly = 10     #4
impish = 10    #5
naive = 10     #6
timid = 10     #7
hasty = 10     #8
sassy = 10     #9
calm = 10      #10
relaxed = 10   #11
lonely = 10    #12
quirky = 10    #13

# Pasta art
spaghet_art = '~==================~'
thin_art = '~~~~~~~~~~~~~~~~~~~'
fett_art = ',----------------,\n\'----------------\''
penne_art = ' _____\n/___O/'
elbow_art = ' __\n(/\)'
shell_art = '(O'
farf_art = '\~v~/\n/~^~\\'
angel_art = '__________________\n'
rotini_art = 'x/=/=/x'
rigatoni_art = ' ___ \nO___)'
lasag_art = '~~~~~\n|   |\n~~~~~'
tort_art = '{O}'
orzo_art = '<>'

# User
user_input = ''
user_pasta_name = 'Insert pasta name here.'
user_pasta_art = 'Insert pasta art here'

# Welcome text
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print()
print('Welcome to "I am pasta! You?",')
print('where we can determine your inner')
print('pasta self!')
print()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# Start prompt
print()
input('Press enter to start!')
print('Pastarific!')
print()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print()
print('*To choose, enter the number next to the choice*')
print()

# Q1 (Naive)
print('Q.1: You wake up and realize you\'re on a deserted island. What do you do?')
print()
print('1. Cry.')
print('2. "Cool! An island!"')
print('3. Look for food.')
print('4. Lay in the sand.')
user_input = input()
if ('1' in user_input):
  docile += 1
  timid += 2
  relaxed -= 1
  print('[Input = 1]')
elif ('2' in user_input):
  naive += 4
  jolly += 1
  timid -= 1
  print('[Input = 2]')
elif ('3' in user_input):
  calm += 2
  hasty += 1
  hardy += 2
  relaxed -= 1
  print('[Input = 3]')
elif ('4' in user_input):
  relaxed += 2
  calm += 1
  lonely += 1
  hasty -= 2
  print('[Input = 4]')
else:
  hasty += 1
  quirky += 1
  print('[Input = 5]')

# Q2 (Relaxed)
print()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print()
print('Q.2: Oh no! You realized you have a homework due tonight and you haven\'t even started.')
print()
print('1. "Eh, I guess I\'ll use my drop."')
print('2. Skip class and focus on the homework.')
print('3. Ask your friend for help.')
print('4. Panick.')
user_input = input()
if ('1' in user_input):
  calm += 1
  relaxed += 4
  hasty -= 1
  print('[Input = 1]')
elif ('2' in user_input):
  lonely += 1
  hardy += 2
  hasty += 2
  docile -= 2
  print('[Input = 2]')
elif ('3' in user_input):
  calm += 2
  hasty += 1
  hardy += 2
  lonely -= 3
  print('[Input = 3]')
elif ('4' in user_input):
  hasty += 1
  timid += 2
  lonely += 1
  relaxed -= 2
  print('[Input = 4]')
else:
  hasty += 1
  quirky += 1
  print('[Input = 5]')

# Q3 (Lonely)
print()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print()
print('Q.3: One morning you wake up with superpowers! You can now')
print()
print('1. breath fire!')
print('2. use alchemy.')
print('3. fly.')
print('4. turn invisible.')
user_input = input()
if ('1' in user_input):
  impish += 3
  naive += 3
  sassy += 4
  quirky += 2
  calm -= 2
  print('[Input = 1]')
elif ('2' in user_input):
  calm += 3
  hardy += 2
  naive -= 3
  print('[Input = 2]')
elif ('3' in user_input):
  brave += 2
  naive += 1
  hasty += 1
  quirky -= 2
  print('[Input = 3]')
elif ('4' in user_input):
  lonely += 4
  timid += 3
  impish += 2
  brave -= 2
  print('[Input = 4]')
else:
  hasty += 1
  quirky += 1
  print('[Input = 5]')

# Q4
print()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print()
print('Q.4: You find $100 on the floor after class. What do you do?')
print()
print('1. Leave it there.')
print('2. "I\'ll take it for now, if anybody asks I\'ll give it to them."')
print('3. Hold on to it. Next class, you\'ll take it out and ask if anyone lost it.')
print('4. "Money!"')
user_input = input()
if ('1' in user_input):
  docile += 2
  timid += 3
  naive += 1
  brave -= 1
  print('[Input = 1]')
elif ('2' in user_input):
  docile += 3
  timid += 2
  relaxed += 1
  quirky -= 1
  print('[Input = 2]')
elif ('3' in user_input):
  hardy += 2
  brave += 2
  relaxed += 2
  timid -= 2
  impish -= 3
  print('[Input = 3]')
elif ('4' in user_input):
  naive += 1
  jolly += 3
  brave += 1
  impish += 1
  timid -= 1
  print('[Input = 4]')
else:
  hasty += 1
  quirky += 1
  print('[Input = 5]')

# Q5
print()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print()
print('Q.5: You arrive late to a dinner with your friends at a restaurant. Their entrees just arrive. What do you order?')
print()
print('1. Desert.')
print('2. An entree.')
print('3. Just water.')
print('4. A shareable appetizer.')
user_input = input()
if ('1' in user_input):
  quirky += 2
  jolly += 1
  sassy += 2
  hardy -= 2
  print('[Input = 1]')
elif ('2' in user_input):
  jolly += 1
  sassy += 1
  hardy += 2
  timid -= 1
  print('[Input = 2]')
elif ('3' in user_input):
  docile += 2
  lonely += 4
  hasty += 1
  brave -= 2
  print('[Input = 3]')
elif ('4' in user_input):
  relaxed += 3
  calm += 1
  brave += 2
  naive += 3
  docile -= 1
  print('[Input = 4]')
else:
  hasty += 1
  quirky += 1
  print('[Input = 5]')

# Q6
print()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print()
print('Q.6: You notice an attractive person is sitting by themselves in class as you walk in. What do you do?')
print()
print('1. Sit next to your friends. Maybe you\'ll catch them after class.')
print('2. Ignore them and find an empty seat close to you.')
print('3. Sit next to them and start a conversation.')
print('4. Sit near them and hope they talk to you.')
user_input = input()
if ('1' in user_input):
  jolly += 3
  relaxed += 2
  timid += 1
  lonely -= 1
  print('[Input = 1]')
elif ('2' in user_input):
  lonely += 3
  calm += 2
  docile += 1
  brave -= 1
  print('[Input = 2]')
elif ('3' in user_input):
  jolly += 2
  hardy += 2
  brave += 5
  sassy += 2
  hasty += 2
  timid -= 3
  docile -= 1
  print('[Input = 3]')
elif ('4' in user_input):
  docile += 4
  timid += 5
  brave -= 2
  hasty -= 1
  print('[Input = 4]')
else:
  hasty += 1
  quirky += 1
  print('[Input = 5]')

# Q7
print()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print()
print('Q.7: The power goes out in your home. What do you do?')
print()
print('1. Scroll on your phone.')
print('2. Sit quietly and wait for it to come back on.')
print('3. Go outside.')
print('4. Try to continue whatever you were doing without power.')
user_input = input()
if ('1' in user_input):
  sassy += 2
  relaxed += 3
  hasty -= 1
  print('[Input = 1]')
elif ('2' in user_input):
  docile += 3
  relaxed += 1
  impish -= 2
  print('[Input = 2]')
elif ('3' in user_input):
  hardy += 2
  jolly += 2
  calm += 2
  docile -= 2
  print('[Input = 3]')
elif ('4' in user_input):
  naive += 1
  hardy += 3
  hasty += 2
  sassy -= 1
  print('[Input = 4]')
else:
  hasty += 1
  quirky += 1
  print('[Input = 5]')

# Q8
print()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print()
print('Q.8: What is your favorite color?')
print()
print('1. Ocean Blue')
print('2. Royal Purple')
print('3. Dark Red')
print('4. Longhorn Orange')
print('5. It\'s not here!')
user_input = input()
if ('1' in user_input):
  calm += 3
  sassy -= 2
  print('[Input = 1]')
elif ('2' in user_input):
  sassy += 3
  timid -= 2
  print('[Input = 2]')
elif ('3' in user_input):
  impish += 3
  relaxed -= 2
  print('[Input = 3]')
elif ('4' in user_input):
  hardy += 3
  impish -= 2
  print('[Input = 4]')
else:
  quirky += 3
  hasty += 1
  timid -= 2
  print('[Input = 5]')

# Show personality score
print()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print()
print('Personality score:')
print('Hardy:',hardy)         #1
print('Docile:',docile)       #2
print('Brave:',brave)         #3
print('Jolly:',jolly)         #4
print('Impish:',impish)       #5
print('Naive:',naive)         #6
print('Timid:',timid)         #7
print('Hasty:',hasty)         #8
print('Sassy:',sassy)         #9
print('Calm:',calm)           #10
print('Relaxed:',relaxed)     #11
print('Lonely:',lonely)       #12
print('Quirky:',quirky)       #13

# Determine pasta

# 1: Hardy pasta
if (hardy >= docile and hardy >= brave and hardy >= jolly and
    hardy >= impish and hardy >= naive and hardy >= timid and
    hardy >= hasty and hardy >= sassy and hardy >= calm and
    hardy >= relaxed and hardy >= lonely and hardy >= quirky):
  user_pasta_name = 'spaghetti'
  user_pasta_art = spaghet_art
# 2: Docile pasta
elif (docile >= brave and docile >= jolly and docile >= impish and
      docile >= naive and docile >= timid and docile >= hasty and
      docile >= sassy and docile >= calm and docile >= relaxed and
      docile >= lonely and docile >= quirky):
  user_pasta_name = 'elbow macaroni'
  user_pasta_art = elbow_art
# 3: Brave pasta
elif (brave >= jolly and brave >= impish and brave >= naive and
      brave >= timid and brave >= hasty and brave >= sassy and
      brave >= calm and brave >= relaxed and brave >= lonely and
      brave >= quirky):
  user_pasta_name = 'rotini'
  user_pasta_art = rotini_art
# 4: Jolly pasta
elif (jolly >= impish and jolly >= naive and jolly >= timid and
      jolly >= hasty and jolly >= sassy and jolly >= calm and
      jolly >= relaxed and jolly >= lonely and jolly >= quirky):
  user_pasta_name = 'rigatoni'
  user_pasta_art = rigatoni_art
# 5: Impish pasta
elif (impish >= naive and impish >= timid and impish >= hasty and
      impish >= sassy and impish >= calm and impish >= relaxed and
      impish >= lonely and impish >= quirky):
  user_pasta_name = 'penne rigate'
  user_pasta_art = penne_art
# 6: Naive pasta
elif (naive >= timid and naive >= hasty and naive >= sassy and
      naive >= calm and naive >= relaxed and naive >= lonely and
      naive >= quirky):
  user_pasta_name = 'lasagna'
  user_pasta_art = lasag_art
# 7: Timid pasta
elif (timid >= hasty and timid >= sassy and timid >= calm and
      timid >= relaxed and timid >= lonely and timid >= quirky):
  user_pasta_name = 'fettuccine'
  user_pasta_art = fett_art
# 8: Hasty pasta
elif (hasty >= sassy and hasty >= calm and hasty >= relaxed and
      hasty >= lonely and hasty >= quirky):
  user_pasta_name = 'thin spaghetti'
  user_pasta_art = thin_art
# 9: Sassy pasta
elif (sassy >= calm and sassy >= relaxed and sassy >= lonely and
      sassy >= quirky):
  user_pasta_name = 'tortellini'
  user_pasta_art = tort_art
# 10: Calm pasta
elif (calm >= relaxed and calm >= lonely and calm >= quirky):
  user_pasta_name = 'orzo'
  user_pasta_art = orzo_art
# 11: Relaxed pasta
elif (relaxed >= lonely and relaxed >= quirky):
  user_pasta_name = 'angel hair'
  user_pasta_art = angel_art
# 12: Lonely pasta
elif (lonely >= quirky):
  user_pasta_name = 'shells'
  user_pasta_art = shell_art
# 13: Quirky pasta
else:
  user_pasta_name = 'farfalle'
  user_pasta_art = farf_art

# Conclusion
print()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print()
print()
print(user_pasta_art)
print()
print('Your inner pasta is the ',user_pasta_name,'!',sep='')
print()
print()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
input('Press enter to quit.')
