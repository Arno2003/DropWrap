import pandas as pd
def convert(sourceFile, destinationFile):
    data = pd.read_csv(sourceFile)
    cast = data["Social Category"]
    dest = pd.read_csv(destinationFile)
    newCols = []
    for i in cast:
        if i not in newCols:
            newCols.append(i)

        else:
            break


if __name__ == "__main__":
    sourceFile = "Gujarat.csv"
    destinationFile = "castClustGuj.csv"
    convert(sourceFile, destinationFile)