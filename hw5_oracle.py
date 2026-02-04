
import sys
import os
from Oracle import Oracle
from Token import Token
from ArcModel import Arc
TRANSITIONS = {
    'shift': "SHIFT",
    'leftArc': "LEFTARC",
    'rightArc': "RIGHTARC"
}
def get_inputs():
    if len(sys.argv) > 1:
        parse_input = sys.argv[1]
        sequence_output = sys.argv[2]

    if os.path.exists(sequence_output):
        os.remove(sequence_output)
    
    return parse_input, sequence_output

def get_transition(right_token, left_token, buffer):
    r_head = right_token.get_head_index()
    r_index = right_token.get_index()
    r_dep_rel = right_token.get_dep_rel()
    l_head = left_token.get_head_index()
    l_index = left_token.get_index()
    l_dep_rel = left_token.get_dep_rel()

    if r_head == l_index:
        has_dependents_in_buffer = any(
            token.get_head_index() == r_index for token in buffer
        )
        if not has_dependents_in_buffer:
            return (TRANSITIONS['rightArc'], r_dep_rel)

    if l_head == r_index:
        has_dependents_in_buffer = any(
            token.get_head_index() == l_index for token in buffer
        )
        if not has_dependents_in_buffer:
            return (TRANSITIONS['leftArc'], l_dep_rel)

    return (TRANSITIONS['shift'])

def print_sequence(o, sequence_output):
    transitions = o.get_transitions()
    with open(sequence_output, "a") as f:
        for transition in transitions:
            if isinstance(transition, tuple):
                print(f"({transition[0]}, {transition[1]})", file=f)
            else:
                print(transition, file=f)
        print('', file=f)

def create_transitions(o, sequence_output):
    is_terminal_case = o.is_terminal_case()
    if is_terminal_case:
        o.add_transition((TRANSITIONS['rightArc'], 'root'))
        print_sequence(o, sequence_output)
        return 
    while not is_terminal_case:
        stack = o.get_stack()
        if len(stack) > 1:
            right, left = o.view_top_two()
            buffer = o.get_buffer()
            transition = get_transition(right_token=right, left_token=left, buffer=buffer)

            if transition[0] == TRANSITIONS['rightArc']:
                o.add_transition(transition)
                o.add_to_stack(left)
            if transition[0] == TRANSITIONS['leftArc']:
                o.add_transition(transition)
                o.add_to_stack(right)
            if transition == TRANSITIONS['shift']:
                if len(o.get_buffer()) > 0:
                    o.add_to_stack(left)
                    o.add_to_stack(right)
                    o.add_transition(transition)
                    o.shift()
                else:
                    break
            is_terminal_case = o.is_terminal_case()
        else:
            is_terminal_case = o.is_terminal_case()
            if is_terminal_case:
                o.add_transition((TRANSITIONS['rightArc'], 'root'))
                print_sequence(o, sequence_output)
                return
            else:
                o.shift()
                o.add_transition(transition=TRANSITIONS['shift'])

    o.add_transition((TRANSITIONS['rightArc'], 'root'))
    print_sequence(o, sequence_output)

def create_oracle(parsed_phrase, sequence_output):
    o = Oracle()
    o.set_input_phrase(phrase=parsed_phrase)
    lines = []
   
    for line in parsed_phrase:
        if line[0] == '#':
            o.set_meta_data(line)
        else:
            t = Token()
            t.create_token(line.strip())
            lines.append(t)
    
    if not lines:
        return
    
    root_token = lines.pop(0)
    o.add_to_stack(root_token)
    o.set_buffer(lines)
    o.add_transition(transition=TRANSITIONS['shift'])
    create_transitions(o, sequence_output)

def read_dependency_parses(parse_input, sequence_output):
    with open(parse_input, 'r', encoding='utf8') as file:
        lines = file.readlines()
        parsed_phrase = []
        for line in lines:   
            if line == "\n":
                if parsed_phrase:
                    create_oracle(parsed_phrase, sequence_output)
                parsed_phrase = []
            else:
                parsed_phrase.append(line)
        
        create_oracle(parsed_phrase, sequence_output)
      

def main():
    parse_input,  sequence_output = get_inputs()
    read_dependency_parses(parse_input, sequence_output)

if __name__ == '__main__':
    main()