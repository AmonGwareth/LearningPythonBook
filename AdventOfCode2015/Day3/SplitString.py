

def split_data(data_string: str) -> [str, str]:
    """Returns a Generator of Generators for the separated list."""
    return ["".join(entry for idx, entry in enumerate(data_string) if idx % 2 == 0), "".join(entry for idx, entry in enumerate(data_string) if idx % 2 == 1)]




