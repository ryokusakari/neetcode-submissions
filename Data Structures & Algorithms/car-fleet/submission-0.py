class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carvectors = []

        for pos, v in zip(position, speed):
            carvectors.append((pos, v))
        carvectors.sort() 

        carfleets = []

        while carvectors:
            vector = carvectors.pop()
            posB, vB = vector[0], vector[1]
            if not carfleets:
                carfleets.append((posB, vB))
            else:
                posA, vA = carfleets[-1][0], carfleets[-1][1]
                if  vA >= vB:
                    carfleets.append((posB, vB))
                elif (posA - posB)/(vB - vA) > (target - posA)/vA:
                    carfleets.append((posB, vB))
        
        return len(carfleets)

