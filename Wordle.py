import random



word_list = ["reina","caigo","casco","grasa","manta","breve"]


class Word:
    def __init__(self) -> None:
        pass
    def get_word():
        word_correct = random.choice(word_list)
        print(word_correct)
        Word.Play(word_correct)
    

    def Play(word_correct):
        asking = True
        while asking == True:

            print("Guess the word")
            print("|| || || || ||")
            answer = input()
            if len(answer) != 5:
                print("Sorry, It doesnt have 5 letters")
            else:
                asking = False
                Word.Checking(answer,word_correct)

    def Checking(answer,word_correct):
        for position in range(len(answer)):
            if answer[position] == word_correct[position]:
                print(f"Yep, {answer[position]} is correct!!!")
                continue
            else:
                if str(word_correct).count((answer[position])) != 0:
                    print (f"The letter {answer[position]} is in another place")
                else:
                    print(f"The letter {answer[position]} is not in the word")
        print("me ejecuto")
        Word.Play(word_correct)
        
    

    
Word.get_word()
