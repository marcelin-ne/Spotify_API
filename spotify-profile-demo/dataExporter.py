import csv
import json

class DataExporter:
    @staticmethod
    def export_to_csv(data, file_name):
        """
        Export data to a CSV file.
        
        Args:
            data: A list of dictionaries where each dictionary represents a row of data.
            file_name: The name of the CSV file to be created.
        """
        with open(file_name, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        print(f"Data has been exported to {file_name} successfully.")

    @staticmethod
    def export_to_json(data, file_name):
        """
        Export data to a JSON file.
        
        Args:
            data: A list of dictionaries representing the data.
            file_name: The name of the JSON file to be created.
        """
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
        print(f"Data has been exported to {file_name} successfully.")
