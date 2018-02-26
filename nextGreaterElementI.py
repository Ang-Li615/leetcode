
def nextGreaterElement(nums1, nums2):
    L = []
    for n1 in nums1:
        print(n1)
        exist = 0
        i = nums2.index(n1)
        print(i)
        if i+1 >= len(nums2):
            L.append(-1)
        else:
            for j in range(i+1,len(nums2)):
                print([j,nums2[j]])
                if nums2[j] > n1:
                    print('yay')
                    L.append(nums2[j])
                    exist = 1
                    break
            if exist == 0:
                L.append(-1)
        print(L)
    return L

nums1 = [4,1,2]
nums2 = [1,3,4,2]
L = nextGreaterElement(nums1,nums2)
print(L)