"""Import and export data to and from external files"""

import csv
import json

from .bucket import Bucket

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

def import_data(file_path, field_names):
    """Import csv data from a file path into an OrderedDict with the appropriate field names"""

    data = []
    with open(file_path) as file_handle:
        reader = csv.DictReader(file_handle, field_names)
        for line in reader:
            data.append(line)
    return data

def export_data(sorted_purchases):
    """Export sorted purchase data into a json file"""

    with open(SORTED_PURCHASES_FILE_PATH, 'w') as output_file:
        json.dump(sorted_purchases, output_file)
