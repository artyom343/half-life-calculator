while True:
    try:
        unit = input("Is the half-life in years, months, or minutes? ").lower()

        if unit not in ["years", "months", "minutes"]:
            print("Invalid unit. enter 'years', 'months', or 'minutes'.\n")
            continue

        
        half_life = float(input("Enter the half-life: "))
        time_passed = float(input("Enter time passed (same unit as half-life): "))
        initial_mass = float(input("Enter initial mass (g): "))

        # Converting half-life and time to years
        if unit == "minutes":
            half_life /= 525600      # minutes → years
            time_passed /= 525600
        elif unit == "months":
            half_life /= 12          # months → years
            time_passed /= 12

        #the half life formula
        remaining_mass = initial_mass * (0.5 ** (time_passed / half_life))

        print(f"\nStarting mass: {initial_mass:.6g} g")
        print(f"Remaining mass: {remaining_mass:.6g} g\n")

    except ValueError:
        print("Enter valid numbers.\n")
