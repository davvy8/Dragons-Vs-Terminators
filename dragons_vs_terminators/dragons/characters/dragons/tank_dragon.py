from .bodyguard_dragon import BodyguardDragon


class TankDragon(BodyguardDragon):
    """TankDragon provides both offensive and defensive capabilities."""

    name = 'Tank'
    damage = 1
    # OVERRIDE CLASS ATTRIBUTES HERE
    food_cost = 6
    # BEGIN 3.3
    implemented = True  # Change to True to view in the GUI

    # END 3.3

    def action(self, colony):
        # BEGIN 3.3
        "*** YOUR CODE HERE ***"
        super().action(colony)
        left_terminators = []

        for t in self.place.terminators:
            t.armor -= self.damage
            if t.armor > 0:
                left_terminators.append(t)
            else:
                t.death_callback()
                
        self.place.terminators = left_terminators
