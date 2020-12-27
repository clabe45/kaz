import fnmatch

def search(items, pattern):
    filtered_keys = fnmatch.filter(items, pattern)
    return { key: items[key] for key in filtered_keys }
