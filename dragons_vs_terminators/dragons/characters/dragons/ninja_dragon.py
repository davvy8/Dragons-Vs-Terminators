from .dragon import Dragon


class NinjaDragon(Dragon):
    """NinjaDragon does not block the path and damages all terminators in its place."""

    name = 'Ninja'
    damage = 1
    # OVERRIDE CLASS ATTRIBUTES HERE
    food_cost = 5
    blocks_path = False
    # BEGIN 2.4
    implemented = True  # Change to True to view in the GUI

    # END 2.4

    def action(self, colony):
        # BEGIN 2.4
        "*** YOUR CODE HERE ***"
        left_terminators = []

        for t in self.place.terminators:
            t.armor -= self.damage
            if t.armor > 0:
                left_terminators.append(t)
            else:
                t.death_callback()

        self.place.terminators = left_terminators
