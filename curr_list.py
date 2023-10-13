curr_list_df = pd.read_csv("curr_10.csv")
# Iterate through columns and convert each to string
for col in curr_list_df.columns:
    curr_list_df[col] = curr_list_df[col].astype(str)