number  = 7 



while True: 

    user_input  =  input('Would you like to play? (Y/n) ') #will default to Y  

    if user_input == 'n':
        break

    user_number = int(input('Guess our number: '))
    if user_number == number:
        print ('You guessed correctly!!')
    elif abs(number - user_number) == 1:
        print('You were off by one.')
    else:
        print('Sorry, it\'s wrong!')
    
friends = ['rolf', 'jen', 'bob', 'anny']

for friend in friends:
    print(f'{friend} is my friend. ')

for friend in range(3):
    print(f'{friend} is my friend. ')

numbers  = [1, 2, 3, 4, 5, 6]
total  = sum(numbers)
amount = len(numbers)
print(total)
print(amount)