def filter_query(value, data):
    return filter(lambda x: value in x, data)

def map_query(value, data):
    column_num = int(value)
    return map(lambda x: data.split()[column_num], data)

def unique_query(data):
    return set(data)

def sort_query(value, data):
    reverse = value == "desc"
    return sorted(data, reverse=reverse)

def limit_query(value, data):
    limit=int(value)
    return list(data)[:limit]
