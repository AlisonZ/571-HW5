
import sys
import os
from TrainingModel import TrainingModel
from Token import Token

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
            # Do not add Meta data to the phrase 
            if line[0] != "#":
                # print(f"!***!!!!! {line}")
                token = Token()
                token.create_token(line.strip())
                phrase.append(token)
            if line == "\n":
                if phrase:
                    return phrase
        return phrase
    
def create_training_data(t):
    sequences = t.get_sequence()
    # create training tuple from the stack and add to t.set_training_data()
    for s in sequences:
        t.perform_transition(s)

def initialize_training_data(phrase, seq):
    t = TrainingModel()
    root = Token()
    root.create_token("0\tROOT\tROOT\tROOT\t_\t_\t0\troot\t_\t_")
    t.set_buffer(phrase)
    t.set_stack(root)
    t.set_sequence(seq)
    return t

def main():
    train_data, test_data, test_labels, train_seq, pred_seq = get_inputs()
    phrase, seq = get_phrase_and_seq(train_data, train_seq)
    # print(f"!!! {phrase}")
    t = initialize_training_data(phrase, seq)
    create_training_data(t)

if __name__ == '__main__':
    main()