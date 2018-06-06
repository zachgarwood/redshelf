"""Sort purchases into buckets by certain criteria"""

from . import bucket

def sort_purchases(purchases, buckets):
    """Return a list of buckets, each with a corresponding list of purchases"""

    sorted_purchases = []
    for b in buckets:
        bucket_label = bucket.create_bucket_label(b)
        sorted_purchases.append({'bucket': bucket_label, 'purchases': purchases})
    return sorted_purchases
