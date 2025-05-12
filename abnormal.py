import pandas as pd

# Load dataset
data = pd.read_csv("Dataset/archive/mitbih_test.csv", header=None)

# Filter for abnormal data (labels != 0)
abnormal_data = data[data[187] != 0]

# Randomly select one abnormal patient
one_abnormal_patient = abnormal_data.sample(n=1)

# Save the selected data to a new CSV file
one_abnormal_patient.to_csv("abnormal_patient_ecg.csv", index=False, header=False)

print("Saved one random abnormal patient ECG data to 'abnormal_patient_ecg.csv'")
