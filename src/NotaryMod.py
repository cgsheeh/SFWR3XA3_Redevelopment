__author__ = 'connor'

class Notary:
    def __init__(self):
        self.t = []

    # Return all Notaries
    def get_all(self):
        return self.t

    # Return notary identified by notaryInfo
    def get(self, notaryInfo):
        return notaryInfo