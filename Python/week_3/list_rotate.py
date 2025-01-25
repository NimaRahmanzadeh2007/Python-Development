# user_input_count = int(input("Enter the number of inputs: "))

# sample_list = []

# for i in range(1, user_input_count+1):
#     user_input = int(input(f"Enter the input number {i}: "))
#     sample_list.append(user_input)

# user_rotate = int(input("Enter the numer of rotates: "))

# new_list = sample_list[-user_rotate:] + sample_list[:-user_rotate]

# print(f"original list is: {sample_list}")
# print(f"edited list is: {new_list}")

# --------------------------------------------------------------  Updated

user_count = int(input("Enter the number of elements: "))


sample_list = []

for i in range(1, user_count + 1):
    while True:
        try:
            user_input = int(input(f"Enter the value of element number {i}: "))
            sample_list.append(user_input)
            break
        except:
            print("enter inteager...")
            print("try again...")


rotates = int(input("Enter the number of rotates: "))

new_list = sample_list[-rotates:] + sample_list[:-rotates]

print(new_list)
