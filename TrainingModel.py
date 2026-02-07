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
    
    def create_transition(self, left, right, transition):
        if transition == TRANSITIONS['SHIFT']:
            features = {'stack_0': left.get_lemma(), 'stack_0_POS': left.get_upos()}
            data = (features, transition)
            self.training_data.append(data)
        else:
            features = {'stack_0': left.get_lemma(), 'stack_0_POS': left.get_upos(), 'stack_1': right.get_lemma(), 'stack_1_POS': right.get_upos()}
            data = (features, transition)
            self.training_data.append(data)
    
    def shift(self):
        top_item = self.buffer.pop()
        self.create_transition(left=top_item, right='', transition=TRANSITIONS['SHIFT'])
        self.stack.append(top_item)

    def leftarc(self):
        left = self.stack.pop()
        right = self.stack.pop()
        self.create_transition(left, right, TRANSITIONS['LEFTARC'])
        self.stack.append(right)

    def rightarc(self):
        left = self.stack.pop()
        right = self.stack.pop()
        self.create_transition(left, right, TRANSITIONS['RIGHTARC'])
        self.stack.append(left)
    
    def perform_transition(self, transition):
        if not isinstance(transition, tuple):
            self.shift()
        else:
            if transition[0] == TRANSITIONS['LEFTARC']:
                self.leftarc()
            elif transition[0] == TRANSITIONS['RIGHTARC']:
                self.rightarc()
                