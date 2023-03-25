#ifndef SOLUTION_H
#define SOLUTION_H
#include <vector>

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target);
private:
    std::vector<int> indices;
};

#endif