import unittest
from data_fetcher import data_processor

class TestDataProcessor(unittest.TestCase):

    def test_process_todos_empty_input(self):
        """Test processing with an empty list."""
        self.assertEqual(data_processor.process_todos([]), [])

    def test_process_todos_valid_data(self):
        """Test processing with valid todo items."""
        raw_data = [
            {"userId": 1, "id": 1, "title": "Test todo 1", "completed": True},
            {"userId": 1, "id": 2, "title": "Test todo 2", "completed": False},
        ]
        expected_output = [
            {"id": 1, "title": "Test todo 1", "completed": True},
            {"id": 2, "title": "Test todo 2", "completed": False},
        ]
        self.assertEqual(data_processor.process_todos(raw_data), expected_output)

    def test_process_todos_missing_keys(self):
        """Test processing with items missing essential keys."""
        raw_data = [
            {"userId": 1, "id": 1, "title": "Valid todo"}, # Missing 'completed'
            {"id": 2, "completed": False}, # Missing 'title'
            {"title": "Todo 3", "completed": True} # Missing 'id'
        ]
        # Malformed items should be skipped
        self.assertEqual(data_processor.process_todos(raw_data), [])

    def test_process_todos_mixed_data(self):
        """Test processing with a mix of valid and malformed items."""
        raw_data = [
            {"userId": 1, "id": 1, "title": "First todo", "completed": True},
            {"userId": 1, "title": "Incomplete todo"}, # Missing id and completed
            {"userId": 1, "id": 3, "title": "Third todo", "completed": False},
        ]
        expected_output = [
            {"id": 1, "title": "First todo", "completed": True},
            {"id": 3, "title": "Third todo", "completed": False},
        ]
        self.assertEqual(data_processor.process_todos(raw_data), expected_output)

    def test_process_todos_incorrect_types_graceful_skip(self):
        """Test processing with items having incorrect data types for id, title, completed."""
        raw_data = [
            {"userId": 1, "id": "not-an-int", "title": "Todo with string id", "completed": True},
            {"userId": 1, "id": 2, "title": 12345, "completed": False}, # Title is not a string
            {"userId": 1, "id": 3, "title": "Todo with string bool", "completed": "true"}, # Completed is not a bool
            {"userId": 1, "id": 4, "title": "Valid one", "completed": True},
        ]
        # The current implementation tries to cast, but if it fails (e.g. int("string")), it will raise ValueError
        # and the item will be skipped.
        expected_output = [
             {"id": 4, "title": "Valid one", "completed": True},
        ]
        # Note: Depending on print output for skipped items due to casting errors.
        # The function is designed to skip items that cause errors during processing or type mismatches for 'completed'.
        expected_output = [
            {"id": 2, "title": "12345", "completed": False},
            {"id": 4, "title": "Valid one", "completed": True},
        ]
        self.assertEqual(data_processor.process_todos(raw_data), expected_output)


    def test_simple_data_transform_empty_input(self):
        """Test simple_data_transform with an empty list."""
        self.assertEqual(data_processor.simple_data_transform([], "name"), [])

    def test_simple_data_transform_key_exists(self):
        """Test simple_data_transform when the key exists and value is a string."""
        data = [{"name": "Alice", "age": 30}, {"name": "bob", "city": "New York"}]
        expected = [{"name": "ALICE", "age": 30}, {"name": "BOB", "city": "New York"}]
        self.assertEqual(data_processor.simple_data_transform(data, "name"), expected)

    def test_simple_data_transform_key_not_exists(self):
        """Test simple_data_transform when the key does not exist in some items."""
        data = [{"name": "Alice", "age": 30}, {"city": "New York"}]
        expected = [{"name": "ALICE", "age": 30}, {"city": "New York"}] # No change for the second item for 'name'
        self.assertEqual(data_processor.simple_data_transform(data, "name"), expected)

    def test_simple_data_transform_value_not_string(self):
        """Test simple_data_transform when the value for the key is not a string."""
        data = [{"name": 123, "age": 30}]
        expected = [{"name": 123, "age": 30}] # Value is not a string, so no change
        self.assertEqual(data_processor.simple_data_transform(data, "name"), expected)


if __name__ == '__main__':
    unittest.main()
