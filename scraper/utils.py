def GetPreviousSibling(element):
    if (element is None):
        return element

    sibling = element.previous_sibling
    if sibling == "\n":
        return GetPreviousSibling(sibling)
    else:
        return sibling

def GetNextSibling(element):
    if (element is None):
        return element

    sibling = element.next_sibling
    if sibling == "\n":
        return GetNextSibling(sibling)
    else:
        return sibling