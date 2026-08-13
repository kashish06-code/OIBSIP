import tkinter as tk
from tkinter import messagebox


# ---------------- BMI Category Function ---------------- #
def calculate_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight 😕", "orange"
    elif bmi < 25:
        return "Healthy ✅", "green"
    elif bmi < 30:
        return "Overweight ⚠️", "dark orange"
    else:
        return "Obese 🩺", "red"


# ---------------- Calculate BMI ---------------- #
def calculate():
    try:
        weight = float(weight_entry.get())
        height_cm = float(height_entry.get())

        if weight <= 0 or height_cm <= 0:
            raise ValueError("Weight and Height must be greater than 0.")

        height_m = height_cm / 100
        bmi = weight / (height_m ** 2)

        category, color = calculate_bmi_category(bmi)

        result_label.config(
            text=f"BMI: {bmi:.2f}\nCategory: {category}",
            fg=color
        )

    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))


# ---------------- Reset Fields ---------------- #
def reset():
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)

    result_label.config(
        text="Enter your details and click Calculate",
        fg="black"
    )


# ---------------- Main Window ---------------- #
window = tk.Tk()
window.title("BMI Calculator - Python (tkinter)")
window.geometry("420x500")
window.resizable(False, False)
window.configure(bg="#E8F4F8")

# ---------------- Heading ---------------- #
title = tk.Label(
    window,
    text="BMI Calculator",
    font=("Arial", 20, "bold"),
    bg="#E8F4F8",
    fg="#003366"
)
title.pack(pady=15)

# ---------------- Weight ---------------- #
weight_label = tk.Label(
    window,
    text="Weight (kg)",
    font=("Arial", 12),
    bg="#E8F4F8"
)
weight_label.pack()

weight_entry = tk.Entry(
    window,
    font=("Arial", 12),
    width=20,
    justify="center"
)
weight_entry.pack(pady=5)

# ---------------- Height ---------------- #
height_label = tk.Label(
    window,
    text="Height (cm)",
    font=("Arial", 12),
    bg="#E8F4F8"
)
height_label.pack()

height_entry = tk.Entry(
    window,
    font=("Arial", 12),
    width=20,
    justify="center"
)
height_entry.pack(pady=5)

# ---------------- Buttons ---------------- #
button_frame = tk.Frame(window, bg="#E8F4F8")
button_frame.pack(pady=15)

calculate_button = tk.Button(
    button_frame,
    text="Calculate BMI",
    command=calculate,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 11, "bold"),
    width=15
)
calculate_button.grid(row=0, column=0, padx=5)

reset_button = tk.Button(
    button_frame,
    text="Reset",
    command=reset,
    bg="#FF9800",
    fg="white",
    font=("Arial", 11, "bold"),
    width=10
)
reset_button.grid(row=0, column=1, padx=5)

# ---------------- Result ---------------- #
result_label = tk.Label(
    window,
    text="Enter your details and click Calculate",
    font=("Arial", 14, "bold"),
    bg="#E8F4F8",
    justify="center"
)
result_label.pack(pady=20)

# ---------------- BMI Classification ---------------- #
frame = tk.LabelFrame(
    window,
    text="BMI Classification",
    font=("Arial", 11, "bold"),
    padx=10,
    pady=10,
    bg="white"
)
frame.pack(padx=15, fill="both")

classification = [
    ("Below 18.5", "Underweight"),
    ("18.5 - 24.9", "Healthy"),
    ("25.0 - 29.9", "Overweight"),
    ("30.0 and above", "Obese")
]

for bmi_range, status in classification:
    row = tk.Frame(frame, bg="white")
    row.pack(fill="x", pady=2)

    tk.Label(
        row,
        text=bmi_range,
        width=15,
        anchor="w",
        bg="white",
        font=("Arial", 10)
    ).pack(side="left")

    tk.Label(
        row,
        text=status,
        anchor="w",
        bg="white",
        font=("Arial", 10)
    ).pack(side="left")

# ---------------- Exit Button ---------------- #
exit_button = tk.Button(
    window,
    text="Exit",
    command=window.destroy,
    bg="#F44336",
    fg="white",
    font=("Arial", 11, "bold"),
    width=10
)
exit_button.pack(pady=15)

# ---------------- Run Application ---------------- #
window.bind("<Return>", lambda event: calculate())
window.mainloop()