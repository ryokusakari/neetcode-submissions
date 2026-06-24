class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        #iterate through and sort strings alphabetically
        for string in strs:
            #if there is an anagram, add to sublist
            sortstring = "".join(sorted(string))
            if sortstring in anagrams.keys():
                anagrams[sortstring].append(string)
            #if there have not been any anagrams, make new sublist
            else:
                anagrams[sortstring] = [string]
        #combine sublists into list
        return list(anagrams.values())


        