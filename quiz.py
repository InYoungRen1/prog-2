# quiz

answer_correct = 0

print("Hello I'm William and I want to play a game with you!")
print("Reminder: please don't print random words, numbers and punctuation in the answers.")
# Question 1

answer_one = float(input("Now please answer question one: 25*4"))
if answer_one == 100:
    print("You are correct")
    answer_correct += 1
else:
    print("you are wrong")

if answer_correct != 1:
    print(f"You have {answer_correct} answer correct.")

# Question 2

answer_two = input("Please answer question 2: What is my name?").lower().strip("!.,?")
if answer_two == "william":
    print("you are correct")
    answer_correct += 1
else:
    print("You are wrong")

if answer_correct != 1:
    print(f"You have {answer_correct} answer correct.")

# Question 3

print("Question 3: Is William cool?")
answer_three = input("which one of these are correct: \na. yes\nb. no\nc. maybe").lower().strip("!,.?")
if answer_three == "a":
    print("you are very correct")
    answer_correct += 1
else:
    print("you are wrong")

if answer_correct != 1:
    print(f"You have {answer_correct} answer correct.")

# Question 4

answer_four = float(input("Question 4: what is 150+25*4"))
if answer_four == 250:
    print("you are correct")
    answer_correct += 1
else:
    print("you are wrong")

if answer_correct != 1:
    print(f"You have {answer_correct} answer correct.")

# Question 5

answer_five = float(input("Question 5: what is (5)^2*3+24"))
if answer_five == 99:
    print("you are correct")
    answer_correct += 1
else:
    print("you are wrong")


if answer_correct != 1:
    print(f"You have {answer_correct} answer correct in total, congratulation!")