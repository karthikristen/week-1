import tkinter as tk
from tkinter import messagebox
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt

# ----------------------------
# 1. Synthetic Dataset Creation
# ----------------------------
np.random.seed(42)
n_samples = 500

data = {
    "pH": np.random.uniform(5.5, 9.5, n_samples),
    "Hardness": np.random.uniform(100, 400, n_samples),
    "Nitrate": np.random.uniform(0, 100, n_samples),
    "Conductivity": np.random.uniform(200, 2000, n_samples),
    "TDS": np.random.uniform(100, 1000, n_samples)
}
df = pd.DataFrame(data)

def label_sample(row):
    if (6.5 <= row["pH"] <= 8.5) and row["Hardness"] < 300 and row["Nitrate"] < 50:
        return "Safe"
    elif (5.8 <= row["pH"] <= 9.0) and row["Hardness"] < 350 and row["Nitrate"] < 70:
        return "Moderate"
    else:
        return "Unsafe"

df["Label"] = df.apply(label_sample, axis=1)

# Train model
X = df[["pH", "Hardness", "Nitrate", "Conductivity", "TDS"]]
y = df["Label"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# ----------------------------
# 2. GUI Application
# ----------------------------
root = tk.Tk()
root.title("💧 Water Quality Checker")
root.geometry("450x600")
root.configure(bg="#e6f7ff")

# Title
title_label = tk.Label(root, text="💧 Water Quality Checker", font=("Arial", 18, "bold"),
                       bg="#e6f7ff", fg="#0077b6")
title_label.pack(pady=15)

# Input fields
labels = ["pH", "Hardness (mg/L)", "Nitrate (mg/L)", "Conductivity (µS/cm)", "TDS (mg/L)"]
entries = {}

for lbl in labels:
    tk.Label(root, text=lbl, font=("Arial", 12), bg="#e6f7ff").pack(pady=5)
    entry = tk.Entry(root, font=("Arial", 12), justify="center")
    entry.pack(pady=5)
    entries[lbl] = entry

# Prediction function
def check_water():
    try:
        values = [float(entries[lbl].get()) for lbl in labels]
        sample = np.array([values])
        prediction = model.predict(sample)[0]

        # Show popup result
        messagebox.showinfo("Result", f"✅ The water is **{prediction}** for drinking.")

        # Show bar chart
        plt.figure(figsize=(6,4))
        plt.bar(labels, values, color=['#0077b6','#00b4d8','#90e0ef','#48cae4','#0096c7'])
        plt.title("Water Sample Parameters", fontsize=14)
        plt.ylabel("Value", fontsize=12)
        plt.xticks(rotation=20)
        plt.tight_layout()
        plt.show()

    except ValueError:
        messagebox.showerror("Error", "⚠️ Please enter valid numbers.")

# Button
tk.Button(root, text="Check Water Quality", font=("Arial", 14, "bold"), bg="#0077b6", fg="white",
          command=check_water, relief="raised", bd=3).pack(pady=20)

# Footer
tk.Label(root, text="Made with ❤️ by Karthikeyan", font=("Arial", 10), bg="#e6f7ff", fg="gray").pack(side="bottom", pady=10)

root.mainloop()
