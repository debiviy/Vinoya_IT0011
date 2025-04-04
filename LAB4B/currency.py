import csv

def load_exchange_rates(filename):
    """Loads exchange rates from a CSV file into a dictionary."""
    exchange_rates = {}
    try:
        with open(filename, mode='r', newline='', encoding='ISO-8859-1') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                if len(row) == 3:
                    code, name, rate = row
                    try:
                        exchange_rates[code] = float(rate)
                    except ValueError:
                        print(f"Error: Invalid rate value for currency code {code}. Skipping entry.")
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return exchange_rates

def convert_currency(amount, currency, rates):
    """Converts the given amount from USD to the target currency using exchange rates."""
    if currency in rates:
        return amount * rates[currency]
    else:
        print(f"Error: Currency '{currency}' not found.")
        return None

def main():
    filename = r'LAB4B\currency.csv'  # Update this with the correct path if necessary
    rates = load_exchange_rates(filename)

    if not rates:
        print("No exchange rates loaded. Exiting.")
        return
    
    try:
        amount = float(input("How many dollars do you have? "))
        currency = input("What currency do you want to convert to? ").upper()
        
        # Perform currency conversion
        converted_amount = convert_currency(amount, currency, rates)
        
        if converted_amount is not None:
            print(f"\nUSD: {amount} USD")
            print(f"{currency}: {converted_amount}")
    except ValueError:
        print("Error: Invalid input. Please enter a valid number for the amount.")

if __name__ == "__main__":
    main()
