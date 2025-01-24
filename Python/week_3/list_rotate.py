user_input_count = int(input("Enter the number of inputs: "))

sample_list = []

for i in range(1, user_input_count+1):
    user_input = int(input(f"Enter the input number {i}: "))
    sample_list.append(user_input)

user_rotate = int(input("Enter the numer of rotates: "))

new_list = sample_list[-user_rotate:] + sample_list[:-user_rotate]

print(f"original list is: {sample_list}")
print(f"edited list is: {new_list}")
