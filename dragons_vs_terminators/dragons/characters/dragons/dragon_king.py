from .scuba_thrower import ScubaThrower
from utils import terminators_win


class DragonKing(ScubaThrower):  # You should change this line
    # END 4.3
    """The King of the colony. The game is over if a terminator enters his place."""

    name = 'King'
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 4.3
    food_cost = 7
    implemented = True  # Change to True to view in the GUI
    # END 4.3

    def __init__(self, armor=1):
        # BEGIN 4.3
        "*** YOUR CODE HERE ***"
        super().__init__(armor)
        if DragonKing.instantiated is False:
            DragonKing.instantiated = True
            self.instantiated = False
        # END 4.3

    def action(self, colony):
        """A dragon king throws a stone, but also doubles the damage of dragons
        in his tunnel.

        Impostor kings do only one thing: reduce their own armor to 0.
        """
        # BEGIN 4.3
        "*** YOUR CODE HERE ***"
        if self.instantiated:
            self.reduce_armor(self.armor)
        else:
            super().action(colony)
            p = self.place.exit
            while p is not None:
                if p.dragon is not None:
                    if p.dragon.is_container:
                        if not p.dragon.is_buffed:
                            p.dragon.damage *= 2
                            p.dragon.is_buffed = True
                        if p.dragon.contained_dragon is not None and not p.dragon.contained_dragon.is_buffed:
                            p.dragon.contained_dragon.damage *= 2
                            p.dragon.contained_dragon.is_buffed = True
                    elif not p.dragon.is_buffed:
                        p.dragon.damage *= 2
                        p.dragon.is_buffed = True
                p = p.exit
        # END 4.3

    def reduce_armor(self, amount):
        """Reduce armor by AMOUNT, and if the True DragonKing has no armor
        remaining, signal the end of the game.
        """
        # BEGIN 4.3
        "*** YOUR CODE HERE ***"
        check = self.instantiated
        super().reduce_armor(amount)
        if check is False and self.armor <= 0:
            terminators_win()

