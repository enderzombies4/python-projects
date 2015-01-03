import random 


answers = ['Yes','No','My Sources Say No','For Sure',
           'Reply Hazy; Try Again']

print('''
Welcome To The Magic 8 Ball!
Enter Your Question Below:
''')

while True:
    question = input('> ')
    answer = random.choice(answers)
    print(answer)
