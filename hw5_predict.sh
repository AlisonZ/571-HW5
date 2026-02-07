#!/bin/bash
train_data=$1
test_data=$2
test_labels=$3 
train_seq=$4
pred_seq=$5

python3 hw5_oracle.py "$train_data" "$train_seq"

python3 hw5_train.py "$train_data" "$test_data" "$test_labels" "$train_seq" "$pred_seq"