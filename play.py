import game


number = game.Generate_Random()
rand_number = number.generate()
game = game.Play_Game()

playing = True
while playing == True:
    given_number = raw_input('Enter the 4 digit number: ')
    if (number.is_correct(rand_number,given_number)):
        print ('Correct answer!')
    else:
        numbers_correct = number.numbers_correct(rand_number, given_number)
        print('Incorrect answer. You had {} number(s) correct'.format(numbers_correct))
    
        
