# This file is for strategy

from util.objects import *
from util.routines import *
from util.tools import find_hits
import time


class Bot(GoslingAgent):
    # This function runs every in-game tick (every time the game updates anything)
    def run(self):

        if self.intent is not None:
            self.debug_intent()
            white = self.renderer.white()
            text = "Debug Message"
            self.renderer.draw_string_2d(10, 100, 3, 3, text, white)
            return
        # d1 = abs(self.ball.location.y - self.foe_goal.location.y)
        # d2 = abs(self.me.location.y - self.foe_goal.location.y)
        # is_in_front_of_ball = d1 > d2
        if self.kickoff_flag:
            self.set_intent(kickoff())
            return
        # if is_in_front_of_ball:
        #     self.set_intent(goto(self.friend_goal.location))
        #     return
        # self.set_intent(short_shot(self.foe_goal.location))

        distBetBallFndgoal = (self.ball.location -
                              self.friend_goal.location).magnitude()

        targets = {
            'at_opponent_goal': (self.foe_goal.left_post, self.foe_goal.right_post),
            'away_from_our_net': (self.friend_goal.right_post, self.friend_goal.left_post)
        }
        hits = find_hits(self, targets)
        print(hits)
        if len(hits["at_opponent_goal"]) > 0:
            self.set_intent(hits['at_opponent_goal'][0])
            return
        elif (distBetBallFndgoal < 1000 or len(hits["away_from_our_net"]) <= 0):
            self.set_intent(hits['away_from_our_net'][0])
            return
        else:
            self.set_intent(goto(self.ball.location))
        # if self.me.boost > 70:
        #     self.set_intent(short_shot(self.foe_goal.location))
        #     return

        # Boost Logic
        # closest_boost = self.get_closest_large_boost()
        # lastBoostTime = 0
        # if closest_boost is not None and self.me.boost < 55 and (time.time()*1000)-lastBoostTime > 3000:

        #     lastBoostTime = time.time()*1000

        #     return
        # if len(available_boosts) > 0:
        #     self.set_intent(goto(available_boosts[0].location))
        #     return
