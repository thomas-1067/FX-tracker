# Exchange Rate Calculator and Plotter

#### Description:
The Exchange Rate Calculator and Plotter is a Python application designed to help users calculate real-time exchange rates between currencies and visualise historical trends from 2000 to 2024. By using the Frankfurter API, the program provides accurate and reliable currency data in an easy-to-use command-line interface. The tool features dynamic ASCII art for the title and exchange rate trends, making the experience both functional and visually engaging.

## Features
- **Real-Time Exchange Rates**: Instantly calculate the exchange rate for a specific day between two currencies, including the current day.
- **Historical Data Visualisation**: View simplified exchange rate trends from 2000 to 2024 as ASCII charts, directly in the terminal.
- **Input Validation**: Ensures valid inputs for currencies, dates, and amounts, with clear error messages for incorrect entries.
- **Dynamic Title**: Features an ASCII-art title generated with the `text2art` library.

## Files
### `project.py`
This is the main Python script that contains the following components:
1. **`print_title` Function**:
   Displays a large ASCII-art title ("FX") and some other info to introduce the program.

2. **`CurrencyConverter` Class**:
   - `__init__`: Initialises the program and fetches a list of supported currencies from the API.
   - `get_supported_currencies`: Retrieves a dictionary of available currencies from the Frankfurter API.
   - `get_valid_currency`: Prompts the user to input valid currency codes, checking them against the API's list.
   - `get_valid_date`: Ensures the user provides a valid date in the YYYY-MM-DD format and within the range of 2000 to today.
   - `get_valid_amount`: Verifies that the entered amount is positive and numeric, defaulting to 1 if invalid.
   - `get_annual_exchange_rate_data`: Fetches exchange rates for January and July of each year from 2000 to 2024
   - `get_day_rate`: Fetches the exchange rate for a specific date.
   - `generate_annual_plot`: Creates an ASCII chart showing exchange rate trends over the selected time range for the base and target currencies.
   - `main`: The program's main execution point, coordinating user input, calculations, and visualisations.

### `test_project.py`
This file contains unit tests for the project using the `pytest` framework. It ensures critical functions work as expected:
- `test_get_supported_currencies`: Verifies that the `get_supported_currencies` function retrieves a valid dictionary of supported currencies.
- `test_get_valid_amount`: Ensures that valid numeric amounts are accepted and invalid inputs are defaulted to 1.
- `test_get_day_rate`: Checks the retrieval of exchange rates for valid and invalid dates.

### `requirements.txt`
This file lists the Python libraries required to run the project:
- `requests`: For fetching exchange rate data from the API.
- `asciichartpy`: To generate ASCII charts for visualising trends.
- `pytest`: For running the test cases provided in `test_project.py`.
- `text2art`: For creating the ASCII title.

### `README.md`
This file explains the purpose of the project, outlines its features, and provides instructions for running the program. It also includes a link to the video demo and details about the design choices.

## Design Choices
1. **API Integration**:
   The Frankfurter API was chosen for its simplicity and reliability in providing exchange rate data. It supports various currencies, historical rates and is open-source, making it ideal for this project.

2. **Command-Line Interface**:
   A CLI was implemented to ensure cross-platform compatibility and a straightforward user experience. User inputs are validated to prevent invalid requests.

3. **ASCII Visualization**:
   To keep the project terminal-friendly, ASCII charts were chosen to visualize historical data using the `asciichartpy` library, and the `text2art` library was used to add a creative touch with the title.

4. **Error Handling**:
   User input is thoroughly validated to ensure smooth operation. For example, unsupported currencies, invalid dates, or negative amounts trigger helpful error messages to guide the user.

## How to Use
1. Run the script using Python: Run "python project.py" in the CLI

2. Follow the prompts to:
- Enter a base currency (e.g., USD).
- Enter a target currency (e.g., EUR).
- Provide a specific date (YYYY-MM-DD).
- Input the amount to convert.

3. The program will display:
- The exchange rate for the given date.
- The converted amount.
- An ASCII chart of historical exchange rate trends.

## Future Improvements
- **Additional Visualisations**: Add graphical charts using libraries like `matplotlib` for users who prefer more detailed and visually rich outputs.
- **Extended Date Range**: Support exchange rate data for years beyond 2000–2024 as additional data becomes available.
- **Multi-Currency Comparison**: Enable users to compare trends for multiple currencies side by side in the same chart.

---

This project showcases the power of Python and APIs to build practical, user-friendly tools.
