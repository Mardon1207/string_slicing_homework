def main(s):
    """The s string variable is given. Return all characters except the one at the beginning and end.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    n=len(s)
    return s[1:n-1]
s=str(input())
print(main(s))