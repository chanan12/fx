# Create the date range
date_range = pd.date_range(start=start_date, periods=int(history_duration))

date_df = pd.DataFrame({"Date": date_range.strftime("%d/%m/%Y"), "ID": range(1, int(history_duration)+1)})
date_df_predict = pd.DataFrame({"Date": date_range.strftime("%d/%m/%Y"), "ID": range(1, int(history_duration)+1)})
