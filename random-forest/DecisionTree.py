import numpy as np
import math
import random

from collections import Counter, defaultdict


class DecisionTree:

 
    def __init__(self, attributes, labels):
       self.node_gain_ratio: float = 0.0
       self.node_information_ratio: float = 0.0
       self.is_leaf: bool = False
       self.majority_class: int = 0
       self.best_attr: int = 0
       self.children = defaultdict(DecisionTree) 
       self.parent: DecisionTree = None

       self.build_tree(attributes, labels)

    def build_tree(self, attributes: np.array, labels: np.array):
        num_instances = len(labels)

        if num_instances == 0:
            self.is_leaf = True
            return

        node_information = num_instances * self.compute_entropy(labels = labels)
        self.majority_class = self.most_frequent(labels)


        best_attr = None
        best_info_gain = -np.inf
        best_gain_ratio = -np.inf

        for X in range(attributes.shape[1]):
            conditional_info = 0
            attribute_entropy = 0

            attr_count = defaultdict(int)

            rel_attr = attributes[:, X]
            for Y in np.unique(rel_attr):
                ids = self.segregate(rel_attr, Y)
                attr_count[Y] = len(ids)
                conditional_info += attr_count[Y] * self.compute_entropy(labels = labels[ids])

            attr_information_gain = node_information - conditional_info

            attr_count_entropy = self.compute_entropy(None, label_counts = attr_count)
            gain_ratio = attr_information_gain / attr_count_entropy if attr_count_entropy != 0 else 0

            if gain_ratio > best_gain_ratio:
                best_information_gain = attr_information_gain
                best_gain_ratio = gain_ratio
                best_attr = X

        if best_gain_ratio == 0:
            self.is_leaf = True
            return

        self.best_attr = best_attr
        self.node_gain_ratio = best_gain_ratio
            
        for Y in iter(attr_count.keys()):
            ids = self.segregate(attributes[:,best_attr], Y)
            child = DecisionTree(attributes[ids], labels[ids])
            child.parent = self
            self.children[Y] = child
                
        return

    def evaluate(self, test_attr):
        if self.is_leaf:
            return self.majority_class
        else:
            return self.children[test_attr[self.best_attr]].evaluate(test_attr)

        
    #---------- Helpers from here down -------------#

        # likely can refactor to gain better performance
        # and avoid repeat calculations.

    def segregate(self, attr_arr: np.ndarray, value: int):
        return [i for i in range(len(attr_arr)) if attr_arr[i] == value]

    def compute_entropy(self, labels: np.ndarray = None, label_counts:dict = None):

        # either dict is already pre-computed or not
        if label_counts:
            total = sum(v for v in label_counts.values())
        else:
            label_counts = Counter(labels)
            total = len(labels)
        entropy = 0.0

        
        for count in label_counts.values():
            p = count / total
            if p > 0:
                entropy -= p * np.log(p)
        return entropy

    def most_frequent(self, labels: np.ndarray):
        label_count = Counter(labels)
        return max(label_count, key=label_count.get)

attributes = np.array([['boy'], ['girl'], ['boy'], ['girl']])
labels = np.array([1,2,1,2])

tree = DecisionTree(attributes, labels)
