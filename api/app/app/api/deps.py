import csv

EV_LOG_HEADER = [
    "CDR_ID",
    "CS_ID",
    "Socketoutlet_ID",
    "Transaction_ID",
    "UID",
    "Type of charge",
    "Start_Datetime",
    "End_Datetime",
    "Energy_kWh",
    "Socket_Type",
    "Duration",
    "Comment"
]

def generate_day_summary(file_path):
    """Generates the day's summary of EV charging"""
    total_val = {
        "Energy_kWh": 0
    }
    passed_header = False
    with open(file_path, newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            if passed_header:
                idx = EV_LOG_HEADER.index("Energy_kWh")
                total_val["Energy_kWh"] += row[idx]
            passed_header = True
            