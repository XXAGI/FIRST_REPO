import sys
import argparse # Import argparse
from typing import List, Dict, Any # For type hinting if needed later for args

from data_fetcher import api_client, data_processor

def main():
    """
    Main function to fetch, process, and display data from JSONPlaceholder.
    Allows specifying the number of todo items to fetch via a command-line argument.
    """
    parser = argparse.ArgumentParser(description="Fetch and process todo items from JSONPlaceholder.")
    parser.add_argument(
        "--limit",
        type=int,
        default=5,
        help="Number of todo items to fetch (default: 5)."
    )
    args = parser.parse_args()

    print(f"Starting data fetching process for {args.limit} items...")

    api_url = f"https://jsonplaceholder.typicode.com/todos?_limit={args.limit}"

    try:
        raw_data: List[Dict[str, Any]] = api_client.fetch_data_from_source(api_url)
    except Exception as e:
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

    # Display the data
    print("\nProcessed Todo List:")
    if processed_data:
        for item in processed_data:
            status = "Completed" if item['completed'] else "Pending"
            print(f"- ID: {item['id']}, Title: \"{item['title']}\", Status: {status}")
    else:
        print("No data to display after processing.")

if __name__ == "__main__":
    main()
