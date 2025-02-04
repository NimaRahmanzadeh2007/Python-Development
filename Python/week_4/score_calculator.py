input_count = int(input("Enter the number of scores: "))

sample_list = []

for i in range(1, input_count + 1):
    while True:
        try:
            user_score = float(input(f"Enter the score number {i}: "))
            if user_score >= 0 and user_score <= 20:
                sample_list.append(user_score)
                break
            else:
                print("score should be between 0 to 20...")
        except:
            print("something went wrong, try again...")

gpa = 0

for x in sample_list:
    gpa += x

gpa = gpa / len(sample_list)

print(f"The average of the scores is: {gpa}")
