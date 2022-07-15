from constants import *
from game.scripting.action import Action


class CheckOverAction(Action):

    def __init__(self):
        self._milestone1 = 100
        self._milestone2 = 400
        self._milestone3 = 1000
        self._milestone4 = 2000
        self._milestone5 = 4000
        self._milestone6 = 6000
        self._milestone7 = 8000
        self._milestone_list = [self._milestone1, self._milestone2, self._milestone3, self._milestone4, self._milestone5, self._milestone6, self._milestone7]
        self._next_milestone = 0

        
    def execute(self, cast, script, callback):
        bricks = cast.get_actors(BRICK_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)
        if stats.get_score() == self._milestone_list[self._next_milestone]:
            stats.next_level()
            callback.on_next(NEXT_LEVEL)
            self._next_milestone += 1