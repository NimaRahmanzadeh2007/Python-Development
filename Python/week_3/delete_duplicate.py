user_input_count = int(input("Enter the number inputs: "))


sample_list = []

new_list = []

for i in range(1, user_input_count+1):
    user_input = int(input(f"Enter the input number {i}: "))
    sample_list.append(user_input)


for i in sample_list:
    if i not in new_list:
        new_list.append(i)

print(f"original list is: {sample_list}")
print(f"edited list is: {new_list}")
