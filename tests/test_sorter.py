import pytest

from purchase_sort import sorter
from purchase_sort.bucket import Bucket
from purchase_sort.purchase import Purchase
from tests.helpers import *

MATCHING = 'MATCHING'
NONMATCHING = 'NONMATCHING'
WILDCARD = sorter.WILDCARD
PURCHASE_FIXTURE = {'publisher': MATCHING, 'duration': MATCHING, 'price': MATCHING,
                    'order_id': 'x', 'isbn': 'x', 'school': 'x', 'order_datetime': 'x'}

@pytest.fixture()
def buckets():
    """
    All possible matching/wildcard bucket criteria combinations, from most
    specific to least
    """
    matrix = [
        {'publisher': MATCHING, 'duration': MATCHING, 'price': MATCHING},
        {'publisher': MATCHING, 'duration': MATCHING, 'price': WILDCARD},
        {'publisher': MATCHING, 'duration': WILDCARD, 'price': MATCHING},
        {'publisher': WILDCARD, 'duration': MATCHING, 'price': MATCHING},
        {'publisher': MATCHING, 'duration': WILDCARD, 'price': WILDCARD},
        {'publisher': WILDCARD, 'duration': MATCHING, 'price': WILDCARD},
        {'publisher': WILDCARD, 'duration': WILDCARD, 'price': MATCHING},
        {'publisher': WILDCARD, 'duration': WILDCARD, 'price': WILDCARD},
    ]
    return [Bucket(**bucket_data) for bucket_data in matrix]

def test_meets_criteria_with_matching_criteria():
    purchase = Purchase(**PURCHASE_FIXTURE)
    bucket = Bucket(**{'publisher': MATCHING, 'duration': MATCHING, 'price': MATCHING})
    assert sorter.meets_criteria(bucket, purchase)

def test_meets_criteria_with_wildcards():
    purchase = Purchase(**PURCHASE_FIXTURE)
    bucket = Bucket(**{'publisher': MATCHING, 'duration': WILDCARD, 'price': WILDCARD})
    assert sorter.meets_criteria(bucket, purchase)

def test_meets_criteria_with_nonmatching_criteria():
    purchase = Purchase(**PURCHASE_FIXTURE)
    bucket = Bucket(**{'publisher': NONMATCHING, 'duration': NONMATCHING, 'price': NONMATCHING})
    assert not sorter.meets_criteria(bucket, purchase)

def test_meets_criteria_is_case_insensitive():
    purchase = Purchase(**PURCHASE_FIXTURE)
    bucket = Bucket(**{'publisher': MATCHING.lower(),
                       'duration': MATCHING.lower(),
                       'price': MATCHING.lower()})
    assert sorter.meets_criteria(bucket, purchase)

def test_find_specificity(buckets):
    for index, bucket in enumerate(buckets):
        # Check against all preceeding buckets
        for more_specific_bucket in buckets[:index]:
            assert sorter.find_specificity(bucket) < sorter.find_specificity(more_specific_bucket)
