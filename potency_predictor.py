import tkinter as tk
from tkinter import filedialog
import pandas as pd
from rdkit import Chem
from rdkit.Chem import Descriptors
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import sys

# Function to load data from selected CSV file
def load_data():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename(title="Select ChEMBL CSV File", filetypes=[("CSV Files", "*.csv")])
    if not file_path:
        print("No file selected. Exiting.")
        sys.exit()
    try:
        df = pd.read_csv(file_path, delimiter=';')
        return df
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        return None

# Function to preprocess SMILES and convert to RDKit Mol objects
def process_smiles(smiles):
    try:
        mol = Chem.MolFromSmiles(smiles)
        return mol
    except:
        return None

# Function to calculate molecular descriptors
def calculate_descriptors(mol):
    if mol is not None:
        return {
            'MolecularWeight': Descriptors.MolWt(mol),
            'AlogP': Descriptors.MolLogP(mol)
        }
    else:
        return None

# Function to predict potency for new compounds
def predict_potency(model, features):
    try:
        predicted_potency = model.predict(features)
        return predicted_potency[0]
    except Exception as e:
        print(f"Prediction error: {e}")
        return None

# Main function
def main():
    # Load data
    df = load_data()
    if df is None:
        return
    
    # Preprocess SMILES and convert to RDKit Mol objects
    df['Smiles'] = df['Smiles'].fillna('').astype(str)
    df['Molecule'] = df['Smiles'].apply(process_smiles)

    # Calculate molecular descriptors
    df['Descriptors'] = df['Molecule'].apply(calculate_descriptors)

    # Drop rows where molecular descriptors could not be computed
    df = df.dropna(subset=['Descriptors'])

    # Split data into X (features) and y (target)
    X = df['Descriptors'].apply(pd.Series)  # Expand dictionary into separate columns
    y = df['Standard Value']

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train a model (e.g., Random Forest Regressor)
    model = RandomForestRegressor(random_state=42)
    model.fit(X_train, y_train)

    # Predict on test set
    y_pred = model.predict(X_test)

    # Evaluate model
    rmse = mean_squared_error(y_test, y_pred, squared=False)
    r2 = r2_score(y_test, y_pred)
    print(f"RMSE: {rmse}, R-squared: {r2}")

    # Example: Predicting for a new compound based on user input features
    try:
        mw = float(input("Enter Molecular Weight of the new compound: "))
        alogp = float(input("Enter AlogP of the new compound: "))
        new_compound_features = pd.DataFrame([[mw, alogp]], columns=['MolecularWeight', 'AlogP'])
        predicted_potency = predict_potency(model, new_compound_features)
        if predicted_potency is not None:
            print(f"Predicted Potency: {predicted_potency}")
    except ValueError:
        print("Invalid input for features. Please enter numerical values.")

# Entry point of the program
if __name__ == "__main__":
    main()
