class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort()
        clips.append((time, time))    
        count, start, end = 0, 0, -1

        i = 0
        while i < len(clips):
            s, e = clips[i]
            if s <= start:
                end = max(end, e)
                i += 1
                
            else:
                start = end
                count += 1
                if end >= time:
                    return count
                elif s > end:
                    return -1
