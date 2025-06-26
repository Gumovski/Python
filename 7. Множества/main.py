nums1 = {1, 2, 3, 4, 5, 6}
nums2 = {5, 6, 7, 8, 9}
print(nums1.union(nums2))
print(nums1 | nums2)

print(nums2.difference(nums1))
print(nums2 - nums1)

print(nums1.intersection(nums2))
print(nums1 & nums2)

print(nums1.symmetric_difference(nums2))
print(nums1 ^ nums2)

