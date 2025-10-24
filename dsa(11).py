from heapq import heapify, heappush, heappop
heap = []

heapify(heap)
heappush(heap, 10)
heappush(heap, 30)
heappush(heap, 20)
heappush(heap, 400)
print("Head value of Min heap : "+str(heap[0]))
print("The Min heap elements : ")
for i in heap:
	print(i),
print("\n")
element = heappop(heap)
print("The heap elements after deleting head node : ")
for i in heap:
	print(i),

heap1 = []
heapify(heap1)
heappush(heap1, -1 * 10)
heappush(heap1, -1 * 30)
heappush(heap1, -1 * 20)
heappush(heap1, -1 * 400)
print("\nHead value of Max heap : " + str(-1 * heap1[0]))
print("The Max heap elements : ")
for i in heap1:
	print((-1*i)),
print("\n")
element = heappop(heap1)
print("The heap elements after deleting root node: ")
for i in heap1:
	print(-1 * i),

