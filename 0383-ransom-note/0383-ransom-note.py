class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote)<=len(magazine):
            for ch in ransomNote:
                if magazine.count(ch) < ransomNote.count(ch):
                    return False
            return True
        return False
