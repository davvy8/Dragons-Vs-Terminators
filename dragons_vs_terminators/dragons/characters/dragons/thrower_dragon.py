from .dragon import Dragon
from utils import random_or_none


class ThrowerDragon(Dragon):
    """ThrowerDragon throws a stone each turn at the nearest Terminator in its range."""

    name = 'Thrower'
    implemented = True
    damage = 1
    min_range = 0
    max_range = float('inf')

    # ADD/OVERRIDE CLASS ATTRIBUTES HERE
    food_cost = 3

    def nearest_terminator(self, skynet):
        """Return the nearest Terminator in a Place that is not the SKYNET, connected to
        the ThrowerDragon's Place by following entrances.

        This method returns None if there is no such Terminator (or none in range).
        """
        # BEGIN 1.3 and 2.1
        start_place = self.place
        start = self.min_range
        while start:
            start_place = start_place.entrance
            if start_place is skynet:
                start_place = None
                return None
            start -= 1

        end_place = self.place
        if self.max_range == float('inf'):
            end_place = skynet
        else:
            end = self.max_range + 1
            while end and end_place is not skynet:
                end_place = end_place.entrance
                end -= 1

        curr_place = start_place
        
        while curr_place is not end_place:
            if len(curr_place.terminators) != 0:
                return random_or_none(curr_place.terminators)
            else:
                curr_place = curr_place.entrance
        return None
        # END 1.3 and 2.1

    def throw_at(self, target):
        """Throw a stone at the TARGET Terminator, reducing its armor."""
        if target is not None:
            target.reduce_armor(self.damage)

    def action(self, colony):
        """Throw a stone at the nearest Terminator in range."""
        self.throw_at(self.nearest_terminator(colony.skynet))

