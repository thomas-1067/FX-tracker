import requests
import datetime
import asciichartpy as chart
from art import text2art

def print_title():
    title = text2art("FX", font="block")
    print(title)

print_title()
print("\nExhange Rate Calculator and Plotter\n\nTom Stone-Wigg\nLondon, UK")
print(datetime.datetime.now().date())

class CurrencyConverter:
    def __init__(self):
        self.supported_currencies = self.get_supported_currencies()

    def get_supported_currencies(self):
        """Fetch the list of supported currencies from the Frankfurter API."""
        try:
            response = requests.get("https://api.frankfurter.app/currencies")
            if response.status_code == 200: # http == ok
                return response.json()
            else:
                print("Error fetching supported currencies.")
                return None
        except Exception as e:
            print(f"Error retrieving supported currencies: {e}") # catch errors
            return None

    def get_valid_currency(self, prompt):
        """Prompt user until a valid currency code is provided."""
        while True:
            currency = input(prompt).upper()
            if currency in self.supported_currencies:
                return currency
            else:
                print("\nInvalid currency code. Please enter a valid 3-letter currency code (e.g., USD, EUR).")
                print("Supported currencies:", ", ".join(self.supported_currencies.keys()) + "\n") # take keys only from dict

    def get_valid_date(self, prompt):
        """Prompt user until a valid date in YYYY-MM-DD format is provided."""
        while True:
            date_str = input(prompt)
            try:
                if len(date_str) != 10:
                    raise ValueError("\nInvalid input: number of characters must be 10. Include leading zeros where necessary.\n")
                date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
                if date_obj > datetime.datetime.now():
                    raise ValueError("\nInvalid input: Date cannot be in the future.")
                elif date_obj < datetime.datetime(2000, 1, 1):
                    raise ValueError("\nInvalid input: Date cannot be before 2000-01-01.")
                return date_str
            except ValueError as e:
                print(e)

    def get_valid_amount(self, amount=None):
        """Prompt user until a valid amount is provided or use the provided amount."""
        try:
            if amount is None:
                amount = float(input("Enter the amount to convert (e.g., 100000): "))
            else:
                amount = float(amount)

            if amount > 0:
                return amount
            else:
                raise ValueError("Amount must be positive.")
        except ValueError:
            print("\nInvalid amount. Setting amount to 1.\n")
            return 1

    def get_annual_exchange_rate_data(self, base_currency, target_currency):
        """Get exchange rate data for January 1st and July 1st for each year from 2000 to 2024."""
        combined_rates = []
        try:
            for year in range(2000, 2025):
                # Get rate for January 1st
                jan_date = f"{year}-01-01"
                response = requests.get(f"https://api.frankfurter.app/{jan_date}?from={base_currency}&to={target_currency}")
                if response.status_code == 200:
                    data = response.json()
                    rate = data.get('rates', {}).get(target_currency)
                    if rate:
                        combined_rates.append(rate)

                # Get rate for July 1st
                jul_date = f"{year}-07-01"
                response = requests.get(f"https://api.frankfurter.app/{jul_date}?from={base_currency}&to={target_currency}")
                if response.status_code == 200:
                    data = response.json()
                    rate = data.get('rates', {}).get(target_currency)
                    if rate:
                        combined_rates.append(rate)

            return combined_rates if combined_rates else None # Return list as-is if it contains data

        except Exception as e:
            print(f"Error retrieving data: {e}")
            return None

    def get_day_rate(self, base_currency, target_currency, specific_date):
        """Get exchange rate for a specific day."""
        try:
            response = requests.get(f"https://api.frankfurter.app/{specific_date}?from={base_currency}&to={target_currency}")
            if response.status_code == 200:
                data = response.json()
                return data.get('rates', {}).get(target_currency)
            else:
                print(f"Error fetching data for {specific_date}")
                return None
        except Exception as e:
            print(f"Error retrieving data: {e}")
            return None

    def generate_annual_plot(self, rates, base_currency, target_currency, specific_year, specific_date):
        """
        Generate an ASCII chart for the exchange rate trend from 2000 to 2024
        and highlight the starting exchange rate with a dynamic baseline adjustment.
        """
        # Ensure rates are provided
        if not rates or len(rates) % 2 != 0: # Check rates has data and is even (jan and july for each year)
            print("No valid rates to plot or inconsistent number of data points.")
            return

        # Define the years range
        years = list(range(2000, 2025))

        # Index for the specific year in years (jan)
        year_index = years.index(specific_year)

        # Indexing for the baseline
        data_index = year_index * 2  # Default to January data index (times 2 as 2 data points per year)
        if 7 <= datetime.datetime.strptime(specific_date, "%Y-%m-%d").month <= 12:
            data_index += 1  # Use July data if in the second half of the year

        # Create the baseline array
        baseline = [rates[0]] * data_index + [rates[data_index]] * (len(rates) - data_index)

        # Chart title
        chart_title = f"\nExchange Rate Trend: {base_currency} to {target_currency} from 2000 to 2024"
        print(chart_title)

        # Plot the chart with rates and baseline
        combined_data = [baseline, rates]
        print("\n" + chart.plot(combined_data, {"height": 12, "colors": [chart.red, chart.green]}) + "\n")

    def main(self):
        print
        if not self.supported_currencies:
            print("Unable to fetch the list of supported currencies.")
            return

        base_currency = self.get_valid_currency("\nEnter the base currency (e.g., USD): ")
        target_currency = self.get_valid_currency("Enter the target currency (e.g., EUR): ")
        specific_date = self.get_valid_date("Enter a specific date (YYYY-MM-DD): ")
        amount = self.get_valid_amount()

        date_obj = datetime.datetime.strptime(specific_date, "%Y-%m-%d")
        year = date_obj.year

        data = self.get_annual_exchange_rate_data(base_currency, target_currency)
        if not data:
            print("No data found for the given years.")
            return

        day_rate = self.get_day_rate(base_currency, target_currency, specific_date)
        if day_rate is None:
            print(f"No data found for {specific_date}.")
        else:
            converted_amount = amount * day_rate
            print(f"\nExchange rate on {specific_date} ({base_currency} to {target_currency}): {day_rate}")
            print(f"Amount {amount:.2f} {base_currency} is equivalent to {converted_amount:.2f} {target_currency}.")

        self.generate_annual_plot(data, base_currency, target_currency, year, specific_date)

if __name__ == "__main__":
    converter = CurrencyConverter()
    converter.main()
