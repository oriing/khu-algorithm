class Node:
    def __init__(self, key, pos):
        self.key = key
        self.link = None
        self.pos = pos

        
def get_digit(key: int, digit_pos: int) -> int:
    stkey = str(key)
    if len(stkey) < digit_pos:
        return 0
    return int(stkey[-digit_pos])

def distribute(masterlist: Optional[Node], digit_pos: int) -> List[Optional[Node]]:
    buckets = [None] * 10
    tails   = [None] * 10

    while masterlist:
        digit           = get_digit(masterlist.key, digit_pos)
        next_node       = masterlist.link
        masterlist.link = None

        if buckets[digit] is None:
            buckets[digit] = masterlist
            tails[digit]   = masterlist
        else:
            tails[digit].link = masterlist
            tails[digit]      = masterlist

        masterlist = next_node

    return buckets

def coalesce(list_array: List[Optional[Node]]) -> Optional[Node]:
    head = None
    tail = None

    for bucket in list_array:
        if bucket == None:
            continue

        if head == None:
            head = bucket
            tail = bucket
        else:
            tail.link = bucket
            
        while tail.link:
            tail = tail.link

    return head

def to_list(masterlist: Optional[Node]) -> List[int]:
    # Convert linked list to Python list
    result = []
    p = masterlist
    while p:
        result.append(p.key)
        p = p.link
    return result


def from_list(lst: List[int]) -> Optional[Node]:
    # Convert Python list to linked list
    head = None
    tail = None
    for idx in range(len(lst)):
        node = Node(lst[idx], idx)
        if head is None:
            head = tail = node
        else:
            tail.link = node
            tail = node
    return head

class Solution:

    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        # 오프라인쿼리 + Radix Sort
        answer = [-1] * len(queries)
        datas  = [int(i) for i in nums]

        masterlist = from_list(datas)
        numdigits  = len(str(max(datas)))

        for digit in range(1, numdigits + 1):
            list_array = distribute(masterlist, digit)
            masterlist = coalesce(list_array)
            for idx in range(len(queries)):
                if queries[idx][1] == digit:
                    ptr = masterlist
                    for _ in range(1, queries[idx][0]):
                        ptr = ptr.link
                    answer[idx] = ptr.pos

        return answer
