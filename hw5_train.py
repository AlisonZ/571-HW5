
import sys
import os
from TrainingModel import TrainingModel

def get_inputs():
    if len(sys.argv) > 1:
        train_data = sys.argv[1]
        test_data = sys.argv[2]
        test_labels = sys.argv[3]
        train_seq = sys.argv[4]
        pred_seq = sys.argv[5]

    if os.path.exists(pred_seq):
        os.remove(pred_seq)
    
    return train_data, test_data, test_labels, train_seq, pred_seq

def get_phrase_and_seq(train_data, train_seq):
    phrase = get_phrase(train_data)
    seq = get_seq(train_seq)

    return phrase, seq

def get_seq(train_seq):
    with open(train_seq, 'r', encoding='utf8') as seq_file:
        lines = seq_file.readlines()
        seq = []
        for line in lines:
            seq.append(line.strip())
            if line == "\n":
                if seq:
                    return seq
        return seq

def get_phrase(train_data):
    with open(train_data, 'r', encoding='utf8') as file:
        lines = file.readlines()
        phrase = []
        for line in lines:
            phrase.append(line.strip())
            if line == "\n":
                if phrase:
                    return phrase
        return phrase

def create_training_data(phrase, test_labels):

    t = TrainingModel()

def main():
    train_data, test_data, test_labels, train_seq, pred_seq = get_inputs()
    phrase, seq = get_phrase_and_seq(train_data, train_seq)
    print(f"!!! {phrase}")
    create_training_data(phrase, train_seq)

if __name__ == '__main__':
    main()