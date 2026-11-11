# ==========================================
# RESISTOR COMBINATION CALCULATOR
# CTE213 PYTHON MINI PROJECT
# ==========================================

# Function to calculate resistance in series
def calculate_series(resistors):
    total = 0

    for resistance in resistors:
        total += resistance

    return total


# Function to calculate resistance in parallel
def calculate_parallel(resistors):
    total = 0

    for resistance in resistors:
        total += 1 / resistance

    return 1 / total


# Main program
def main():

    print("================================")
    print("  RESISTOR COMBINATION CALCULATOR")
    print("================================")

    while True:

        try:
            number = int(input("\nEnter number of resistors: "))

            if number <= 0:
                print("Error: Enter a number greater than zero.")
                continue

            resistors = []

            for i in range(number):

                while True:
                    try:
                        resistance = float(
                            input(f"Enter resistor {i + 1} value (Ohms): ")
                        )

                        if resistance <= 0:
                            print("Resistance must be greater than zero.")
                        else:
                            resistors.append(resistance)
                            break

                    except ValueError:
                        print("Invalid input! Enter a numerical value.")

            # Calculate total resistance
            series = calculate_series(resistors)
            parallel = calculate_parallel(resistors)

            # Display results
            print("\n========== RESULTS ==========")

            print(f"Series Resistance: {series:.2f} Ohms")
            print(f"Parallel Resistance: {parallel:.2f} Ohms")

            print("=============================")

            # Additional feature
            if series > parallel:
                print("Series resistance is greater than parallel resistance.")

            print("\nCalculation completed successfully!")

            again = input("\nCalculate again? (yes/no): ").lower()

            if again != "yes":
                print("\nThank you for using the calculator!")
                break

        except ValueError:
            print("Invalid input! Please enter a whole number.")


# Run the program
if __name__ == "__main__":
    main()