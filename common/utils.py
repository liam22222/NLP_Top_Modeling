import re

def wrap_exception(e: Exception, error_message: str) -> str:
    rw = str(e).replace('\n', '\n\t')
    return f"{error_message}, caused by:\n\t{e.__class__.__name__}: {rw}"


def format_str(variable) -> str:
    """ Formats string to be fitted as Postgresql query"""
    return str(variable) if isinstance(variable, int) or isinstance(variable, float) else f"'{variable}'"

def remove_items_from_string(string : str , list_key_to_remove : list)-> str:
    for word in list_key_to_remove:
        string = string.replace(word, "")
    return string

def remove_double_spaces_from_string(text : str)-> str:
   return re.sub('\s{2,}', ' ', text)
  

