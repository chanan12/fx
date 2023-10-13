new_currency_code = currency_code

if isinstance(start_date, str):
    start_date = datetime.strptime(start_date, "%d/%m/%Y")

data = [(currency_code, start_date, duration_of_historical_data, days_to_predict)]
df_parameters = pd.DataFrame(data)

df_parameters = df_parameters.rename(
    columns={
        0: "Currency_Code",
        1: "Start_Date",
        2: "Duration_Of_Historical_Data",
        3: "Days_To_Predict",
    }
)

# Convert Start_Date to datetime format
if df_parameters["Start_Date"].dtype == "O":
    df_parameters["Start_Date"] = pd.to_datetime(df_parameters["Start_Date"])

# Calculate new columns without changing the dtype
df_parameters["End_Date"] = df_parameters["Start_Date"] + pd.to_timedelta(
    df_parameters["Duration_Of_Historical_Data"] - 1, unit="d"
)

df_parameters["Start_Date_To_Predict"] = df_parameters["End_Date"] - pd.to_timedelta(
    df_parameters["Days_To_Predict"], unit="d"
)

df_parameters["End_Date_To_Predict"] = df_parameters["End_Date"]

# Reorder columns
df_parameters_his = df_parameters[
    ["Currency_Code", "Start_Date", "End_Date", "Duration_Of_Historical_Data"]
]

df_parameters_predict = df_parameters[
    [
        "Days_To_Predict",
        "Start_Date_To_Predict",
        "End_Date_To_Predict",
    ]
]