while True:
    try:
        half_life = float(input("Enter the half-life (years): "))
        time_passed = float(input("Enter time passed (years): "))
        initial_mass = float(input("Enter initial mass (g): "))

        remaining_mass = initial_mass * (0.5 ** (time_passed / half_life))

        print(f"\nStarting mass: {initial_mass:.2f} g")
        print(f"Remaining mass: {remaining_mass:.2f} g\n")

    except ValueError:
        print("Enter valid numbers.\n")