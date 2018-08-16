from collections import namedtuple


class DatasetMeta(namedtuple('DatasetMeta', ['dataset', 'num_classes', 'shape'])):
    @property
    def size(self):
        '''int: Number of examples in the dataset'''
        return self.shape[0]
