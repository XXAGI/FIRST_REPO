from typing import List, Dict, Any

def process_todos(raw_todos: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Processes a list of raw todo items.
    For this example, it filters for essential information and perhaps
    could transform it if needed.

    Args:
        raw_todos: A list of dictionaries, where each dictionary represents a raw todo item
                   (e.g., from JSONPlaceholder). Expected keys: 'userId', 'id', 'title', 'completed'.

    Returns:
        A list of processed todo items, each containing 'id', 'title', and 'completed' status.
        Returns an empty list if input is empty or items are malformed.
    """
    processed_list = []
    if not raw_todos:
        return processed_list

    for todo in raw_todos:
        try:
            # Ensure essential keys are present
            if 'id' in todo and 'title' in todo and 'completed' in todo:
                # Add a specific check for the type of 'completed'
                if not isinstance(todo["completed"], bool):
                    print(f"Skipping todo item {todo.get('id', 'Unknown ID')} due to non-boolean 'completed' field: {todo['completed']}")
                    continue # Skip if 'completed' is not a boolean

                processed_list.append({
                    "id": int(todo["id"]),
                    "title": str(todo["title"]),
                    "completed": todo["completed"] # Already a bool
                })
            else:
                print(f"Skipping malformed todo item: {todo}")
        except (TypeError, ValueError) as e:
            print(f"Error processing todo item {todo.get('id', 'Unknown ID')}: {e}")
            # Optionally, decide whether to skip or handle more gracefully
            continue

    return processed_list

def simple_data_transform(data: List[Dict[str, Any]], key_to_uppercase: str) -> List[Dict[str, Any]]:
    """
    A generic example of a data transformation function.
    This function converts the value of a specified key to uppercase for each item in a list of dictionaries.

    Args:
        data: A list of dictionaries.
        key_to_uppercase: The key whose string value should be converted to uppercase.

    Returns:
        A new list of dictionaries with the specified transformation applied.
        If the key is not found or its value is not a string, it remains unchanged.
    """
    transformed_data = []
    for item in data:
        new_item = item.copy() # Avoid modifying original data
        if key_to_uppercase in new_item and isinstance(new_item[key_to_uppercase], str):
            new_item[key_to_uppercase] = new_item[key_to_uppercase].upper()
        transformed_data.append(new_item)
    return transformed_data
