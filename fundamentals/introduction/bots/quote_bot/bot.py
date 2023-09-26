from api_responses import results
import random
import time

count = 0


def tellquote():
    quote = random.choice(results)
    global count
    if count < 1:
        print("Do you want to read a good quote?")
    else:
        print("Do you want to read another quote?")
    user_input = input()

    if user_input.lower() == "y":
        print(quote['text'])
        print("Author " + quote['author'])
        time.sleep(2)
        print("Good Quote")
        count += 1
        tellquote()

    if user_input.lower() == "n":
        print("Goodbye")
    if user_input != "y" and user_input != "n":
        print("I do not understand?")

tellquote()