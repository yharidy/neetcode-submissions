# sorted dict
# from sortedcontainers import SortedDict
# class TimeMap:

#     def __init__(self):
#         self.store = defaultdict(SortedDict)
        

#     def set(self, key: str, value: str, timestamp: int) -> None:
#         self.store[key][timestamp] = value
        

#     def get(self, key: str, timestamp: int) -> str:
#         if key not in self.store:
#             return ""
#         timestamps = self.store[key]
#         idx = timestamps.bisect_right(timestamp)-1
#         if idx >=0:
#             closest_time = timestamps.iloc[idx]
#             return timestamps[closest_time]
#         return ""

class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store.setdefault(key,[]).append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key,[])

        l = 0
        r = len(values)-1
        while l<=r:
            m =(l+r)//2
            if values[m][0] <= timestamp:
                res = values[m][1]
                l=m+1
            else:
                r = m-1
        return res