import pandas as pd
from pprint import pprint
import os

#######################################################################################
################### ADDING DNO TO A DATASET [NECESSARY FOR MERGING] ###################
#######################################################################################


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


def ppIncome(income_folder_path):
    res = []
    for file in os.listdir(income_folder_path):
        df = pd.read_csv(income_folder_path+"\\"+file)
        df = ppSingleIncome(df)
        print(df.head())
        res.append(df)

    merged_df = pd.concat(res, ignore_index=True)
    return merged_df


#######################################################################################
######################### PRE-PROCESSING DROPOUT DATA #################################
#######################################################################################

def ppDropout(dropout_folder_path):
    res = []

    for file in os.listdir(dropout_folder_path):
        file_path = dropout_folder_path+"\\"+file
        df = pd.read_csv(file_path)
        res.append(df)

    merged_df = pd.concat(res, ignore_index=True)
    columns = ['District']
    merged_df = merged_df.drop(columns=['Location'])

    return merged_df

#######################################################################################
######################### PRE-PROCESSING TOTAL SCHOOL  ################################
#######################################################################################


def ppTotalSchools(total_folder_path):
    res = []
    for file in os.listdir(total_folder_path):
        file_path = total_folder_path+"\\"+file
        df = pd.read_excel(file_path, skiprows=3)
        df = df.iloc[:, [0, -1]]
        df = df.groupby('Location').sum().reset_index()
        # df = df.drop([0, 1, 2]).reset_index(drop=True)
        res.append(df)
    merged_df = pd.concat(res, ignore_index=True)
    return merged_df

#######################################################################################
######################### MERGING FACTORS WITH DROP RATES #############################
#######################################################################################


def mergeWithRates(dropdf, df):
    df_merged = pd.merge(df, dropdf, on='DNo', how='right')
    new_order = ['DNo', 'District', 'Social Category', 'Income',
                 'prim_Girls', 'prim_Boys', 'prim_Overall',
                 'upPrim_Girls', 'upPrim_Boys', 'upPrim_Overall',
                 'snr_Girls', 'snr_Boys', 'snr_Overall']

    # Reorder DataFrame
    df_merged = df_merged[new_order]
    df_merged['Income'] = df_merged['Income'].fillna(method='ffill')
    return df_merged


def exportFinal(df, path):
    df.to_csv(path, index=False)


income_folder_path = "DATA\\RNN Data\\income data"
dropout_folder_path = "DATA\\Test\\DistrictWiseData"
total_folder_path = "DATA\\RNN Data\\Number of schools"
final_path = "DATA\\RNN Data\\final.csv"

# Preprocessing income
inc = ppIncome(income_folder_path)
# print(inc)

# Preprocessing totalschools
tot = ppTotalSchools(total_folder_path)
# print(tot)

# Adding dno to income
inc = addDNO(inc)

tot = addDNO(tot)
# print(tot)

# # preprocessing dropout rates
# drop = ppDropout(dropout_folder_path)

# # preparing final dataset
# merged = mergeWithRates(drop, inc)

# # exporting final dataset
# exportFinal(merged, final_path)
