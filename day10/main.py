# Function with outputs
def format_name(f_name, l_name):
    """ 
    Take a first and last name and format it to
    return the title case version of the name.
    """
    return f'{f_name} {l_name}'.title()


my_name = format_name('pAulo', 'tEiXeira')
print(my_name)
