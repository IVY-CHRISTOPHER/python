from api_response import results
import random
import time

count = 0

def telljoke():
    joke = random.choice(results)
    global count
    # print(count)
    if count < 1:
        print("Do you want to hear a good joke?")
    else:
        print("Do you want to hear another awesome joke?")
    user_input = input()

    if user_input.lower == "y":
        print(joke['setup'])
        time.sleep(5)
        print(joke['punchline'])
        time.sleep(2)
        print("Thats so funny!")
        time.sleep(2)
        print("right?")
        time.sleep(2)
        count += 1
        telljoke()

    if user_input.lower == "n":
        print("darn...")
    if user_input != "y" and user_input != "n":
        print("I do not understand what you said")
telljoke()