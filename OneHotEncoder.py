import pandas as pd

path = "data.csv"
df = pd.read_csv(path)

def OH_Encode(df:pd.DataFrame):  
    
    Df = df.copy() # copy of the dataframe so the the original one isn't changed

    def column_encode(column):
        
        unique_values = Df[column].unique() # Makes columns for each unique value in a categorical column
        for value in unique_values:
            Df[value] = Df[column].apply(lambda x: 1 if x==value else 0)

    categorical_cols=[col for col in Df.columns if Df[col].dtype == "object"]

    for col in categorical_cols:
        column_encode(col)

    print(Df)

if __name__ == "__main__":
    print(df)
    print("\nOne Hot Encoded Data: \n")
    OH_Encode(df)