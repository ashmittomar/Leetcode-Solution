class Solution(object):
    def merge(self, intervals):
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]

        for current in intervals[1:]:
            last = merged[-1]
            if current[0] <= last[1]:
                last[1] = max(last[1], current[1])
            else:
                merged.append(current)

        return merged

if __name__ == "__main__":
    input_str = input("Enter intervals as list of lists (e.g., [[1,3],[2,6],[8,10]]): ")
    
    try:
        intervals = eval(input_str)
        sol = Solution()
        result = sol.merge(intervals)
        print("Merged intervals:", result)
    except:
        print("Invalid input format. Please enter like [[1,3],[2,6],[8,10]].")
