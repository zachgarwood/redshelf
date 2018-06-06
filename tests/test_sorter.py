import pytest

from purchase_sort import sorter
from purchase_sort.bucket import Bucket
from purchase_sort.purchase import Purchase 

MATCHING = 'MATCHING'
NONMATCHING = 'NONMATCHING'
WILDCARD = sorter.WILDCARD
PURCHASE_FIXTURE = {'publisher': MATCHING, 'duration': MATCHING, 'price': MATCHING,
                    'order_id': 'x', 'isbn': 'x', 'school': 'x', 'order_datetime': 'x'}

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

def test_find_specificity_accounts_for_number_of_matches():
    bucket_one_match = Bucket(**{'publisher': MATCHING,
                                 'duration': WILDCARD,
                                 'price': WILDCARD})
    bucket_two_matches = Bucket(**{'publisher': MATCHING,
                                   'duration': MATCHING,
                                   'price': WILDCARD})
    assert sorter.find_specificity(bucket_one_match) <\
           sorter.find_specificity(bucket_two_matches),\
           'A bucket with one matching criteria is less specific than a bucket with two.'

def test_find_specificity_accounts_for_weight_of_matches():
    bucket_duration_specific = Bucket(**{'publisher': WILDCARD,
                                         'duration': MATCHING,
                                         'price': WILDCARD})
    bucket_publisher_specific = Bucket(**{'publisher': MATCHING,
                                          'duration': WILDCARD,
                                          'price': WILDCARD})
    assert sorter.find_specificity(bucket_duration_specific) <\
           sorter.find_specificity(bucket_publisher_specific),\
           'Given that two buckets have the same amount of matching criteria, a bucket with a '\
           'lower weighted criteria match is less specific.'
