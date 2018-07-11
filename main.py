import unittest

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

    # print(chocolates)
    # print(children)

    cuts = 0

    # childpot = [[] for _ in range(len(children))]
    # print(childpot)

    #print(sum(chocolates))
    #print(sum(children))

    children.sort(reverse=True)
    # print(children)
    chocolates.sort(reverse=True)

    # for each child find the exact chocolate size they want
    #fullChildren = []
    for c in range(len(children)):
        for p in range(len(chocolates)):
            diff = getDiff(children[c], chocolates[p])
            if diff==0:
                # childpot[c].append(chocolates[p])
                chocolates.pop(p)
                #fullChildren.append(c)
                children[c]=0
                break

    
    # print(children)  
    children = list(filter(lambda a: a != 0, children))
    # print("Remove zeros")    
    # print(children)    
            #s = str(children[c]) + ' ' +  str(chocolates[p]) + ' ' + str(diff)
            #print(s)

    # print(childpot)
    # print(fullChildren)

    #for c in range(len(children)):
    c = 0
    while c < len(children):
        # if c in fullChildren:
        #     c=c+1
        #     continue
        
        # print(str(c))

        for p in range(len(chocolates)):
            diff = getDiff(children[c], chocolates[p])
            s = str(children[c]) + ' ' +  str(chocolates[p]) + ' ' + str(diff) + ' ' + str(cuts)
            #s = str(c) + ' ' +  str(chocolates[p]) + ' ' + str(diff)
            # print(s)

            if diff < 0:
                children[c] = children[c] - chocolates[p]
                chocolates.pop(p)
                chocolates.append(abs(diff))
                ##cuts = cuts + 1
                children.sort(reverse=True)
                break
            else:
                
                #children[c]=0
                children.pop(c)
                
                chocolates.pop(p)
                chocolates.append(abs(diff))
                
                if diff>0:
                    cuts = cuts + 1

                #c = c + 1
                break

    # print('Number of cuts: ' + str(cuts))
    # print('Chocolate left ' + str(sum(chocolates)))
    # print('Children left ' + str(sum(children)))
    # print(chocolates)

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

class TestScoreMethod(unittest.TestCase):
    """Class with the unit tests.
    """

    def test_given(self):
        chocolates = [2, 5, 7]
        children = [3, 2, 5, 1]
        cuts = giveChocolate(chocolates, children)
        self.assertEqual(cuts, 2)

    def test_exact(self):
        chocolates = [3, 2, 5, 1]
        children = [3, 2, 5, 1]
        cuts = giveChocolate(chocolates, children)
        self.assertEqual(cuts, 0)

    def test_extra_one(self):
        chocolates = [3, 2, 5, 2]
        children = [3, 2, 5, 1]
        cuts = giveChocolate(chocolates, children)
        self.assertEqual(cuts, 1)

    def test_extra_bigger_pieces(self):
        chocolates = [10, 8]
        children = [5, 6, 7]
        cuts = giveChocolate(chocolates, children)
        self.assertEqual(cuts, 2)
    
    def test_extra_smaller_pieces(self):
        chocolates = [3, 4, 4, 1, 2, 3, 1]
        children = [5, 6, 7]
        cuts = giveChocolate(chocolates, children)
        self.assertEqual(cuts, 0)   

if __name__ == '__main__':
    unittest.main()