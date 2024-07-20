import pandas as pd
from pprint import pprint
import os


def addDNO(df):
    dno = pd.read_csv("DATA\\Test\\Abbreviations\\SerialNoListDistricts.csv")
    dis = []
    dno.columns.values[-1:] = 'District'
    for district in dno['District']:
        dis.append(district.replace(" ", ""))

    dno['District'] = dis

    df_merged = pd.merge(df, dno, on='District', how='right')
    return df_merged


#######################################################################################
######################### PRE-PROCESSING INCOME DATA ##################################
#######################################################################################


def ppSingleIncome(df):
    df = df.drop(df.index[0:3]).reset_index(drop=True)
    df = pd.concat([df.iloc[:, :1], df.iloc[:, -1],
                   df.iloc[:, -3], df.iloc[:, -5]], axis=1)

    new_column_names = ['District', 'Low', 'Middle', 'High']
    df.columns.values[:] = new_column_names
    dis = []
    for district in df['District']:
        dis.append(district.split()[0].upper().replace(" ", ""))

    df_no_district = df.drop(columns=['District'])
    df_no_district['Income'] = df_no_district.idxmax(axis=1)

    res = df_no_district[['Income']]
    res.insert(0, 'District', dis)

    return res


def ppIncome():
    folder = "DATA\\RNN Data\\income data"
    res = []
    for file in os.listdir(folder):
        df = pd.read_csv(folder+"\\"+file)

        df = ppSingleIncome(df)
        state = os.path.splitext(file)[0]
        df.insert(0, 'State', state)
        res.append(df)

    merged_df = pd.concat(res, ignore_index=True)
    merged_df = addDNO(merged_df)

    return merged_df


inc = ppIncome()
print(inc.head())
