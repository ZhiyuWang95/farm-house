"""
Problem: Design Parking System
Link: https://leetcode.com/problems/design-parking-system/
Pattern: OOD
Difficulty: Easy

Approach:
(write your approach/intuition here BEFORE coding)

Complexity:
Time: O(1)
Space: O(1)
"""

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.slot_map = {1: big, 2: medium, 3: small}
        

    def addCar(self, carType: int) -> bool:
        response = False

        if self.slot_map.get(carType, 0) > 0:
            available_slots = self.slot_map.get(carType)
            available_slots -= 1
            self.slot_map[carType] = available_slots
            response = True
        return response
                


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
ps = ParkingSystem(1, 1, 0)
print(ps.addCar(1))
print(ps.addCar(2))
print(ps.addCar(3))
print(ps.addCar(1))


# --- Notes / follow-ups discussed ---
#
# Your object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
