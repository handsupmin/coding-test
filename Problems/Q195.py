# Q195.py
# https://www.hackerrank.com/challenges/one-week-preparation-kit-merge-two-sorted-linked-lists/problem

def mergeLists(head1, head2):
    list1 = []
    now = head1
    while now:
        list1.append(now.data)
        now = now.next
        
    list2 = []
    now = head2
    while now:
        list2.append(now.data)
        now = now.next
    list3 = list1 + list2
    list3.sort()
    
    result = SinglyLinkedList()

    for i in range(len(list3)):
        result_item = int(list3[i])
        result.insert_node(result_item)
    
    return result.head