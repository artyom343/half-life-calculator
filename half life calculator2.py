import tkinter as tk
from tkinter import messagebox

# Radioactive isotope database (half-life in YEARS)
isotopes = {
    # 43
    "Technetium-99m (43)": 6.01 / 8760,  # 6.01 hours → years
    "Technetium-98 (43)": 4.2e6,

    # 83–92
    "Bismuth-209 (83)": 1.9e19,
    "Polonium-210 (84)": 138 / 365,
    "Astatine-210 (85)": 8.1 / 24 / 365,
    "Radon-222 (86)": 3.8 / 365,
    "Francium-223 (87)": 22 / 60 / 24 / 365,
    "Radium-226 (88)": 1600,
    "Actinium-227 (89)": 21.8,
    "Thorium-232 (90)": 1.4e10,
    "Protactinium-231 (91)": 32760,
    "Uranium-238 (92)": 4.47e9,

    # Actinides 93–103
    "Neptunium-237 (93)": 2.14e6,
    "Plutonium-239 (94)": 24100,
    "Americium-241 (95)": 432,
    "Curium-247 (96)": 1.56e7,
    "Berkelium-247 (97)": 1380,
    "Californium-251 (98)": 898,
    "Einsteinium-252 (99)": 1.29,
    "Fermium-257 (100)": 100 / 365,
    "Mendelevium-258 (101)": 51.5 / 365,
    "Nobelium-259 (102)": 58 / 60 / 24 / 365,
    "Lawrencium-262 (103)": 3.6 / 60 / 24 / 365,

    # 104–118 (representative longest-lived isotopes)
    "Rutherfordium-267 (104)": 1.3 / 365,
    "Dubnium-268 (105)": 1.0 / 365,
    "Seaborgium-269 (106)": 0.24 / 365,
    "Bohrium-270 (107)": 0.15 / 365,
    "Hassium-277 (108)": 0.03 / 365,
    "Meitnerium-278 (109)": 0.002 / 365,
    "Darmstadtium-281 (110)": 0.0004 / 365,
    "Roentgenium-282 (111)": 0.0002 / 365,
    "Copernicium-285 (112)": 0.0001 / 365,
    "Nihonium-286 (113)": 0.00005 / 365,
    "Flerovium-289 (114)": 0.00003 / 365,
    "Moscovium-290 (115)": 0.00002 / 365,
    "Livermorium-293 (116)": 0.00001 / 365,
    "Tennessine-294 (117)": 0.000005 / 365,
    "Oganesson-294 (118)": 0.000003 / 365,
}

def calculate():
    try:
        isotope_name = isotope_var.get()
        half_life = isotopes[isotope_name]

        time_passed = float(entry_time.get())
        initial_mass = float(entry_mass.get())

        if time_passed < 0:
            messagebox.showerror("Error", "Time cannot be negative.")
            return
        if initial_mass <= 0:
            messagebox.showerror("Error", "Mass must be greater than 0.")
            return

        unit = unit_var.get()

        # Convert time to years
        if unit == "Minutes":
            time_passed /= 525600
        elif unit == "Months":
            time_passed /= 12

        num_half_lives = time_passed / half_life
        remaining_mass = initial_mass * (0.5 ** num_half_lives)
        percent_remaining = (remaining_mass / initial_mass) * 100

        result_label.config(
            text=(
                f"Isotope: {isotope_name}\n"
                f"Remaining mass: {remaining_mass:.6g} g\n"
                f"Half-lives passed: {num_half_lives:.2f}\n"
                f"Remaining: {percent_remaining:.2f}%"
            ),
            fg="blue"
        )

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

def clear_fields():
    entry_time.delete(0, tk.END)
    entry_mass.delete(0, tk.END)
    result_label.config(text="", fg="black")

# Window
root = tk.Tk()
root.title("Radioactive Isotope Decay Calculator")
root.geometry("420x520")

main_frame = tk.Frame(root, padx=25, pady=20)
main_frame.pack()

tk.Label(main_frame, text="☢", font=("Arial", 48), fg="gray").pack(pady=5)

tk.Label(main_frame, text="Radioactive Decay Calculator",
         font=("Arial", 16, "bold")).pack(pady=5)

# Isotope selection
tk.Label(main_frame, text="Select Isotope:").pack()
isotope_var = tk.StringVar(value=list(isotopes.keys())[0])
tk.OptionMenu(main_frame, isotope_var, *isotopes.keys()).pack(pady=5)

# Unit selection
tk.Label(main_frame, text="Select Time Unit:").pack()
unit_var = tk.StringVar(value="Years")
tk.OptionMenu(main_frame, unit_var, "Years", "Months", "Minutes").pack(pady=5)

# Time input
tk.Label(main_frame, text="Time Passed:").pack()
entry_time = tk.Entry(main_frame)
entry_time.pack(pady=5)

# Mass input
tk.Label(main_frame, text="Initial Mass (g):").pack()
entry_mass = tk.Entry(main_frame)
entry_mass.pack(pady=5)

# Buttons
button_frame = tk.Frame(main_frame)
button_frame.pack(pady=15)

tk.Button(button_frame, text="Calculate", width=12, command=calculate).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Clear", width=12, command=clear_fields).grid(row=0, column=1, padx=5)

result_label = tk.Label(main_frame, text="", justify="left", wraplength=360)
result_label.pack(pady=10)

root.bind("<Return>", lambda event: calculate())

root.mainloop()
