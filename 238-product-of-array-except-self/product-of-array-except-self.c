#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* productExceptSelf(int* nums, int numsSize, int* returnSize) {
    *returnSize = numsSize;
    int* out = (int*)malloc(numsSize * sizeof(int));
    int leftProduct = 1, rightProduct = 1;

    for (int i = 0; i < numsSize; i++) {
        out[i] = leftProduct;
        leftProduct *= nums[i];
    }

    for (int i = numsSize - 1; i >= 0; i--) {
        out[i] *= rightProduct;
        rightProduct *= nums[i];
    }
    return out;
}
