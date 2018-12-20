#!/usr/bin/python3
import random

class Word():
    def search_random_word(self):
        with open('words.txt','r') as words_file:
            words = words_file.readlines()            
            line = random.randint(0, len(words)-1)
            word = words[line]
            return word.strip()
    
    def show_word(self, word, letter=None, hidden=None):
        if letter is None and hidden is None:
            return '_'*len(word)

        elif letter in word:
            hidden_word = self.show_hidden_word(word, letter, hidden)
            print(hidden_word)
            return hidden_word
        else:
            hidden_word = '_'*len(word)
            return hidden_word

    def show_hidden_word(self, word, letter, hidden=None):
        import ipdb; ipdb.set_trace()
        
        hidden_list = list(hidden)
        for item in word:
            print(item)

        return ''.join(hidden)

    def guessing_word(self):
        guessed = True
        word = self.search_random_word()
        new_hidden_word = self.show_word(word)
        print(new_hidden_word)
        #letter = input('Enter a letter: ')
        #hidden_word = self.show_word(word, letter, new_hidden_word)
        #print(hidden_word)
        while(guessed == True):
            letter = input('Enter a letter')
            hidden_word = self.show_word(word, letter, new_hidden_word)
            new_hidden_word = hidden_word
            print(hidden_word)
                

search_word = Word()
lets_play = search_word.guessing_word()