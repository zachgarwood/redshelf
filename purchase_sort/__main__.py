"""Main entry point"""

import sys

from . import data_file
from . import sorter

def main():
    """
    Load the external data files, sort the purchases into buckets, and then
    export the sorted data
    """

    buckets = data_file.import_buckets(data_file.BUCKETS_FILE_PATH)
    purchases = data_file.import_purchases(data_file.PURCHASES_FILE_PATH)
    sorted_purchases = sorter.sort_purchases(purchases, buckets)
    data_file.export_data(sorted_purchases)

if __name__ == '__main__':
    try:
        main()
    except Exception as exception:
        sys.stderr.write(str(exception) + '\n')
    finally:
        sys.exit()
