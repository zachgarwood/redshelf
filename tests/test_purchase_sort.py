from unittest import TestCase
import os
import purchase_sort
import json

class TestPurchaseSort(TestCase):

    def setUp(self):
        self.delete_output_file()
        purchase_sort.main()

    def tearDown(self):
        self.delete_output_file()

    def test_purchase_sort_creates_json_file(self):
        assert os.path.exists(purchase_sort.SORTED_PURCHASES_FILE_PATH)

    def test_output_file_is_in_correct_format(self):
        sorted_purchases = self.get_sorted_purchases()
        assert isinstance(sorted_purchases, list)

        bucket = sorted_purchases.pop()
        assert 'bucket' in bucket
        assert isinstance(bucket['purchases'], list)

    def test_output_file_is_in_correct_order(self):
        original_buckets = purchase_sort.import_from_file(purchase_sort.BUCKETS_FILE_PATH, purchase_sort.BUCKETS_FILE_FIELDS)
        sorted_purchases = self.get_sorted_purchases()
        for index, bucket in enumerate(original_buckets):
            bucket_label = purchase_sort.create_bucket_label(bucket)
            sorted_purchases[index]['bucket'] = bucket_label

    def get_sorted_purchases(self):
        with open(purchase_sort.SORTED_PURCHASES_FILE_PATH) as output_file:
            sorted_purchases = json.load(output_file)
        return sorted_purchases

    def delete_output_file(self):
        if (os.path.exists(purchase_sort.SORTED_PURCHASES_FILE_PATH)):
            os.remove(purchase_sort.SORTED_PURCHASES_FILE_PATH)