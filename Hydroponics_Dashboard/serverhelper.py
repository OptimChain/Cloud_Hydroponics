def simulated_read():
    import json
    from random import random
    #Append simulated telemetry
    with open('web_partition.json') as f:
    
        r = json.load(f)
        
        row_count = len(r)-1
        print("Reading " + str(row_count) + " rows")
        last_row = r[row_count]
        

        #Append simulated telemetry
        timestamp = last_row[0] + 5
        value = last_row[1] + -0.5 + random()
        mean = last_row[2] 
        upper_bound = last_row[3]
        lower_bound = last_row[4]
        
        new_row = [timestamp, value, mean, upper_bound, lower_bound]
        
        r.append(new_row)
        f.close()

        jsonString = json.dumps(r)
        jsonFile = open("example.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
        return(r)
    
def production_read(path_filter):
    from azure.storage.blob import BlobClient
    from azure.storage.blob import ContainerClient
    import json
    import pandas as pd

    conn_str="DefaultEndpointsProtocol=https;AccountName=hydrostor;AccountKey=9kCdLW+i7CYyiAjSaiHOeWDsgE8Nm5yBME/wyjE03vLLZEm97ocdXvoEJxuTUhhuKr9c4ebm5dumXvlF7PBWFA==;EndpointSuffix=core.windows.net"
    
    container_name="flowdatacontainer"
    
    def save_json_local(conn_str, container_name):
    
        #This Function Parses all the blob contents within hydrostor
    
        container = ContainerClient.from_connection_string(conn_str=conn_str, container_name=container_name)
    
        blob_paths = []
        #Print blobs from blob list
        blob_list = container.list_blobs()
        for blob in blob_list:
            print(blob.name + '\n')
            blob_paths.append(blob.name)
        return(blob_paths)
    
    def parse_json(path):
        #This function converts a list of filtered blob paths into a single json manifest
        import json
    
        final_ls = []
        for line in open('partition.json', 'r'):
            temp_dict = json.loads(line)
            ts = temp_dict['Body']['timestamp']
            pulse = temp_dict['Body']['pulse']
            temp_ls = []
            temp_ls.append(ts)
            temp_ls.append(pulse)
            final_ls.append(temp_ls)
    
        return(final_ls)
    
    def filter_blob_paths(blob_paths, substring):
        # This function filters for all json blobs within the chosen substring
    
        filtered_blob_paths = []
    
        for i in blob_paths:
            if substring in i and ".json" in i:
                filtered_blob_paths.append(i)
    
        column_names = ["timestamp", "pulse"]
        df = pd.DataFrame(columns = column_names)
    
    
        for i in filtered_blob_paths:
            blob = BlobClient.from_connection_string(conn_str=conn_str, container_name=container_name, blob_name=i)
            with open("./partition.json", "wb") as my_blob:
                blob_data = blob.download_blob()
                blob_data.readinto(my_blob)
    
            temp_ls = parse_json("./partition.json")
            df = df.append(pd.DataFrame(temp_ls, columns = ["timestamp", "pulse"]), ignore_index=True)
    
        return df
    
    def calc_control_limits(df):
        mean = df["pulse"].mean()
        std = df["pulse"].std()
        ub = mean + 2*std
        lb = mean - 2*std
    
        df['mean'] = mean
        df['ub'] = ub
        df['lb'] = lb
        return df
    
    def standardize(df):
        df = df.reset_index(drop=True).to_json(orient='values')
        return df
    
    blob_paths = save_json_local(conn_str, container_name)
    df = filter_blob_paths(blob_paths, path_filter)
    final_df = calc_control_limits(df)
    df_json = json.loads(standardize(final_df))
    
    
    with open('web_partition.json', 'w') as outfile:
        json.dump(df_json, outfile)
        
    return(df_json)

