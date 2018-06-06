from unittest import TestCase
import json
import os

from purchase_sort import data_file, sorter
from purchase_sort.__main__ import main as run_purchase_sort

class TestPurchaseSort(TestCase):

    def setUp(self):
        self.delete_output_file()
        run_purchase_sort()

    def tearDown(self):
        self.delete_output_file()

    def test_purchase_sort_creates_json_file(self):
        assert os.path.exists(data_file.SORTED_PURCHASES_FILE_PATH)

    def test_output_file_is_in_correct_format(self):
        sorted_purchases = self.get_sorted_purchases()
        assert isinstance(sorted_purchases, list)

        bucket = sorted_purchases.pop()
        assert 'bucket' in bucket
        assert isinstance(bucket['purchases'], list)

    def test_output_file_is_in_correct_order(self):
        buckets = self.get_buckets()
        sorted_purchases = self.get_sorted_purchases()
        for index, bucket in enumerate(buckets):
            assert sorted_purchases[index]['bucket'] == str(bucket)

    def test_duplicate_buckets_in_output_file_are_empty(self):
        pass

    def get_buckets(self):
        return data_file.import_buckets(data_file.BUCKETS_FILE_PATH)

    def get_sorted_purchases(self):
        with open(data_file.SORTED_PURCHASES_FILE_PATH) as output_file:
            sorted_purchases = json.load(output_file)
        return sorted_purchases

    def delete_output_file(self):
        if os.path.exists(data_file.SORTED_PURCHASES_FILE_PATH):
            os.remove(data_file.SORTED_PURCHASES_FILE_PATH)
