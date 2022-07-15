from constants import *
from game.scripting.action import Action


class DrawBallAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        ball = cast.get_all_actors(BALL_GROUP)
        for i in ball:
            body = i.get_body()

            if i.is_debug():
                rectangle = body.get_rectangle()
                self._video_service.draw_rectangle(rectangle, PURPLE)
            
            image = i.get_image()
            position = body.get_position()
            self._video_service.draw_image(image, position)