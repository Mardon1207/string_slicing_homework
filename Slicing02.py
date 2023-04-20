def main(s):
    """
    The s string variable is given. return four characters from the end.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    s=s+"b"
    return s[-5:-1]
s=str(input())
print(main(s))