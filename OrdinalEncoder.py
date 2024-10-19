import pandas as pd

path = "data.csv"
df = pd.read_csv(path)

def Ord_Encode(df:pd.DataFrame):
    
    Df = df.copy() # copy of the dataframe so the the original one isn't changed
    
    def column_encode(column):

        Map = dict(zip(Df[column].unique(), range(len(Df[column].unique())))) # Here the first unique value is given zero, second one given one, third one given two, etc.
        Df[column] = Df[column].apply(lambda x: Map[x])

    categorical_cols = [col for col in Df.columns if Df[col].dtype == "object"]

    for col in categorical_cols:
        column_encode(col)

    print(Df)

if __name__ == "__main__":
    print(df)
    print("\nOne Hot Encoded Data: \n")
    Ord_Encode(df)