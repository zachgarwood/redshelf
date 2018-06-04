"""Sort purchases into buckets by certain criteria."""
import csv
import json
import sys

BUCKETS_FILE_FIELDS = ['publisher', 'price', 'duration']
BUCKETS_FILE_PATH = 'data/purchase_buckets.csv'
PURCHASES_FILE_FIELDS = ['order_id',
                         'isbn',
                         'publisher',
                         'school',
                         'price',
                         'duration',
                         'order_datetime']
PURCHASES_FILE_PATH = 'data/purchase_data.csv'
SORTED_PURCHASES_FILE_PATH = 'sorted_purchases.json'

def main():
    """Main entry point"""

    buckets = import_from_file(BUCKETS_FILE_PATH, BUCKETS_FILE_FIELDS)
    purchases = import_from_file(PURCHASES_FILE_PATH, PURCHASES_FILE_FIELDS)

    with open(SORTED_PURCHASES_FILE_PATH, 'w') as output_file:
        json.dump(buckets, output_file)

def import_from_file(file_path, field_names):
    """Import csv data from a file path into an OrderedDict with the appropriate field names."""

    data = []
    with open(file_path) as file_handle:
        reader = csv.DictReader(file_handle, field_names)
        for line in reader:
            data.append(line)
    return data

if __name__ == '__main__':
    try:
        main()
    except Exception as exception:
        sys.stderr.write(str(exception) + '\n')
    finally:
        sys.exit()
