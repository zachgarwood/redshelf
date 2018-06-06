import json
import os
import pytest

from purchase_sort import data_file, sorter
from purchase_sort.__main__ import main as run_purchase_sort

@pytest.fixture(scope='module')
def output_file():
    output_file = run_purchase_sort()
    yield output_file 
    delete_output_file()

def test_purchase_sort_creates_json_file(output_file):
    assert os.path.exists(data_file.SORTED_PURCHASES_FILE_PATH)

def test_output_file_is_in_correct_format(output_file):
    sorted_purchases = get_sorted_purchases()
    assert isinstance(sorted_purchases, list)

    bucket = sorted_purchases.pop()
    assert 'bucket' in bucket
    assert isinstance(bucket['purchases'], list)

def test_output_file_is_in_correct_order(output_file):
    buckets = get_buckets()
    sorted_purchases = get_sorted_purchases()
    for index, bucket in enumerate(buckets):
        assert sorted_purchases[index]['bucket'] == str(bucket)

@pytest.mark.xfail
def test_duplicate_buckets_in_output_file_are_empty(output_file):
    buckets = get_buckets()
    duplicates = set(str(bucket)
                        for index, bucket in enumerate(buckets)
                        if bucket in buckets[:index])
    sorted_purchases = get_sorted_purchases()
    examined_duplicates = set() 
    for sorted_bucket in sorted_purchases:
        bucket_label = sorted_bucket['bucket']
        if bucket_label in duplicates:
            if bucket_label in examined_duplicates:
                assert sorted_bucket['purchases'] == []
            else:
                examined_duplicates.add(bucket_label)

def get_buckets():
    return data_file.import_buckets(data_file.BUCKETS_FILE_PATH)

def get_sorted_purchases():
    with open(data_file.SORTED_PURCHASES_FILE_PATH) as output_file:
        sorted_purchases = json.load(output_file)
    return sorted_purchases

def delete_output_file():
    if os.path.exists(data_file.SORTED_PURCHASES_FILE_PATH):
        os.remove(data_file.SORTED_PURCHASES_FILE_PATH)
