# PotencyPredictor

## Overview
This Python application predicts the potency of chemical compounds using molecular descriptors calculated from SMILES notation. It leverages the RDKit library for chemical informatics operations and uses a Random Forest Regressor model from the scikit-learn library for making predictions based on molecular properties.

## Features
- **Data Loading:** Import chemical compound data from a CSV file using a file dialog.
- **Molecular Descriptor Calculation:** Converts SMILES to molecular descriptors such as Molecular Weight and AlogP using RDKit.
- **Model Training and Prediction:** Utilizes a Random Forest Regressor to predict compound potency and evaluate the model performance with RMSE and R-squared metrics.
- **User Interaction:** Allows the user to input new compound data for potency prediction.

## Prerequisites
Before you can run this script, make sure you have the following installed:
- Python 3.6 or higher
- RDKit: Used for chemical computations.
- pandas: For handling data.
- scikit-learn: For modeling and predictions.

### Installation Guide
1. Install Python from [Python.org](https://www.python.org).
2. Install required Python libraries:
   ```bash
   pip install pandas scikit-learn rdkit-pypi
   ```

## Usage
1. Run the script:
   ```bash
   python potency_predictor.py
   ```
2. Select a CSV file with chemical compounds data when prompted. Ensure your CSV file is formatted with at least the following columns:
   - `Smiles`: Column containing SMILES notation of compounds.
   - `Standard Value`: Column containing potency values of compounds.
3. The script processes the data, trains the model, and evaluates it. You will then be prompted to enter the Molecular Weight and AlogP for a new compound to predict its potency.

## Data Format
The input CSV file should be formatted with semicolon (;) separators and include at least the following columns:
- `Smiles`: SMILES notation of the compounds.
- `Standard Value`: Known potency values (numeric).

### Example CSV Format
```
Smiles;Standard Value
CCO;123.45
NCCO;234.56
```

## Contributing
Contributions to enhance the functionality or efficiency of this application are welcome. Please feel free to fork the repository and submit a pull request.

## License
Specify your license or leave this section empty if you're still deciding.

## Contact Information
- **Email:** [mhurwanth@gmail.com](mailto:mhurwanth@gmail.com)
- **LinkedIn:** [linkedin.com/in/mihirhurwanth](https://www.linkedin.com/in/mihirhurwanth/)

```
