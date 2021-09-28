class Node:
  def __init__(self, value = None, next = None, left = None, right = None):
    self.next = next
    self.value = value
    self.left = left
    self.right = right

class LinkedList:

  def __init__(self):
    self.head = None


  def add(self, value):
    node = Node(value)

    if self.head is None:
      self.head = node
      return

    current = self.head
    while current.next is not None:
      current = current.next

    current.next = node

ll = LinkedList()

ll.add(7)
ll.add(2)
ll.add(13)
ll.add(9)
ll.add(3)
ll.add(14)

def iterate_linked_list_recursively(input_node, largest = 0):
    if input_node is None:
        return largest
    
    if input_node.value > largest:
        largest = input_node.value
        
    return iterate_linked_list_recursively(input_node.next, largest)

print(iterate_linked_list_recursively(ll.head))