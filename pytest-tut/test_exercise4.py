# by Kami Bigdely
# Replace nested conditional with gaurd clauses

def extract_position(line):
    pos = None
    if not line:
        return None
    if 'x:' in line:
        start_index = line.find('x:') + 2
        pos = line[start_index:] # from start_index to the end.
  
    return pos

if __name__ == "__main__":
    result1 = extract_position('|error| numerical calculations could not converge.')
    print(result1)
    result2 = extract_position('|update| the positron location in the particle accelerator is x:21.432')
    print(result2)



def test_extract_position():
    assert extract_position("error") == None
    assert extract_position("debug") == None
    assert extract_position('|update| the positron location in the particle accelerator is x:21.432') == "21.432"
    assert extract_position('|update| the positron location in the particle accelerator is y:21.432') == None
