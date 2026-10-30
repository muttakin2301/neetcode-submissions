class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        mapping = []
        fleet = len(position)

        for i in range(fleet):
            mapping.append((position[i], speed[i])) 

        mapping = sorted(mapping, key=lambda item:item[0])
        # print(mapping)

        ttrn = (target - mapping[fleet-1][0]) / mapping[fleet-1][1]

        for i in range(fleet - 2, -1, -1):
            ttrc = (target - mapping[i][0]) / mapping[i][1]

            # print(ttrc, ttrn)

            if ttrc <= ttrn:
                fleet -= 1
            else:
                ttrn = ttrc

        return fleet