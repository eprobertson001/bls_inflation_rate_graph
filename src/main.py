import requests
import json
import matplotlib.pyplot as plt
from prettytable import PrettyTable
from utils import *


api_key = ""  # Leave blank if you don't have one
series_id = "CUUR0000SA0"  # Series for CPI, All Urban Consumers 
start_year = "2020"
end_year = "2024"

url = "https://api.bls.gov/publicAPI/v2/timeseries/data/"
headers = {"Content-Type": "application/json"}
payload = {
    "seriesid": [series_id],
    "startyear": start_year,
    "endyear": end_year,
    "registrationkey": api_key
}

client = APIClient(path=url, headers=headers)
bls_response = client.post_api(endpoint="",json=payload)

if bls_response and "Results" in bls_response: # if bls_response is not empty and "Results" exists, extract data
    cpi_data = bls_response.get("Results", {}).get("series", [])[0].get("data", []) # Looks for the "Results" key in the data dictionary. Looks for the "series" key inside the "Results" dictionary. Gets the first item in the "series" list. Looks for the "data" key in the first series dictionary. If items don't exist, an empty list or dict is returned.
else:
    print("⚠️ No valid data found in BLS response.")
    cpi_data = []

# (option) Check data
# print(cpi_data)

# Calculate Year-over-Year Inflation
# Compare each month with the same month from the previous year.
inflation_rates = {}

for i in range(len(cpi_data)) : # loop through cpi_data equal to the amount of items in the list (60)
    current = cpi_data[i]
    current_month = current["periodName"]
    current_year = int(current["year"])
    current_value = float(current["value"])

    for j in range(i+1, len(cpi_data)):
        previous = cpi_data[j]
        if previous["periodName"] == current_month and int(previous["year"]) == current_year - 1:
            previous_value = float(previous["value"])
            inflation = ((current_value - previous_value) / previous_value) * 100
            inflation_rate = round(inflation, 2)
            inflation_rates[f"{current_year} {current_month}"] = inflation_rate
            break

# Plot line graph
x = list(inflation_rates.keys())
x = x[::-1] # reverse list order (oldest to newest)
y = list(inflation_rates.values())
y = y[::-1]

plt.figure(figsize=(12, 6)) # Bigger window
plt.gcf().canvas.manager.set_window_title("U.S. Inflation Rate - BLS") # Window title
plt.title("U.S. Inflation Rate:\nYear-over-Year", fontweight="bold", fontsize=16) # Graph title
plt.grid(True, axis='y', linestyle='--', linewidth=0.5, alpha=0.7) # Show grid background

plt.plot(x, y, c="crimson", linewidth=2.5, marker='o', label="Inflation Rate") # Line color, width, dots, label
n = 6
plt.xticks(ticks=range(0, len(x), n), labels=[x[i] for i in range(0, len(x), n)], rotation=45, fontsize=10) # x-axis tick labels/spacing
plt.yticks(fontsize=10)
plt.ylim(min(y)-1, max(y)+1) # y-axis range
plt.xlabel("Date", fontweight="bold", fontsize=12)
plt.ylabel("Rate %", fontweight="bold", fontsize=12)
plt.legend() # include legend
plt.tight_layout() # Graph fits to window size

plt.show()

# (option) Print as table

# table = PrettyTable(["date", "inflation_rate"])
# for date, rate in sorted(inflation_rates.items()):
#     table.add_row([date, rate])
# print(table)

# (Option) Print values
# for period, rate in inflation_rates.items():
#     print(f"{period}: {rate}%")
