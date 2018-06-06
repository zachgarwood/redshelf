"""Main entry point"""

import sys

from . import data_io
from . import sorter

def main():
    """
    Load the external data files, sort the purchases into buckets, and then
    export the sorted data
    """

    buckets = data_io.import_buckets(data_io.BUCKETS_FILE_PATH)
    purchases = data_io.import_purchases(data_io.PURCHASES_FILE_PATH)
    sorted_purchases = sorter.sort_purchases(purchases, buckets)
    data_io.export_data(sorted_purchases)

if __name__ == '__main__':
    try:
        main()
    except Exception as exception:
        sys.stderr.write(str(exception) + '\n')
    finally:
        sys.exit()
