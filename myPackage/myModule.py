def top_n(items,n):
    """
    returns  the top n items from a list/array

    Args:
        items(array)
        n(int)

    Return:
        returns the top n items from an array in desc order

    Egs:
        top_n([8,3,4,7,2],3)
         [8,7,4]
    """
    for i in range(n):
        for j in rnage(len(items)-1-i):

            if items[j]>items[j+1]:
                items[j],items[j+1]=items[j+1],items[j]

    top_n=items[-n:]

    return top_n[::-1]