"""Import and export data to and from external files"""

import csv
import json

from .bucket import Bucket
from .purchase import Purchase

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

def import_buckets(file_path):
    """Import data from file and cast to Bucket"""

    data = import_data(file_path, BUCKETS_FILE_FIELDS)
    return [Bucket(**datum) for datum in data]

def import_purchases(file_path):
    """Import data from file and cast to Purchase"""

    data = import_data(file_path, PURCHASES_FILE_FIELDS)
    return [Purchase(**datum) for datum in data]

def import_data(file_path, field_names):
    """Import data from a file path"""

    with open(file_path) as file_handle:
        data = extract_data(file_handle, field_names)
    return data

def extract_data(iterable, field_names):
    """Extract csv data from an iterable into an OrderedDict with the appropriate field names"""

    reader = csv.DictReader(iterable, field_names)
    return [line for line in reader]

def export_data(sorted_purchases):
    """Serialize the sorted purchases data and export into a json file"""

    serialized_data = [{'bucket': str(entry['bucket']),
                        'purchases': [str(purchase) for purchase in entry['purchases']]}
                       for entry in sorted_purchases]
    with open(SORTED_PURCHASES_FILE_PATH, 'w') as output_file:
        json.dump(serialized_data, output_file)
