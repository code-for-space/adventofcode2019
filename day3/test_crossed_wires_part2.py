from crossed_wires import FuelManagementSystem
import pytest


class Test1:
    @pytest.fixture
    def fms(self):
        return FuelManagementSystem("R8,U5,L5,D3", "U7,R6,D4,L4")

    def test_steps_combined_min(self, fms):
        assert fms.steps_combined_min() == 30


class Test2:
    @pytest.fixture
    def fms(self):
        return FuelManagementSystem(
            "R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83"
        )

    def test_steps_combined_min(self, fms):
        assert fms.steps_combined_min() == 610


class Test3:
    @pytest.fixture
    def fms(self):
        return FuelManagementSystem(
            "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
            "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7",
        )

    def test_steps_combined_min(self, fms):
        assert fms.steps_combined_min() == 410
