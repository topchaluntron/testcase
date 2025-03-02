def alternate(s):
    unique_chars = set(s)
    max_len = 0

    for char1 in unique_chars:
        for char2 in unique_chars:
            if char1 == char2:
                continue

            filtered_s = ""
            for char in s:
                if char == char1 or char == char2:
                    filtered_s += char

            is_alternating = True
            if len(filtered_s) > 1:
                for i in range(len(filtered_s) - 1):
                    if filtered_s[i] == filtered_s[i + 1]:
                        is_alternating = False
                        break
            
            if is_alternating:
                max_len = max(max_len, len(filtered_s))
    return max_len