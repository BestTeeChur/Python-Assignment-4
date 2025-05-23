import random
import time

#This section creates a list of all the possible replies and prints out an ASCII 8ball with a pause between each line. This is to indicate that the code has started running.
answers = ["It is certain", "It is decidely so", "Without a doubt", "Yes Definitely", "You may rely on it", "As I see it, yes", "Most Likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy, try again", "Ask again later", "Better not tell you now", "Cannot Predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very Doubtful"]
print("  .-'''-.")
time.sleep(.5)
print(" /   _   \\")
time.sleep(.5)
print(" |  (8)  |")
time.sleep(.5)
print(" \   ^   /")
time.sleep(.5)
print("  '-...-'")

#The main function of the 8ball. 
def ask_eight_ball():
    #asks the user to input a name and questions. .upper() turns the string into all caps. 
    print("Hello! Welcome to Pj's Magic 8 ball")
    name = input(What is your name? ")
    #capitalizes the name
    cap_name = name.upper()
    question = input("What is your question? ")
    cap_question = question.upper()
    #This uses random to create a random integer between two numbers, in this case 0 and the length of the list minus 1 to account for 0 indexing. 
    get_the_i = random.randint(0, len(answers))
    #this selectes the answer by using the random number as the index from the list
    answer = answers[get_the_i]

    #fun filler to pretend like it's thinking
    print(f"{cas_name}, you asked '{cap_quesrion}'.")
    print("Pondering the Orb")
    time.sleep(random.randint(1, 5))
    print("🔮 ✨ 🔮")
    time.sleep(1)
    print(f"{answer}")
    ask_again = input("Would you like to ask again? yes/no ")
    #runs play again to check if user wants another round
    play_again(ask_again)

#if the user wants to play again, this function is called to ask the question again
    play_again(user_answer2)

#play again is the logic for deciding how the player answered about another question
def play_again(user_answer):
   # write this function
        
#runs the game function    
ask_8_ball()