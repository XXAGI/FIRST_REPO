import sys
import argparse # The argparse module makes it easy to write user-friendly command-line interfaces.
from typing import List, Dict, Any # Type hinting helps with code clarity and can be used by static analysis tools.

# Import custom modules from the data_fetcher package.
from data_fetcher import api_client, data_processor

def main():
    """
    The main entry point of the script.
    It orchestrates fetching, processing, and displaying data.
    """
    # Create an ArgumentParser object to handle command-line inputs.
    parser = argparse.ArgumentParser(description="Fetch and process todo items from JSONPlaceholder.")

    # Add a '--limit' argument. It expects an integer (type=int) and defaults to 5.
    parser.add_argument(
        "--limit",
        type=int,
        default=5,
        help="Number of todo items to fetch (default: 5)."
    )

    # Parse the arguments provided by the user.
    args = parser.parse_args()

    # f-strings (formatted string literals) allow embedding expressions inside string literals.
    print(f"Starting data fetching process for {args.limit} items...")

    # The URL of the API we want to fetch data from.
    api_url = f"https://jsonplaceholder.typicode.com/todos?_limit={args.limit}"

    try:
        # Call the fetch_data_from_source function from the api_client module.
        raw_data: List[Dict[str, Any]] = api_client.fetch_data_from_source(api_url)
    except Exception as e:
        # Error handling: if something goes wrong, print the error and exit the script.
        print(f"Error fetching data: {e}", file=sys.stderr)
        sys.exit(1)

    if not raw_data:
        print("No data fetched. Exiting.")
        sys.exit(0)

    print(f"Successfully fetched {len(raw_data)} items.")

    # Process the data
    try:
        processed_data = data_processor.process_todos(raw_data)
    except Exception as e:
        print(f"Error processing data: {e}", file=sys.stderr)
        sys.exit(1)

    print("Data processed successfully.")

    # Display the data to the console.
    print("\nProcessed Todo List:")
    if processed_data:
        # Iterate over each item in the processed_data list.
        for item in processed_data:
            # A ternary operator (conditional expression) to determine the status string.
            status = "Completed" if item['completed'] else "Pending"
            print(f"- ID: {item['id']}, Title: \"{item['title']}\", Status: {status}")
    else:
        print("No data to display after processing.")

# This idiom ensures that main() is only called if this script is run directly,
# not if it's imported as a module in another script.
if __name__ == "__main__":
    main()
