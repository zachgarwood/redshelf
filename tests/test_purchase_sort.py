from unittest import TestCase
import os
import purchase_sort

class TestPurchaseSort(TestCase):

    def setUp(self):
        self.delete_output_file()

    def tearDown(self):
        self.delete_output_file()

    def test_purchase_sort_creates_json_file(self):
        """Assert running the program outputs a json file"""

        purchase_sort.main()
        assert os.path.exists(purchase_sort.SORTED_PURCHASES_FILE_PATH)

    def delete_output_file(self):
        if (os.path.exists(purchase_sort.SORTED_PURCHASES_FILE_PATH)):
            os.remove(purchase_sort.SORTED_PURCHASES_FILE_PATH)