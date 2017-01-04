import xml.etree.ElementTree as etree

def getTags(rootXml):
    A = {}
    for child in root.iter():
        A[child.tag] = child.attrib
    return A

n = int(input())
L = [input() for i in range(n)]
xml = ''.join(L)
tree = etree.ElementTree(etree.fromstring(xml))
root = tree.getroot()

count = 0
N = getTags(root)
for i in N:
    count+=len(N[i])

print(count)
