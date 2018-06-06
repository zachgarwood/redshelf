"""Handle buckets"""

def create_bucket_label(bucket):
    """Concatenate bucket properties into a single label"""

    return ','.join([bucket['publisher'], bucket['price'], bucket['duration']])
