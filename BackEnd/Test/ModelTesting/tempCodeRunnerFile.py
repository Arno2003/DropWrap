    # # Loop through each CSV file and read it using pandas
    # for file in csv_files:
    #     file_path = os.path.join(directory_path, file)
    #     df = pd.read_csv(file_path)
    #     df1 = df.copy()
    #     df = df[df["Social Category"] == "Overall"]
        
    #     print(f'Read {file} successfully:')
        
    #     df.insert(0, "DNo", range(serialNo+1, serialNo+len(df)+1))
    #     df = df[["DNo", "Location"]]
        
    #     serialNo += 100
        
    #     df.to_csv(outPath+"\\"+f'{file.replace("_modified", "")}.csv', index=False)