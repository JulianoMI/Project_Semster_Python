import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style

def submit_survey():

    thank_you_window = tk.Toplevel(root)
    thank_you_window.title("Thank You")
    thank_you_label = ttk.Label(thank_you_window, text="Thank you for filling this survey!", font=("Helvetica", 16))
    thank_you_label.pack(pady=20, padx=20)
    
    def on_thank_you_close():
        root.destroy()
    
    thank_you_window.protocol("WM_DELETE_WINDOW", on_thank_you_close)

root = tk.Tk()
root.title("Restaurant Survey")
style = Style(theme='journal')  


title_label = ttk.Label(root, text="Restaurant Survey", font=("Arial", 20))
title_label.pack(pady=10)

# Question 1
q1_label = ttk.Label(root, text="1. How was our service?")
q1_label.pack(anchor='w', padx=20)
q1_var = tk.IntVar()
for i in range(1, 6):
    ttk.Radiobutton(root, text=str(i), variable=q1_var, value=i).pack(anchor='w', padx=40)

# Question 2
q3_label = ttk.Label(root, text="2. Were you satisfied with our staff?")
q3_label.pack(anchor='w', padx=20)
q3_var = tk.IntVar()
for i in range(1, 6):
    ttk.Radiobutton(root, text=str(i), variable=q3_var, value=i).pack(anchor='w', padx=40)

# Question 3
q4_label = ttk.Label(root, text="3. How would you rate the cleanliness of our restaurant?")
q4_label.pack(anchor='w', padx=20)
q4_var = tk.IntVar()
for i in range(1, 6):
    ttk.Radiobutton(root, text=str(i), variable=q4_var, value=i).pack(anchor='w', padx=40)

# Question 4 
q2_label = ttk.Label(root, text="4. How did you find out about us?")
q2_label.pack(anchor='w', padx=20)
q2_var = tk.StringVar()
social_media_options = ["Facebook", "Instagram", "Twitter", "Google", "Friend", "Other"]
q2_combobox = ttk.Combobox(root, textvariable=q2_var, values=social_media_options)
q2_combobox.pack(anchor='w', padx=40)

# Question 5
q5_label = ttk.Label(root, text="5. Write any more improvements that we can implement:")
q5_label.pack(anchor='w', padx=20)
q5_text = tk.Text(root, height=4, width=50)
q5_text.pack(anchor='w', padx=40)

submit_button = ttk.Button(root, text="Submit", command=submit_survey)
submit_button.pack(pady=20)

root.mainloop()
