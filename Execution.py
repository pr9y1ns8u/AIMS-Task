import pandas as pd
from OneHotEncoder import OH_Encode
from OrdinalEncoder import Ord_Encode

# Original Data Frame
path = "data.csv"
df = pd.read_csv(path)
print(f"Original Data:\n\n{df}\n")

# One Hot Encoded Data Frame
print(f"One Hot Encoded Data:\n")
OH_Encode(df)

# Ordinally Encoded Data Frame
print(f"\nOrdinally Encoded Data:\n")
Ord_Encode(df)