"""Test helpers"""

import json
import os

from purchase_sort import data_file
from purchase_sort.bucket import Bucket
from purchase_sort.purchase import Purchase

def unserialize_bucket(bucket):
    """Unserialize a single csv-encoded bucket"""

    bucket_data = data_file.extract_data([bucket], data_file.BUCKETS_FILE_FIELDS)[0]
    return Bucket(**bucket_data)

def unserialize_purchase(purchase):
    """Unserialize a single csv-encoded purchase"""
    purchase_data = data_file.extract_data([purchase], data_file.PURCHASES_FILE_FIELDS)[0]
    return Purchase(**purchase_data)

def get_buckets():
    """Retrieve the unsorted bucket data"""

    return data_file.import_buckets(data_file.BUCKETS_FILE_PATH)

def get_sorted_purchases():
    """Retrieve the sorted bucket/purchase data"""

    with open(data_file.SORTED_PURCHASES_FILE_PATH) as output_file:
        sorted_purchases = json.load(output_file)
    return sorted_purchases

def output_file_exists():
    return os.path.exists(data_file.SORTED_PURCHASES_FILE_PATH)

def delete_output_file():
    """Delete the output sorted purchases json file"""

    if os.path.exists(data_file.SORTED_PURCHASES_FILE_PATH):
        os.remove(data_file.SORTED_PURCHASES_FILE_PATH)