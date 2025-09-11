import random
import math

highscore = 0
score = 0
diff = 1

symbolarr = ["+", "-", "*", "/"]
print(f"Welcome to the math game! Current highscore: {highscore}")

def checkans(answer):
    global score, diff, highscore
    if answer:
        score += 1
        print(f"Correct! Current score: {score}")
        diff = math.ceil(score/20)
        run()
    else:
        print("Incorrect! Game over!")
        print(f"Final Score : {score}")
        if(score > highscore):
            highscore = score
        print(f"NEW HIGHSCORE! Highscore: {highscore}")
        retry = input("Do you want to play again? (Y/N): ")
        if retry == "y" or "Y" or "YES" or "yes" or "Yes":
            print(f'Current highscore: {highscore}')
            score = 0
            run()
        

def run():
    randomsymbol = random.randint(0,2)
    number1, number2 = random.randint(10*diff-9,10*diff), random.randint(10*diff-9,10*diff)
    print(f"What is {number1} {symbolarr[randomsymbol]} {number2}?")
    ans = float(input(">>> "))
    checkans(ans == eval(str(number1) + symbolarr[randomsymbol] + str(number2)))
    
run()