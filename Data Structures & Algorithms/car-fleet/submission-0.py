class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        fleets =0
    
        last_time =0
        for pos, spe in cars:
            t= (target-pos)/spe
            if t > last_time:      
                last_time=t
                fleets+=1
        return fleets
        