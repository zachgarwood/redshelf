"""Handle buckets"""

class Bucket:
    """Data object for buckets"""
    
    def __init__(self, **kwargs):
        self.publisher = kwargs['publisher']
        self.price = kwargs['price']
        self.duration = kwargs['duration']

    def __repr__(self):
        return ','.join([self.publisher, self.price, self.duration])
