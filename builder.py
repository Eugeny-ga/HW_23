from functions import filter_query, map_query, unique_query, sort_query, limit_query

cmd_to_functions = {
    'filter': filter_query,
    'map': map_query,
    'unique': unique_query,
    'sort': sort_query,
    'limit': limit_query,
}


def read_file(file_name):
    with open(file_name) as file:
        for line in file:
            yield line

def build_query(cmd, value, file_name, data):
    if data is None:
        prepared_data = read_file(file_name)
    else:
        prepared_data = data

    function = cmd_to_functions[cmd]
    return list(function(value=value, data=prepared_data))


