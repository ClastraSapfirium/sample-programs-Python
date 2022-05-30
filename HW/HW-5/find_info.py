from export_info import export_info
from print_info import print_info

def search_info(word, info):
    if len(info) > 0:
        for item in info:
            if word in item:
                return item
    else:
        return None