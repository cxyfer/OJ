import sys
import json
sys.path.append("D:\\OneDrive\\Workplace\\OJ\\Leetcode\\en\\Python3")
sys.path.append("D:\\\\OneDrive\\\\Workplace\\\\OJ\\\\Leetcode")
a = __import__('2441_Largest Positive Integer That Exists With Its Negative')
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def serializeListNode(head:ListNode):
    if(head==None):
        return []
    node=head
    arr=[]
    while(node!=None):
        arr.append(str(node.val))
        node=node.next
    return '['+','.join(arr)+']'
def parseListNode(arr)->ListNode:
    header=ListNode()
    node=header
    for num in arr:
        node.next=ListNode(num)
        node=node.next
    return header.next

def serializeTreeNode(root:TreeNode):
    if(root==None):
        return []
    arr=[]
    queue=[root]
    while(len(queue)>0):
        node=queue.pop(0)
        if node!=None:
            arr.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        else:
            arr.append("null")
    i=len(arr)-1
    while(arr[i]=="null"):
        i=i-1
        arr.pop()
    return '['+','.join(arr)+']'
def parseTreeNode(arr)->TreeNode:
    if(len(arr)==0):
        return None
    val=arr.pop(0)
    root=TreeNode(val)
    queue=[root]
    while(queue):
        node=queue.pop(0)
        if len(arr)==0:
            return root
        leftVal=arr.pop(0)
        if leftVal!=None:
            left=TreeNode(leftVal)
            node.left=left
            queue.append(left)
        if len(arr)==0:
            return root
        rightVal=arr.pop(0)
        if  rightVal!=None:
            right=TreeNode(rightVal)
            node.right=right
            queue.append(right)
    return root
def parseTreeNodeArr(arr):
    out=[]
    for item in arr:
        treeNode=parseTreeNode(item)
        out.append(treeNode)
    return out
def serializeTreeNodeArr(arr):
    treeNodeStrArr=[]
    for item in arr:
        treeNodeStrArr.append(serializeTreeNode(item))
    return '['+','.join(treeNodeStrArr)+']'
def parseListNodeArr(arr):
    out=[]
    for item in arr:
        listNode=parseListNode(item)
        out.append(listNode)
    return out
def serializeListNodeArr(arr):
    listNodeStrArr=[]
    for item in arr:
        listNodeStrArr.append(serializeListNode(item))
    return '['+','.join(listNodeStrArr)+']'
def serializeFloat(param):
    r=str(param)
    arr=r.split(".")
    if len(arr)==1:
        return r+".00000"
    else:
        decimalStr=arr[1]+"00000"
        return arr[0]+"."+decimalStr[0:5]
       

arr=json.loads("[[[-1,2,-3,3]],[[-1,10,6,7,-7,1]],[[-10,8,6,7,-2,-3]]]")
for i in range(len(arr)):
    unitArgs=arr[i]
    s=a.Solution()
    arg0 = unitArgs[0]
    result=s.findMaxK(arg0)
    resultabc =json.dumps(result,separators=(',', ':'))
    print("resultabc"+str(i)+":"+resultabc+"resultend")