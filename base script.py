import pandas as pd

def getData(inputFile):
    dataframe = pd.read_stata(inputFile)
    return dataframe


def main():
    data = getData('dataset.dta')
    print(type(data))



if __name__ == '__main__':
    main()