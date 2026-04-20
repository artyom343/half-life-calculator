import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        unit = unit_var.get().lower()
        if unit not in ["years", "months", "minutes"]:
            messagebox.showerror("Error", "Choose years, months, or minutes.")
            return

        half_life = float(entry_half_life.get())
        time_passed = float(entry_time.get())
        initial_mass = float(entry_mass.get())

        # Convert to years
        if unit == "minutes":
            half_life /= 525600
            time_passed /= 525600
        elif unit == "months":
            half_life /= 12
            time_passed /= 12

        remaining_mass = initial_mass * (0.5 ** (time_passed / half_life))

        result_label.config(
            text=f"Starting mass: {initial_mass:.6g} g\n"
                 f"Remaining mass: {remaining_mass:.6g} g"
        )

    except ValueError:
        messagebox.showerror("Error", "Enter valid numbers.")

# Create window
root = tk.Tk()
root.title("Half-Life Calculator")
root.geometry("350x300")

# Unit selection
tk.Label(root, text="Unit (years/months/minutes):").pack()
unit_var = tk.StringVar()
tk.Entry(root, textvariable=unit_var).pack()

# Half-life input
tk.Label(root, text="Half-life:").pack()
entry_half_life = tk.Entry(root)
entry_half_life.pack()

# Time passed input
tk.Label(root, text="Time passed:").pack()
entry_time = tk.Entry(root)
entry_time.pack()

# Initial mass input
tk.Label(root, text="Initial mass (g):").pack()
entry_mass = tk.Entry(root)
entry_mass.pack()

# Calculate button
tk.Button(root, text="Calculate", command=calculate).pack(pady=10)

# Result label
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()