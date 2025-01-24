user_input_count = int(input("Enter the number of inputs: "))

sample_list = []

for i in range(1, user_input_count+1):
    user_input = int(input(f"Enter the input number {i}: "))
    sample_list.append(user_input)


even_numbers = [i for i in sample_list if i % 2 == 0]

print(f"original list is: {sample_list}")
print(f"edited list is: {even_numbers}")
