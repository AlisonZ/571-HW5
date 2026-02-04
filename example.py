from nltk.classify.maxent import MaxentClassifier 
from sklearn.metrics import f1_score

# Train data is a list of tuples (Dict, str)
# Each training instance corresponds to one of these tuples
# The Dict consists of {feature:value} pairs
# The str corresponds to the correct label
train_data = [({'stack_1':'book', 'stack_1_POS': 'verb'}, '(LEFTARC,iobj)'),
              ({'stack_1':'flight', 'stack_1_POS': 'noun'}, 'SHIFT')]

# Test data is a list of Dicts
# Each test instance corresponds to a Dict of {feature:value} pairs
test_data = [{'stack_1':'hand', 'stack_1_POS':'verb'},
             {'stack_1':'book', 'stack_1_POS':'noun'}]

# Use the default parameters for the NLTK MaxEnt classifier
# NOTE: You can change these in your actual implementation.
classifier = MaxentClassifier.train(train_data, algorithm='GIS', max_iter=25, min_lldelta=0.001)

# Run the trained classifier on the test data
pred = [classifier.classify(x) for x in test_data]

# Suppose you have loaded in the gold test labels
test_gold = ['SHIFT', 'SHIFT']

# Get the micro-F1 score
# Can pass lists as args
micro_f1 = f1_score(test_gold, pred, average='micro') 

# Print 
report = "Micro F1: {0}".format(micro_f1)
print(report)


# Extra: If you want to use macro or weighted F1 score
macro_f1 = f1_score(test_gold, pred, average='macro')
weighted_f1 = f1_score(test_gold, pred, average='weighted')
extra_report = "Macro F1: {0}   Weighted F1: {1}".format(macro_f1, weighted_f1)
print(extra_report)
