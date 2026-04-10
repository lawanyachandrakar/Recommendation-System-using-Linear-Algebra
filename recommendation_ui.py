import numpy as np
import tkinter as tk

def calculate():
    try:
        R = []
        for i in range(3):
            row = []
            for j in range(3):
                val = float(entries[i][j].get())
                row.append(val)
            R.append(row)

        R = np.array(R)

        U = np.array([
            [1.0, 0.8],
            [0.9, 0.6],
            [0.7, 1.0]
        ])

        V = np.array([
            [5, 3],
            [2, 4],
            [3, 5]
        ])

        R_pred = np.dot(U, V.T)

        result_text = "Predicted Ratings:\n"
        result_text += str(np.round(R_pred, 2)) + "\n\n"

        result_text += "Recommendations:\n"
        for i in range(3):
            for j in range(3):
                if R[i][j] == 0:
                    result_text += f"User {i+1} → Product {j+1}\n"

        result_label.config(text=result_text)

    except:
        result_label.config(text="Invalid input")

root = tk.Tk()
root.title("Recommendation System")

entries = []

for i in range(3):
    row = []
    for j in range(3):
        e = tk.Entry(root, width=5)
        e.grid(row=i, column=j)
        row.append(e)
    entries.append(row)

btn = tk.Button(root, text="Calculate", command=calculate)
btn.grid(row=4, column=1)

result_label = tk.Label(root, text="")
result_label.grid(row=5, column=0, columnspan=3)

root.mainloop()
