# average_program.py

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def main():
    numbers = input("Enter numbers separated by spaces: ").split()
    numbers = [float(num) for num in numbers]
    
    if len(numbers) == 0:
        print("No numbers were entered.")
    else:
        average = calculate_average(numbers)
        print(f"The average of the entered numbers is: {average}")

if __name__ == "__main__":
    main()
