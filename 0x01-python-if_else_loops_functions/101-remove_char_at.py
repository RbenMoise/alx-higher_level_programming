#!/usr/bin/python3
def remove_char_at(s, n):
    if n < 0 or n >= len(s):
        # If n is out of bounds, return the original string
        return s

    # Create a new string by slicing the original string
    # from the beginning up to the character before n,
    # and concatenate it with the part after n.
    return s[:n] + s[n+1:]
