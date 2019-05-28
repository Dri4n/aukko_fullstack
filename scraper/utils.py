def GetPreviousSibling(element):
    sibling = element.previous_sibling
    if sibling == "\n":
        return GetPreviousSibling(sibling)
    else:
        return sibling

def GetNextSibling(element):
    sibling = element.next_sibling
    if sibling == "\n":
        return GetNextSibling(sibling)
    else:
        return sibling