"""Sort purchases into buckets by certain criteria"""

"""
These criteria are the purchase attributes that we use to sort purchases into
the appropriate buckets. They are listed in order from least specific to most,
with their index in the list being their implicit specificity weight.
See find_specificity().
"""
CRITERIA = ['price', 'duration', 'publisher']
WILDCARD = '*'

def sort_purchases(purchases, buckets):
    """
    Return a list of buckets, each with a corresponding list of purchases.

    First, create a list of purchases with their corresponding most specific
    matching bucket. Then, create and return a new list of bucketed purchases
    by iterating over the list of buckets and, for each one, pulling from the
    purchases list all the entries with that bucket, being sure to skip over
    any buckets that already appear in the list.
    """

    purchases_with_matching_bucket = [find_most_specific_bucket(purchase, buckets)
                                      for purchase in purchases]

    return [{'bucket': bucket,
             'purchases': [matched_purchase['purchase']
                           for matched_purchase in purchases_with_matching_bucket
                           if matched_purchase['bucket'] == bucket
                           if matched_purchase['bucket'] not in buckets[:index]]}
            for index, bucket in enumerate(buckets)]

def find_most_specific_bucket(purchase, buckets):
    """Find the most specific bucket for a given purchase."""

    matching_buckets = [bucket for bucket in buckets if meets_criteria(bucket, purchase)]
    most_specific_bucket = sorted(matching_buckets, key=find_specificity, reverse=True)[0]
    return {'purchase': purchase, 'bucket': most_specific_bucket}

def meets_criteria(bucket, purchase):
    """
    Compare a purchase's attributes to a bucket's criteria.

    If all of the bucket and purchase criteria match (or the bucket contains
    wildcards), return True. Criteria comparisons are case-insensitive.
    """

    for criterion in CRITERIA:
        bucket_attribute = getattr(bucket, criterion).lower()
        if bucket_attribute != WILDCARD and\
           bucket_attribute != getattr(purchase, criterion).lower():
            return False
    return True

def find_specificity(bucket):
    """
    Determine a bucket's specificity.

    Specificity is determined by how many nonwildcard criteria matches it
    contains, and, in case of a tie, the weight of the most specific matching
    criteria. The weight of the criteria is determined by the order of
    CRITERIA which is listed from least specific to most. The index of each
    criteria in the list is used as its implicit weight.

    To accomplish all this we calculate a specificity score that is a two
    digit decimal number where the 10s position represents the number of
    nonwildcard matches and the 1s position represents the weight of the
    most specific criteria.

    Examples:

    {'publisher': 'wildcard',
     'duration': 'matching value',
     'price': 'matching value'}
    This bucket has two nonwildcard matching values, so it gets a `matches`
    value of '20'. And its most specific criteria value is 'duration', which
    has an index in CRITERIA of '1', so it gets a `weight` value of '1'. When
    we add these to values together, we get a total specificity score of '21'.

    {'publisher': 'matching value',
     'duration': 'matching value',
     'price': 'wildcard'}
    Compare the previous bucket to this one. It has a also has a `matches`
    value of '20' but the `weight` value is '2' due to the most specific
    criteria being 'publisher'. So its specificity score comes out to '22'.
    """

    matches = 0
    weight = 0
    for index, criterion in enumerate(CRITERIA):
        if getattr(bucket, criterion) != WILDCARD:
            matches += 10
            weight = index
    return matches + weight
