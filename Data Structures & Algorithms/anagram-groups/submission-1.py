class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Iterate through list 
        #Order items and see if they match existing anagram
        #If existing, add to dictionary 
        #Convert dictionary items to list of sublists

        anagrams = {}
        for s in strs:
            ss = str(sorted(s))
            if ss in anagrams:
                anagrams[ss].append(s)
            else:
                anagrams[ss] = [s]
        return list(anagrams.values())

        