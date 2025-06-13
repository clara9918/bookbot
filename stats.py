

def text_to_String(text):
    splits = text.split()
    return len(splits)

def count_char(text):
    count={}
    for tex in text:
        exist=0
        tex=tex.lower()
        if tex in count:
            exist=count[tex]+1
            count[tex]= exist
        else:
            count[tex]=1
    return count

def sort_on(dict):
    return dict["num"]


def chars_dict_to_sorted_list(chars_dict):
    sorted_list = []
    
    # Convert dictionary to list of dictionaries
    for char, count in chars_dict.items():
        sorted_list.append({"char": char, "num": count})
    
    # Sort from greatest to least
    sorted_list.sort(reverse=True, key=sort_on)
    
    return sorted_list