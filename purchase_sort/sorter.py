"""Sort purchases into buckets by certain criteria"""

def sort_purchases(purchases, buckets):
    """Return a list of buckets, each with a corresponding list of purchases"""

    sorted_purchases = []
    for bucket in buckets:
        sorted_purchases.append({'bucket': str(bucket), 'purchases': purchases})
    return sorted_purchases
