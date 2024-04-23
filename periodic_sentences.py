from elements_set import elements_len1, elements_len2
import copy

all_element_combos = []
elements = []

def str_elements(str_check: str) -> None:
    '''
    A recursive function that saves all possible combinations of elements to all_element_combos.
    '''
    global all_element_combos
    global elements
    if str_check[0].upper() in elements_len1:
        elements.append(str_check[0].upper())
        if len(str_check) == 1:
            all_element_combos.append(copy.deepcopy(elements))
        else:
            str_elements(str_check[1:])
        elements.pop()
    
    if len(str_check) >= 1:
        if str_check[:2].capitalize() in elements_len2:
            elements.append(str_check[:2].capitalize())
            if len(str_check) == 2:
                all_element_combos.append(elements)
            else:
                str_elements(str_check[2:])
            elements.pop()

str_elements('')
print(all_element_combos)