METADATA_TAGS = {
    'NEW_DOC': 'newdoc', 
    'SENT_ID': "sent_id", 
    'ORIG_TEXT': 'text', 
    'EN_TEXT':'text_en'
}

class Oracle:
    def __init__(self):
        self.buffer = []
        self.stack = []
        self.transitions = []
        self.input_phrase = '', 
        self.doc_id = '', 
        self.sent_id = '', 
        self.orig_text = '', 
        self.eng_text = ''

    def set_buffer(self, buffer_input):
        self.buffer = buffer_input

    def set_input_phrase(self, phrase):
        self.input_phrase = phrase
    
    def set_doc_id(self, id):
        self.doc_id = id

    def set_sent_id(self, id):
        self.sent_id = id
    
    def set_orig_text(self, text):
        self.orig_text = text

    def set_eng_text(self, text):
        self.eng_text = text
    
    def get_buffer(self):
        return self.buffer
    
    def get_input_phrase(self):
        return self.input_phrase
    
    def get_stack(self):
        return self.stack
    
    def get_transitions(self):
        return self.transitions
    
    def is_terminal_case(self):
        buffer_len = len(self.buffer)
        stack_len = len(self.stack)
        transition_len = len(self.transitions)
        
        if buffer_len == 0 and stack_len == 1 and transition_len != 0:
            return True
        else:
            return False
    
    def add_transition(self, transition):
        self.transitions.append(transition)

    def add_to_stack(self, token):
        self.stack.append(token)
    
    def shift(self):
        shifted_el = self.buffer.pop(0)
        self.stack.append(shifted_el)

    def view_top_two(self):
        right = self.stack.pop()
        left = self.stack.pop()
        return right, left
    
    def print_buffer(self):
        print(f"BUFFFFFF: {self.buffer}")

    def print_stack(self):
        print(f"STACK!!!! {self.stack}")

    def set_meta_data(self, input):
        meta_split = input.split(" ")
        meta_type = meta_split[1]
        if meta_type == METADATA_TAGS['NEW_DOC']:
            doc_id = meta_split[-1]
            self.set_doc_id(doc_id)
        elif meta_type == METADATA_TAGS['SENT_ID']:
            sent_id = meta_split[-1]
            self.set_sent_id(sent_id)
        elif meta_type == METADATA_TAGS['ORIG_TEXT']:
            orig_text = meta_split[3:]
            self.set_orig_text(orig_text)
        elif meta_type == METADATA_TAGS['EN_TEXT']:
            eng_text = meta_split[3:]
            self.set_eng_text(eng_text)