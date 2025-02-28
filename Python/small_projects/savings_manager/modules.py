def calculate_budget():
    try:
        monthly_income = int(input("Enter your cash for every month: "))
        recommended_spending = monthly_income * 0.7
        monthly_expenses = int(input("Enter your cash use for every month: "))

        if monthly_expenses > recommended_spending:
            print("\nWarning! You are using too much!")
        else:
            print("Good! You are using correctly!")

    except ValueError:
        print("Invalid input! Please enter a valid number.")

    except Exception as e:
        print(f"Something went wrong: {e}")
