def main(s,n):
    """
    The s string variable is given. return n characters from the end.
    Args:
        s(str): parameter
        n(int): parameter
    Returns:
        str: answer
    """
    a=len(s)
    return s[a-n:a]
s=str(input())
n=int(input())
print(main(s,n))
