from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        ana_hash = defaultdict(list)

        for item in strs:
            keys = "".join(sorted(item))
            ana_hash[keys].append(item)
            
        ret_list = []
        for val in ana_hash.values():
            ret_list.append(val)
        return ret_list
