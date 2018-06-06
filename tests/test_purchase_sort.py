import pytest

from purchase_sort.__main__ import main as purchase_sort
from tests.helpers import *

@pytest.fixture(scope='module')
def output_file():
    output_file = purchase_sort()
    yield output_file 
    delete_output_file()

def test_output_file_is_created(output_file):
    assert output_file_exists()

def test_output_file_is_in_correct_format(output_file):
    sorted_purchases = get_sorted_purchases()
    assert isinstance(sorted_purchases, list)

    bucket = sorted_purchases.pop()
    assert 'bucket' in bucket
    assert isinstance(bucket['purchases'], list)

def test_output_file_is_in_correct_order(output_file):
    buckets = get_buckets()
    sorted_purchases = get_sorted_purchases()
    for index, bucket in enumerate(sorted_purchases):
        assert unserialize_bucket(bucket['bucket']) == buckets[index],\
               'The output bucket is equal to the input bucket at the same index in both lists.'
        purchases = [unserialize_purchase(purchase) for purchase in bucket['purchases']]
        assert purchases == sorted(purchases, key=lambda purchase: purchase.order_id),\
               'The output purchases are sorted by order_id.'

def test_duplicate_buckets_in_output_file_are_empty(output_file):
    buckets = get_buckets()
    duplicates = set(str(bucket)
                        for index, bucket in enumerate(buckets)
                        if bucket in buckets[:index])
    sorted_purchases = get_sorted_purchases()
    examined_duplicates = set() 
    for bucket in sorted_purchases:
        bucket_label = bucket['bucket']
        if bucket_label in duplicates:
            if bucket_label in examined_duplicates:
                assert bucket['purchases'] == [],\
                       'If the bucket is a duplicate and it is not the first copy, then it '\
                       'should not have any corresponding purchases.'
            else:
                examined_duplicates.add(bucket_label)
