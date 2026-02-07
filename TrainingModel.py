class TrainingModel:
    def __init__(self):
        self.buffer = []
        self.stack = []
        self.training_data = []

    def set_buffer(self, buffer_input):
        self.buffer = buffer_input

    def set_stack(self, stack_input):
        self.stack = stack_input

    def set_training_data(self, training_data):
        self.training_data = training_data
    
    def get_buffer(self):
        return self.buffer

    def get_stack(self):
        return self.stack
    
    def get_training_data(self):
        return self.training_data