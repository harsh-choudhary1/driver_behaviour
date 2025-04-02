import pandas as pd
import datetime

record_file = "driver_record.csv"

def init_database():
    try:
        df = pd.read_csv(record_file)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Name", "Date_time", "Status", "Accuracy"])
        df.to_csv(record_file, index=False)

def save_driver_record(name, status, accuracy=None):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    accuracy = accuracy if accuracy else "N/A"
    data = {"Name": [name], "Date_time": [timestamp], "Status": [status], "Accuracy": [accuracy]}

    try:
        df = pd.DataFrame(data)
        df.to_csv(record_file, mode='a', index=False, header=False)
    except Exception as e:
        print(f"Error saving record: {e}")

def load_records():
    try:
        return pd.read_csv(record_file)
    except FileNotFoundError:
        return pd.DataFrame(columns=["Name", "Date_time", "Status", "Accuracy"])
