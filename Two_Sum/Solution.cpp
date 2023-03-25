#include <vector>
#include <iostream>
#include "Solution.h"

std::vector<int> Solution::twoSum(std::vector<int>& nums, int target) {
    int add = 0;
    for (int i = 0; i < nums.size(); ++i) {
        for (int j = 0; j < nums.size(); ++j) {
            if(nums[i] != nums[j]) {
                add = nums[i] + nums[j];
            }
            if(add == target) {
                indices.push_back(i);
                indices.push_back(j);
            }
        }
    }
    return indices;
}