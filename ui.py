import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from detection import start_detection, stop_detection
from database import load_records

driver_name = ""

def set_driver_name():
    global driver_name
    driver_name = simpledialog.askstring("Driver Info", "Enter Driver's name:")
    if driver_name:
        messagebox.showinfo('Success', f"Driver Name Set: {driver_name}")

def start_detection_ui():
    if not driver_name:
        messagebox.showwarning("Warning", "Enter driver name first")
        return
    start_detection(driver_name)

def stop_detection_ui():
    stop_detection()
    messagebox.showinfo("Info", "Stopping Application...")

def view_records():
    df = load_records()
    record_window = tk.Toplevel()
    record_window.title("Previous Driver Records")
    record_window.geometry("500x300")

    tree = ttk.Treeview(record_window, columns=("Name", "Date_time", "Status", "Accuracy"), show="headings")
    tree.heading("Name", text="Driver Name")
    tree.heading("Date_time", text="Date & Time")
    tree.heading("Status", text="Status")
    tree.heading("Accuracy", text="Accuracy (%)")

    for _, row in df.iterrows():
        tree.insert("", tk.END, values=(row['Name'], row["Date_time"], row["Status"], row["Accuracy"]))

    tree.pack(expand=True, fill="both")

def create_ui():
    root = tk.Tk()
    root.title("Driver Behavior Analysis")
    root.geometry("300x300")

    tk.Button(root, text="Enter Driver Name", command=set_driver_name, bg="blue", fg="white", font=("Arial", 12)).pack(pady=5)
    tk.Button(root, text="Start Detection", command=start_detection_ui, bg="green", fg="white", font=("Arial", 12)).pack(pady=5)
    tk.Button(root, text="Stop Application", command=stop_detection_ui, bg="red", fg="white", font=("Arial", 12)).pack(pady=5)
    tk.Button(root, text="View Past Records", command=view_records, bg="purple", fg="white", font=("Arial", 12)).pack(pady=5)

    root.mainloop()