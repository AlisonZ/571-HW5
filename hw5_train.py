
import sys
import os

def get_inputs():
    # TODO: handle incorrect number of inputs
    # TODO: delete existing output files
    if len(sys.argv) > 1:
        train_data = sys.argv[1]
        test_data = sys.argv[2]
        test_labels = sys.argv[3]
        train_seq = sys.argv[4]
        pred_seq = sys.argv[5]
    
    if os.path.exists(train_seq):
        os.remove(train_seq)

    if os.path.exists(pred_seq):
        os.remove(pred_seq)
    
    return train_data, test_data, test_labels, train_seq, pred_seq
    

def main():
    train_data, test_data, test_labels, train_seq, pred_seq = get_inputs()

if __name__ == '__main__':
    main()