def is_same_class(obj, a_class):
    """
    Check if the object is exactly an instance of the specified class.

    Args:
        obj: The object to check.
        a_class: The specified class to compare with.

    Returns:
        True if obj is an instance of a_class, False otherwise.
    """
    if type(obj) == a_class:
        return True
    return False
