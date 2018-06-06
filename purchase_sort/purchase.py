"""Handle purchases"""

class Purchase:
    """Data object for purchases"""

    def __init__(self, **kwargs):
        self.order_id = kwargs['order_id']
        self.isbn = kwargs['isbn']
        self.publisher = kwargs['publisher']
        self.school = kwargs['school']
        self.price = kwargs['price']
        self.duration = kwargs['duration']
        self.order_datetime = kwargs['order_datetime']


    def __repr__(self):
        return ','.join([self.order_id,
                         self.isbn,
                         self.publisher,
                         self.school,
                         self.price,
                         self.duration,
                         self.order_datetime])
