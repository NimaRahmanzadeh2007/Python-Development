user_input_count = int(input("Enter the number of scores: "))

scores = []

for i in range(1, user_input_count+1):
    while True:
        user_score = float(input(f"Enter the score number {i}: "))
        if 0 < user_score <= 20:
            scores.append(user_score)
            break
        else:
            print("Invalid input! please enter a number between 1 and 20...")


sum_of_all = 0

for i in scores:
    sum_of_all += i

average = sum_of_all / len(scores)


print(f"The average is {average:.2f}.")
