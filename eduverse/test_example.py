
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next



class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        # deal with edge cases
        # heapify the list : O(NLogN)
        for i in range(1, len(lists)):
            parent = int((i + 1) // 2) - 1
            while lists[i].val > lists[parent].val:
                lists[i].val, lists[parent].val = lists[parent].val, lists[i].val
                i = parent
                parent = int((i + 1) // 2) - 1
        for i in lists:
            print('/n')
            j = i
            while j:
                print(f"{j.val} ->")
                j = j.next
        # get the smallest element and update the first linked list
        head = ListNode(0)
        pointer = head
        counter = len(lists)
        while counter > 0:

            pointer.next = lists[0]
            pointer = pointer.next
            lists[0] = lists[0].next
            if lists[0] == None:
                counter -= 1
            # call the function that rearranges the heap : O(LogN)
            self.arrange(lists)

            print("next iteration")
            for i in lists:
                print('/n')
                j = i
                while j:
                    print(f"{j.val} ->")
                    j = j.next
        return head.next

    # haep rule : if a parent has 2 children and only one of them is a None : then the right child has to be None

    def arrange(self, list: list[ListNode | None]) -> None:

        parent = 0
        # check if the first element of the list is None or not
        if list[parent] != None:

            # start traversing through the list : this does not check the case where the the parent only has 1 child
            while len(list) > 2 * parent + 2:
                child = parent
                # if left child is None both are none
                if list[2 * parent + 1] == None:
                    break
                # left child is not none ; make the swap
                if list[2 * parent + 1].val < list[parent].val:
                    list[parent], list[2 * parent + 1] = list[2 * parent + 1], list[parent]
                    child = 2 * parent + 1
                # only right child is none; change parent to the left child and continue to next iteration
                if list[2 * parent + 2] == None:
                    parent = child
                    continue
                # neither are none and check if right child swap is needed
                elif list[2 * parent + 2].val < list[parent].val:
                    list[parent], list[2 * parent + 2] = list[2 * parent + 2], list[parent]
                    child = 2 * parent + 2
                if child == parent:
                    break
                parent = child
            # edge case if the parent only has left child
            if 2 * parent + 2 == len(list):
                child = 2 * parent + 1
                if list[child] != None:
                    if list[child].val < list[parent].val:
                        list[child], list[parent] = list[parent], list[child]

        # first element is None

        else:
            while len(list) > 2 * parent + 2:
                child = parent
                # if left child is None both are none
                if list[2 * parent + 1] == None:
                    break
                # only right child is none
                elif list[2 * parent + 2] == None:
                    list[2 * parent + 1], list[parent] = list[parent], list[2 * parent + 1]
                    break
                # neither are none and check if right child swap is needed
                else:
                    left = list[2 * parent + 1]
                    if left.val < list[2 * parent + 2].val:
                        list[2 * parent + 1] = list[2 * parent + 2]
                        list[parent] = left
                    else:
                        list[parent] = list[2 * parent + 2]
                    list[2 * parent + 2] = None
                    child = 2 * parent + 2

                if child == parent:
                    break
                parent = child
            # edge case if the parent only has left child
            if 2 * parent + 2 == len(list):
                child = 2 * parent + 1
                if list[child] != None:
                    list[child], list[parent] = list[parent], list[child]


def main():
    a = ListNode(1)
    a.next = ListNode(4)
    a.next.next = ListNode(5)
    a.next.next = ListNode(5)
    b = ListNode(2)
    b.next = ListNode(6)
    c = ListNode(1)
    c.next = ListNode(3)
    c.next.next = ListNode(4)
    l = [a, b, c]
    obj = Solution()
    link = obj.mergeKLists(l)
    while link != None:
        print(f"{link.val} -->")
        link = link.next

if __name__ == '__main__':
    main()

