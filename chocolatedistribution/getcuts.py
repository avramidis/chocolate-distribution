def giveChocolate(chocolates, children):
    """Calculates the number times given chocolate bars have to be cut to give the requested
    pieces to each child.
    Args:
        chocolates: A list with the pieces of each chocolate bar.
        children: A list with the chocolate pieces each child wants.
    Returns:
        An integer value (>=0) with the number of cuts for the precise distribution of chocolates 
        to children. Return -1 if the checks to the inputs fail.
    """

    if (sum(children)) > (sum(chocolates)):
        print("No enough chocolates to please all children!")
        return -1

    if len(list(filter(lambda a: a < 0, chocolates)))>0:
        print("Error in chocolates input - negative values!")
        return -1
    
    if len(list(filter(lambda a: a < 0, children)))>0:
        print("Error in childer input - negative values!")
        return -1

    children.sort(reverse=True)
    chocolates.sort(reverse=True)

    # for each child find the exact chocolate size they want
    for c in range(len(children)):
        for p in range(len(chocolates)):
            diff = getDiff(children[c], chocolates[p])
            if diff==0:
                chocolates.pop(p)
                children[c]=0
                break

    children = list(filter(lambda a: a != 0, children))

    cuts = 0
    while 0 < len(children):

        for p in range(len(chocolates)):
            diff = getDiff(children[0], chocolates[p])

            if diff < 0:
                children[0] = children[0] - chocolates[p]
                chocolates.pop(p)
                chocolates.append(abs(diff))
                children.sort(reverse=True)
                break
            else:
    
                children.pop(0)
                
                chocolates.pop(p)
                chocolates.append(abs(diff))
                
                if diff>0:
                    cuts = cuts + 1

                break
    return cuts

def getDiff(child, bar):
    """Calculates the difference in pieces of a chocolate bar to 
    the requested pieces by a child.
    Args:
        child: An integer with pieces requested.
        bar: An integer with the number of chocolate pieces.
    Returns:
        An integer value with the difference of the requested pieces
        and the given bar size.
    """
    return  bar - child