def count_char_occurrences(text):
    from collections import defaultdict
    counts = defaultdict(int)
    for char in text.lower():
        if char.isalpha():
            counts[char] += 1
    return dict(counts)

def merge_dicts(dict1, dict2, conflict_resolver):
    merged = dict1.copy()
    for key, value in dict2.items():
        if key in merged:
            merged[key] = conflict_resolver(key, merged[key], value)
        else:
            merged[key] = value
    return merged

def invert_dictionary(original_dict):
    inverted = {}
    for key, value in original_dict.items():
        inverted.setdefault(value, []).append(key)
    return inverted

def dict_to_table(data_dict, columns):
    if not data_dict or not columns:
        return ""
    
    headers = [col.upper() for col in columns]
    rows = []
    for item in data_dict.values():
        row = [str(item.get(col, "N/A")) for col in columns]
        rows.append(row)
    
    col_widths = [
        max(len(headers[i]), max(len(row[i]) for row in rows))
        for i in range(len(columns))
    ]
    
    separator = "+" + "+".join("-" * (w + 2) for w in col_widths) + "+\n"
    header_line = "| " + " | ".join(
        headers[i].ljust(col_widths[i]) for i in range(len(headers))
    ) + " |\n"
    
    table = separator + header_line + separator
    for row in rows:
        row_line = "| " + " | ".join(
            row[i].ljust(col_widths[i]) for i in range(len(row))
        ) + " |\n"
        table += row_line
    table += separator
    
    return table

def deep_update(base_dict, update_dict):
    result = base_dict.copy()
    for key, value in update_dict.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_update(result[key], value)
        else:
            result[key] = value
    return result