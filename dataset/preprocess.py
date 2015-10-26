# -*- coding: utf-8 -*-

import random


def dataset_split(dataset, ratio):
    # split raw dataset into a training/verification pair based on a ratio

    def pro_type_a(_dataset, _ratio):
        n_samples = len(_dataset)
        n_training_samples = int(n_samples * _ratio)

        random.shuffle(_dataset)
        _training_samples = _dataset[:n_training_samples]
        _verification_samples = _dataset[n_training_samples:]
        return _training_samples, _verification_samples

    training_samples = None
    verification_samples = None

    if not 0 < ratio < 1:
        print("Ratio must be a position number larger than 1")
        raise Exception

    if type(dataset) == list:
        if type(dataset[0]) == str:
            training_samples, verification_samples = pro_type_a(dataset, ratio)

    return training_samples, verification_samples
