# -*- coding: utf-8 -*-


class GraphClustering:
    def __init__(self, _dataframe, _threshold, _kernel):
        self.clusters = list()
        self.excludes = list()
        self.index = [data["index"] for data in _dataframe]
        self.data = [data["data"] for data in _dataframe]
        self.threshold = _threshold
        self.kernel = _kernel

    def test(self, content_x, content_y):
        measure = self.kernel(content_x, content_y)
        if measure > self.threshold:
            result = True
        else:
            result = False
        return result

    def find_derivative(self, current_index):
        data = self.data
        cluster = [self.index[current_index]]
        if current_index not in self.excludes:
            for i in range(current_index, (len(data)-1)):
                if (i+1) not in self.excludes:
                    if self.test(data[current_index], data[i+1]):
                        cluster.append(self.index[i+1])
                        self.excludes.append(i+1)
        return cluster

    def clustering(self):
        for i in range(len(self.index)-1):
            if i not in self.excludes:
                self.clusters.append(self.find_derivative(i))
                print("Derivative Clustering Ieration: " + str(i))
        return self.clusters
