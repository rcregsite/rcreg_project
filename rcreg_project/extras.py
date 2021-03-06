import string



def make_obj_dict(obj, attr_list):
    """Makes dict of obj, from list of items.
    Like model_to_dict, but limited to list."""
    
    pre_save_dict = {}
    for item in attr_list:
        attr = getattr(obj, item)
        pre_save_dict[item] = attr

    return pre_save_dict


def remove_punct(string_input):
    """Takes in string, removes punctuation, returns string sans punctuation"""
    # turn it into string just to be sure.
    # Inputing from Excel can make it think it's a number.
    punct_list = list(string.punctuation)
    string_list = []
    input_list = []

    # If is float, turn to int, str.
    # So import from Excel sheets won't have automatic decimal formatting.
    if isinstance(string_input, float):
        input_list = list(str(int(string_input)))
    else:  # fine for int and float, but not None or bools.
        # try to make a list of the string input, if it's unicode or a string
        input_list = list(str(string_input))

    for char in input_list:
        if char not in punct_list:
            string_list.append(char)
    new_string = "".join(string_list)

    return new_string


def ascii_only(string_input):
    """Takes in string, removes non-ascii chars, returns string."""

    try:  # in case is Bool or other troublemaker
        try:
            decoded_str = string_input.decode('ascii', errors='ignore')
            newstring_ascii = decoded_str.encode('ascii', errors='ignore')
        except:
            encoded_str = string_input.encode('ascii', errors='ignore')
            newstring_ascii = encoded_str.decode('ascii', errors='ignore')

        if (len(newstring_ascii) >= 1 and newstring_ascii != " "):
            return newstring_ascii
        else:
            return None
    except:
        return string_input


def ascii_only_no_punct(string_input):
    """Removes both non-ascii chars & punctuation, retuns new string"""
    step1 = ascii_only(string_input)
    step2 = remove_punct(step1)
    return step2
