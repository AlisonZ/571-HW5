class Token:
    def __init__(self):
        self.index = 0
        self.head_index = 0
        self.form = ''
        self.upos = ''
        self.xpos = ''
        self.lemma = ''
        self.features = 0
        self.dep_rel = ''
        self.deps = '', 
        self.misc = ''

    def set_index(self, i):
        self.index = i 
    
    def set_head_index(self, i):
        self.head_index = i
    
    def set_form(self, form):
        self.form = form
    
    def set_lemma(self, lemma):
        self.lemma = lemma
    
    def set_upos(self, upos):
        self.upos = upos

    def set_xpos(self, xpos):
        self.xpos = xpos
    
    def set_features(self, features):
        self.features = features

    def set_dep_rel(self, dep_rel):
        self.dep_rel = dep_rel
    
    def set_deps(self, deps):
        self.deps = deps
    
    def set_misc(self, misc):
        self.misc = misc

    def get_lemma(self):
        return self.lemma
    
    def get_form(self):
        return self.form
    
    def get_head_index(self):
        return self.head_index
    
    def get_index(self):
        return self.index
    
    def get_upos(self):
        return self.upos
    
    def get_xpos(self):
        return self.xpos    
    
    def get_features(self):
        return self.features
    
    def get_dep_rel(self):
        return self.dep_rel
    
    def get_deps(self):
        return self.deps

    def get_misc(self):
        return self.misc
        
    def create_token(self, token):
        split_token = token.split("\t")
        index = split_token[0]
        form = split_token[1]
        lemma = split_token[2]
        upos = split_token[3]
        xpos = split_token[4]
        features = split_token[5]
        head_index = split_token[6]
        dep_rel = split_token[7]
        deps = split_token[8]
        misc = split_token[9]

        self.set_index(index)
        self.set_form(form)
        self.set_lemma(lemma)
        self.set_upos(upos)
        self.set_xpos(xpos)
        self.set_features(features)
        self.set_head_index(head_index)
        self.set_dep_rel(dep_rel)
        self.set_deps(deps)
        self.set_misc(misc)
     

    def print_token(self):
        print("**************")
        print(f"INDEX {self.index}")
        print(f"HEAD {self.head_index}")
        print(f"WORD {self.word}")
        print(F"POS {self.pos}")
