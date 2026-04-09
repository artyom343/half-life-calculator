while True:
    try:
        unit = input("Is the half-life in years or minutes? (years/months/minutes): ").lower()
        half_life = float(input("Enter the half-life: "))
        
        if unit == "minutes":
            half_life = half_life / 525600  # convert minutes to years
            
        if unit == "months":
            half_life = half_life / 12  # convert months to years

        time_passed = float(input("Enter time passed (the unit doesn't matter): "))
            time_passed = time_passed / 525600  # convert minutes to years
        initial_mass = float(input("Enter initial mass (g): "))

        remaining_mass = initial_mass * (0.5 ** (time_passed / half_life))

        print(f"\nStarting mass: {initial_mass:.6g} g")
        print(f"Remaining mass: {remaining_mass:.6g} g\n")

    except ValueError:
        print("Enter valid numbers.\n")
