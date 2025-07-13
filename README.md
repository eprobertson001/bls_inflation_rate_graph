# BLS Inflation Rate API
This portfolio project works by fetching recent U.S. inflation rate data from [BLS.gov](https://www.bls.gov/) official API, calculating the results, and  transforming the data into a useful clear, professional visualization.

## Overview

- **Purpose:** Fetch and visualize the most recent U.S. year-over-year inflation rate data.
- **Data Source:** Bureau of Labor Statistics (BLS) API.
- **Visualization:** Clean, publication-ready graph using `matplotlib`.
- **Professional Relevance:** Showcases API integration, data analysis, and data visualization

## Features

- **API Integration:** Securely connects to the BLS public data API via POST requests.
- **Data Parsing:** Transforms and cleans raw JSON responses to extract time series data.
- **Visualization:** Creates a clear, informative graph of inflation trends using `matplotlib`.
- **Error Handling:** Robust exception handling for API connectivity and data integrity.
- **Documentation:** Well-commented, readable code for easy maintenance and extension.

## Skills Demonstrated

- **Python Programming:** Clean, modular, and idiomatic Python code.
- **API Consumption:** Working with RESTful APIs, authentication, and JSON parsing.
- **Data Analysis:** Transforming and analyzing economic time series data.
- **Data Visualization:** Creating professional graphics with `matplotlib`.
- **Best Practices:** Code documentation, error handling, and separation of concerns.
- **Portfolio Quality:** Suitable for technical interviews, code reviews, and as a proof of competency for data or software engineering positions.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- `requests` library
- `matplotlib` library

Install dependencies with pip:
```bash
pip install requests matplotlib
```

### Usage

1. **Clone the repository:**
    ```bash
    git clone https://github.com/eprobertson001/bls_inflation_rate_api.git
    cd bls_inflation_rate_api
    ```

2. **Run the script:**
    ```bash
    python bls_inflation.py
    ```
    *(Replace `bls_inflation.py` with the actual script name if different.)*

3. **View the Graph:**  
   The script will automatically display a matplotlib graph of recent U.S. inflation rates between 2020 and 2024.

## Example Output

![Sample Inflation Rate Graph](bls_inflation_rate_graph\img\inflation_graph_example.png)

## Customization

- **API Key:** If required, set up your BLS API key as instructed in the script or via environment variables.
- **Time Range:** Adjust the script parameters to fetch different time spans or inflation measures.

## Professional Notes

- **Extensible:** The code serves as a solid base for more advanced financial or economic data visualizations.

## License

This project is open-source and available under the [MIT License](LICENSE).

---

**Contact:**  
Evan Robertson  
[GitHub Profile](https://github.com/eprobertson001)
email: eprobertson001@gmail.com