class Arc:
    def __init__(self):
        self.head_index = 0
        self.index = 0
        self.dep_relation = ''
        self.form = ''
    
    def set_head_index(self, index):
        self.head_index = index
    
    def set_index(self, index):
        self.index = index

    def set_dep_relation(self, relation):
        self.dep_relation = relation

    def set_form(self, form):
        self.form = form
    
    def get_dep_relation(self):
        return self.dep_relation
    
    def get_head_index(self):
        return self.head_index
    
    def get_index(self):
        return self.index
    
    def get_form(self):
        return self.form
    