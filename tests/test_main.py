import json
import matplotlib.pyplot as plt
from prettytable import PrettyTable
from test_utils import *


api_key = ""
series_id = "CUUR0000SA0"  
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
    cpi_data = bls_response.get("Results", {}).get("series", [])[0].get("data", [])
else:
    print("⚠️ No valid data found in BLS response.")
    cpi_data = []
print(cpi_data)

# Calculate Year-over-Year Inflation
# Loop through the data and compare each month with the same month from the previous year.
inflation_rates = {}

for i in range(len(cpi_data)) : # loop through cpi_data, stop count equal to the amount of items in cpi_data list (60)
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


# Print as table or values
# table = PrettyTable(["date", "inflation_rate"])
# for date, rate in sorted(inflation_rates.items()):
#     table.add_row([date, rate])
# print(table)

# for period, rate in inflation_rates.items():
#     print(f"{period}: {rate}%")

# Plot
x = list(inflation_rates.keys())
x = x[::-1]
y = list(inflation_rates.values())
y = y[::-1]


plt.figure(figsize=(12, 6)) # Bigger window
plt.gcf().canvas.manager.set_window_title("U.S. Inflation Rate - BLS") # Window title
plt.title("U.S. Inflation Rate:\nYear-over-Year", fontweight="bold", fontsize=16)
plt.grid(True, axis='y', linestyle='--', linewidth=0.5, alpha=0.7)

plt.plot(x, y, c="crimson", linewidth=2.5, marker='o', label="Inflation Rate") # Line color, width, dots, label
n = 6
plt.xticks(ticks=range(0, len(x), n), labels=[x[i] for i in range(0, len(x), n)], rotation=45, fontsize=10)
plt.yticks(fontsize=10)
plt.ylim(min(y)-1, max(y)+1)
plt.xlabel("Date", fontweight="bold", fontsize=12)
plt.ylabel("Rate %", fontweight="bold", fontsize=12)
plt.legend()

plt.tight_layout() # Window fits to graph size
plt.show()