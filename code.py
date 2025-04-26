import pandas as pd
import json

# Load Disease and Symptoms CSV
disease_symptoms_df = pd.read_csv('D:\\Python\\chatbot\\DiseaseAndSymptoms.csv')

# Print existing columns for troubleshooting
print("Columns in DiseaseAndSymptoms.csv:", disease_symptoms_df.columns)

# Load Precautions CSV
precautions_df = pd.read_csv('D:\\Python\\chatbot\\Disease precaution.csv')

# Print existing columns for troubleshooting
print("Columns in Disease precaution.csv:", precautions_df.columns)

# Merge DataFrames on 'Disease' column
merged_df = pd.merge(disease_symptoms_df, precautions_df, on='Disease')

# Prepare the final JSON structure
intents = {"intents": []}

# Iterate through each row and prepare the intent object
for index, row in merged_df.iterrows():
    disease = row['Disease']
    
    # Collect symptoms from 'symptom 1' to 'symptom 17' columns
    symptoms = [row[f'Symptom_{i}'] for i in range(1, 18) if pd.notna(row[f'Symptom_{i}'])]

    # Collect precautions from 'Precaution_1' to 'Precaution_3'
    precautions = [row.get(f'Precaution_{i}', None) for i in range(1, 4) if pd.notna(row.get(f'Precaution_{i}', None))]

    # Add the intent object to the intents list
    intents['intents'].append({
        "tag": disease,
        "patterns": symptoms,
        "responses": precautions
    })

# Save the intents to a JSON file
with open('intents.json', 'w') as json_file:
    json.dump(intents, json_file, indent=4)

print("intents.json file created successfully!")
