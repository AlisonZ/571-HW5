import re
TRANSITIONS = {
    'SHIFT': 'SHIFT', 
    'LEFTARC': 'LEFTARC', 
    'RIGHTARC': 'RIGHTARC'
}

class TrainingModel:
    def __init__(self):
        self.buffer = []
        self.stack = []
        self.sequence = []
        self.training_data = []

    def set_buffer(self, buffer_input):
        self.buffer = buffer_input

    def set_stack(self, stack_input):
        self.stack = [stack_input]
    
    def add_to_stack(self, item):
        self.stack.append(item)

    def set_training_data(self, training_data):
        self.training_data = training_data
    
    def set_sequence(self, seq):
        for s in seq:
            regex = r"[\(\)]"
            clean_str = re.sub(regex, "", s)
            split_seq = clean_str.split(',')
            if len(split_seq) == 1:
                self.sequence.append(clean_str)
            else:
              tup = tuple(split_seq)
              self.sequence.append(tup)

    def get_buffer(self):
        return self.buffer

    def get_stack(self):
        return self.stack
    
    def get_training_data(self):
        return self.training_data
    
    def get_sequence(self):
        return self.sequence
    
    def extract_features(self):
        features = {}
        if len(self.stack) >=1:
            stack_0 = self.stack[-1]
            features['stack_0'] = stack_0.get_lemma()
            features['stack_0_POS'] = stack_0.get_upos()

        if len(self.stack) >=2:
            stack_1 = self.stack[-2]
            features['stack_1'] = stack_1.get_lemma()
            features['stack_1_POS'] = stack_1.get_upos()

        return features
    
    def shift(self):
        top_item = self.buffer.pop(0)
        self.stack.append(top_item)

    def leftarc(self):
        left = self.stack.pop()
        right = self.stack.pop()
        self.stack.append(right)

    def rightarc(self):
        left = self.stack.pop()
        right = self.stack.pop()
        self.stack.append(left)
    
    def perform_transition(self, transition):
        if not isinstance(transition, tuple):
            self.shift()
        else:
            if transition[0] == TRANSITIONS['LEFTARC']:
                self.leftarc()
            elif transition[0] == TRANSITIONS['RIGHTARC']:
                self.rightarc()
                
            else:
                print("ERROR: unknown transition")