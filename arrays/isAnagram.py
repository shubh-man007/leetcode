class Solution(object):
    def str_to_hash(self, x):
        x_set = set(x)
        str_dict = dict.fromkeys(x_set, 0)
        for i in x:
            str_dict[i] += 1
        return str_dict

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        s_dict = self.str_to_hash(s)
        t_dict = self.str_to_hash(t)

        if s_dict == t_dict:
            return True
        return False
        
