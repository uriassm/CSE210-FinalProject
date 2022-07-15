from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideBordersAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service    
        
    def execute(self, cast, script, callback):
        balls = cast.get_all_actors(BALL_GROUP)

        if len(balls) == 2:

            ball1 = balls[0]
            body1 = ball1.get_body()
            position1 = body1.get_position()
            x1 = position1.get_x()
            y1 = position1.get_y()
            bounce_sound = Sound(BOUNCE_SOUND)
            over_sound = Sound(OVER_SOUND)
            stats = cast.get_first_actor(STATS_GROUP)

            ball2 = balls[1]
            body2 = ball2.get_body()
            position2 = body2.get_position()
            x2 = position2.get_x()
            y2 = position2.get_y()
            bounce_sound = Sound(BOUNCE_SOUND)
            over_sound = Sound(OVER_SOUND)

            if x1 < FIELD_LEFT:
                ball1.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)
            
            elif x1 >= (FIELD_RIGHT - BALL_WIDTH):
                ball1.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            if y1 < FIELD_TOP:
                ball1.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            elif y1 >= (FIELD_BOTTOM - BALL_WIDTH):
                ball1.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)
                # stats = cast.get_first_actor(STATS_GROUP)
                # stats.lose_life()
                
                # if stats.get_lives() > 0:
                #     callback.on_next(TRY_AGAIN) 
                # else:
                #     callback.on_next(GAME_OVER)
                #     self._audio_service.play_sound(over_sound)

            if x2 < FIELD_LEFT:
                ball2.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)
                
            elif x2 >= (FIELD_RIGHT - BALL_WIDTH):
                ball2.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            if y2 < FIELD_TOP:
                ball2.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            elif y2 >= (FIELD_BOTTOM - BALL_WIDTH):
                ball2.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

        elif len(balls) == 3:
            ball1 = balls[0]
            body1 = ball1.get_body()
            position1 = body1.get_position()
            x1 = position1.get_x()
            y1 = position1.get_y()
            bounce_sound = Sound(BOUNCE_SOUND)
            over_sound = Sound(OVER_SOUND)
            stats = cast.get_first_actor(STATS_GROUP)

            ball2 = balls[1]
            body2 = ball2.get_body()
            position2 = body2.get_position()
            x2 = position2.get_x()
            y2 = position2.get_y()
            bounce_sound = Sound(BOUNCE_SOUND)
            over_sound = Sound(OVER_SOUND)
            
            ball3 = balls[2]
            body3 = ball3.get_body()
            position3 = body3.get_position()
            x3 = position3.get_x()
            y3 = position3.get_y()
            bounce_sound = Sound(BOUNCE_SOUND)
            over_sound = Sound(OVER_SOUND)       

            if x1 < FIELD_LEFT:
                ball1.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)
            
            elif x1 >= (FIELD_RIGHT - BALL_WIDTH):
                ball1.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            if y1 < FIELD_TOP:
                ball1.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            elif y1 >= (FIELD_BOTTOM - BALL_WIDTH):
                ball1.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)
                # stats = cast.get_first_actor(STATS_GROUP)
                # stats.lose_life()
                
                # if stats.get_lives() > 0:
                #     callback.on_next(TRY_AGAIN) 
                # else:
                #     callback.on_next(GAME_OVER)
                #     self._audio_service.play_sound(over_sound)

            if x2 < FIELD_LEFT:
                ball2.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)
                
            elif x2 >= (FIELD_RIGHT - BALL_WIDTH):
                ball2.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            if y2 < FIELD_TOP:
                ball2.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            elif y2 >= (FIELD_BOTTOM - BALL_WIDTH):
                ball2.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)


            if x3 < FIELD_LEFT:
                ball3.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)
            
            elif x3 >= (FIELD_RIGHT - BALL_WIDTH):
                ball3.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            if y3 < FIELD_TOP:
                ball3.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            elif y3 >= (FIELD_BOTTOM - BALL_WIDTH):
                ball3.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

        elif len(balls) == 4:
            ball1 = balls[0]
            body1 = ball1.get_body()
            position1 = body1.get_position()
            x1 = position1.get_x()
            y1 = position1.get_y()
            bounce_sound = Sound(BOUNCE_SOUND)
            over_sound = Sound(OVER_SOUND)
            stats = cast.get_first_actor(STATS_GROUP)

            ball2 = balls[1]
            body2 = ball2.get_body()
            position2 = body2.get_position()
            x2 = position2.get_x()
            y2 = position2.get_y()
            bounce_sound = Sound(BOUNCE_SOUND)
            over_sound = Sound(OVER_SOUND)
                    
            ball3 = balls[2]
            body3 = ball3.get_body()
            position3 = body3.get_position()
            x3 = position3.get_x()
            y3 = position3.get_y()
            bounce_sound = Sound(BOUNCE_SOUND)
            over_sound = Sound(OVER_SOUND)

            ball4 = balls[3]
            body4 = ball4.get_body()
            position4 = body4.get_position()
            x4 = position4.get_x()
            y4 = position4.get_y()
            bounce_sound = Sound(BOUNCE_SOUND)
            over_sound = Sound(OVER_SOUND)

            if x1 < FIELD_LEFT:
                ball1.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)
            
            elif x1 >= (FIELD_RIGHT - BALL_WIDTH):
                ball1.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            if y1 < FIELD_TOP:
                ball1.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            elif y1 >= (FIELD_BOTTOM - BALL_WIDTH):
                ball1.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)
                # stats = cast.get_first_actor(STATS_GROUP)
                # stats.lose_life()
                
                # if stats.get_lives() > 0:
                #     callback.on_next(TRY_AGAIN) 
                # else:
                #     callback.on_next(GAME_OVER)
                #     self._audio_service.play_sound(over_sound)

            if x2 < FIELD_LEFT:
                ball2.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)
                
            elif x2 >= (FIELD_RIGHT - BALL_WIDTH):
                ball2.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            if y2 < FIELD_TOP:
                ball2.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            elif y2 >= (FIELD_BOTTOM - BALL_WIDTH):
                ball2.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

                

            if x3 < FIELD_LEFT:
                ball3.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)
                
            elif x3 >= (FIELD_RIGHT - BALL_WIDTH):
                ball3.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            if y3 < FIELD_TOP:
                ball3.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            elif y3 >= (FIELD_BOTTOM - BALL_WIDTH):
                ball3.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)


            if x4 < FIELD_LEFT:
                ball4.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)
                
            elif x4 >= (FIELD_RIGHT - BALL_WIDTH):
                ball4.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            if y4 < FIELD_TOP:
                ball4.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            elif y4 >= (FIELD_BOTTOM - BALL_WIDTH):
                ball4.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

        elif len(balls) == 5:
            ball1 = balls[0]
            body1 = ball1.get_body()
            position1 = body1.get_position()
            x1 = position1.get_x()
            y1 = position1.get_y()
            bounce_sound = Sound(BOUNCE_SOUND)
            over_sound = Sound(OVER_SOUND)
            stats = cast.get_first_actor(STATS_GROUP)

            ball2 = balls[1]
            body2 = ball2.get_body()
            position2 = body2.get_position()
            x2 = position2.get_x()
            y2 = position2.get_y()
            bounce_sound = Sound(BOUNCE_SOUND)
            over_sound = Sound(OVER_SOUND)
                    
            ball3 = balls[2]
            body3 = ball3.get_body()
            position3 = body3.get_position()
            x3 = position3.get_x()
            y3 = position3.get_y()
            bounce_sound = Sound(BOUNCE_SOUND)
            over_sound = Sound(OVER_SOUND)

            ball4 = balls[3]
            body4 = ball4.get_body()
            position4 = body4.get_position()
            x4 = position4.get_x()
            y4 = position4.get_y()
            bounce_sound = Sound(BOUNCE_SOUND)
            over_sound = Sound(OVER_SOUND)
                    
            ball5 = balls[4]
            body5 = ball5.get_body()
            position5 = body5.get_position()
            x5 = position5.get_x()
            y5 = position5.get_y()
            bounce_sound = Sound(BOUNCE_SOUND)
            over_sound = Sound(OVER_SOUND)

            if x1 < FIELD_LEFT:
                ball1.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)
            
            elif x1 >= (FIELD_RIGHT - BALL_WIDTH):
                ball1.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            if y1 < FIELD_TOP:
                ball1.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            elif y1 >= (FIELD_BOTTOM - BALL_WIDTH):
                ball1.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)
                # stats = cast.get_first_actor(STATS_GROUP)
                # stats.lose_life()
                
                # if stats.get_lives() > 0:
                #     callback.on_next(TRY_AGAIN) 
                # else:
                #     callback.on_next(GAME_OVER)
                #     self._audio_service.play_sound(over_sound)

            if x2 < FIELD_LEFT:
                ball2.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)
                
            elif x2 >= (FIELD_RIGHT - BALL_WIDTH):
                ball2.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            if y2 < FIELD_TOP:
                ball2.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            elif y2 >= (FIELD_BOTTOM - BALL_WIDTH):
                ball2.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

                

            if x3 < FIELD_LEFT:
                ball3.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)
                
            elif x3 >= (FIELD_RIGHT - BALL_WIDTH):
                ball3.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            if y3 < FIELD_TOP:
                ball3.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            elif y3 >= (FIELD_BOTTOM - BALL_WIDTH):
                ball3.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)


            if x4 < FIELD_LEFT:
                ball4.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)
                
            elif x4 >= (FIELD_RIGHT - BALL_WIDTH):
                ball4.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            if y4 < FIELD_TOP:
                ball4.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            elif y4 >= (FIELD_BOTTOM - BALL_WIDTH):
                ball4.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)


            if x5 < FIELD_LEFT:
                ball5.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)
                
            elif x5 >= (FIELD_RIGHT - BALL_WIDTH):
                ball5.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            if y5 < FIELD_TOP:
                ball5.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            elif y5 >= (FIELD_BOTTOM - BALL_WIDTH):
                ball5.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

        elif len(balls) == 6:
            ball1 = balls[0]
            body1 = ball1.get_body()
            position1 = body1.get_position()
            x1 = position1.get_x()
            y1 = position1.get_y()
            bounce_sound = Sound(BOUNCE_SOUND)
            over_sound = Sound(OVER_SOUND)
            stats = cast.get_first_actor(STATS_GROUP)

            ball2 = balls[1]
            body2 = ball2.get_body()
            position2 = body2.get_position()
            x2 = position2.get_x()
            y2 = position2.get_y()
            bounce_sound = Sound(BOUNCE_SOUND)
            over_sound = Sound(OVER_SOUND)
                    
            ball3 = balls[2]
            body3 = ball3.get_body()
            position3 = body3.get_position()
            x3 = position3.get_x()
            y3 = position3.get_y()
            bounce_sound = Sound(BOUNCE_SOUND)
            over_sound = Sound(OVER_SOUND)

            ball4 = balls[3]
            body4 = ball4.get_body()
            position4 = body4.get_position()
            x4 = position4.get_x()
            y4 = position4.get_y()
            bounce_sound = Sound(BOUNCE_SOUND)
            over_sound = Sound(OVER_SOUND)
                    
            ball5 = balls[4]
            body5 = ball5.get_body()
            position5 = body5.get_position()
            x5 = position5.get_x()
            y5 = position5.get_y()
            bounce_sound = Sound(BOUNCE_SOUND)
            over_sound = Sound(OVER_SOUND)

            ball6 = balls[5]
            body6 = ball6.get_body()
            position6 = body6.get_position()
            x6 = position6.get_x()
            y6 = position6.get_y()
            bounce_sound = Sound(BOUNCE_SOUND)
            over_sound = Sound(OVER_SOUND)

            if x1 < FIELD_LEFT:
                ball1.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)
            
            elif x1 >= (FIELD_RIGHT - BALL_WIDTH):
                ball1.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            if y1 < FIELD_TOP:
                ball1.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            elif y1 >= (FIELD_BOTTOM - BALL_WIDTH):
                ball1.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)
                # stats = cast.get_first_actor(STATS_GROUP)
                # stats.lose_life()
                
                # if stats.get_lives() > 0:
                #     callback.on_next(TRY_AGAIN) 
                # else:
                #     callback.on_next(GAME_OVER)
                #     self._audio_service.play_sound(over_sound)

            if x2 < FIELD_LEFT:
                ball2.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)
                
            elif x2 >= (FIELD_RIGHT - BALL_WIDTH):
                ball2.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            if y2 < FIELD_TOP:
                ball2.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            elif y2 >= (FIELD_BOTTOM - BALL_WIDTH):
                ball2.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

                

            if x3 < FIELD_LEFT:
                ball3.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)
                
            elif x3 >= (FIELD_RIGHT - BALL_WIDTH):
                ball3.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            if y3 < FIELD_TOP:
                ball3.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            elif y3 >= (FIELD_BOTTOM - BALL_WIDTH):
                ball3.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)


            if x4 < FIELD_LEFT:
                ball4.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)
                
            elif x4 >= (FIELD_RIGHT - BALL_WIDTH):
                ball4.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            if y4 < FIELD_TOP:
                ball4.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            elif y4 >= (FIELD_BOTTOM - BALL_WIDTH):
                ball4.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)


            if x5 < FIELD_LEFT:
                ball5.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)
                
            elif x5 >= (FIELD_RIGHT - BALL_WIDTH):
                ball5.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            if y5 < FIELD_TOP:
                ball5.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            elif y5 >= (FIELD_BOTTOM - BALL_WIDTH):
                ball5.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)


            if x6 < FIELD_LEFT:
                ball6.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)
                
            elif x6 >= (FIELD_RIGHT - BALL_WIDTH):
                ball6.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            if y6 < FIELD_TOP:
                ball6.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            elif y6 >= (FIELD_BOTTOM - BALL_WIDTH):
                ball6.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

        elif len(balls) == 7:
            ball1 = balls[0]
            body1 = ball1.get_body()
            position1 = body1.get_position()
            x1 = position1.get_x()
            y1 = position1.get_y()
            bounce_sound = Sound(BOUNCE_SOUND)
            over_sound = Sound(OVER_SOUND)
            stats = cast.get_first_actor(STATS_GROUP)

            ball2 = balls[1]
            body2 = ball2.get_body()
            position2 = body2.get_position()
            x2 = position2.get_x()
            y2 = position2.get_y()
            bounce_sound = Sound(BOUNCE_SOUND)
            over_sound = Sound(OVER_SOUND)
                    
            ball3 = balls[2]
            body3 = ball3.get_body()
            position3 = body3.get_position()
            x3 = position3.get_x()
            y3 = position3.get_y()
            bounce_sound = Sound(BOUNCE_SOUND)
            over_sound = Sound(OVER_SOUND)

            ball4 = balls[3]
            body4 = ball4.get_body()
            position4 = body4.get_position()
            x4 = position4.get_x()
            y4 = position4.get_y()
            bounce_sound = Sound(BOUNCE_SOUND)
            over_sound = Sound(OVER_SOUND)
                    
            ball5 = balls[4]
            body5 = ball5.get_body()
            position5 = body5.get_position()
            x5 = position5.get_x()
            y5 = position5.get_y()
            bounce_sound = Sound(BOUNCE_SOUND)
            over_sound = Sound(OVER_SOUND)

            ball6 = balls[5]
            body6 = ball6.get_body()
            position6 = body6.get_position()
            x6 = position6.get_x()
            y6 = position6.get_y()
            bounce_sound = Sound(BOUNCE_SOUND)
            over_sound = Sound(OVER_SOUND)
                    
            ball7 = balls[6]
            body7 = ball7.get_body()
            position7 = body7.get_position()
            x7 = position7.get_x()
            y7 = position7.get_y()
            bounce_sound = Sound(BOUNCE_SOUND)
            over_sound = Sound(OVER_SOUND)

            if x1 < FIELD_LEFT:
                ball1.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)
            
            elif x1 >= (FIELD_RIGHT - BALL_WIDTH):
                ball1.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            if y1 < FIELD_TOP:
                ball1.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            elif y1 >= (FIELD_BOTTOM - BALL_WIDTH):
                ball1.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)
                # stats = cast.get_first_actor(STATS_GROUP)
                # stats.lose_life()
                
                # if stats.get_lives() > 0:
                #     callback.on_next(TRY_AGAIN) 
                # else:
                #     callback.on_next(GAME_OVER)
                #     self._audio_service.play_sound(over_sound)

            if x2 < FIELD_LEFT:
                ball2.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)
                
            elif x2 >= (FIELD_RIGHT - BALL_WIDTH):
                ball2.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            if y2 < FIELD_TOP:
                ball2.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            elif y2 >= (FIELD_BOTTOM - BALL_WIDTH):
                ball2.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

                

            if x3 < FIELD_LEFT:
                ball3.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)
                
            elif x3 >= (FIELD_RIGHT - BALL_WIDTH):
                ball3.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            if y3 < FIELD_TOP:
                ball3.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            elif y3 >= (FIELD_BOTTOM - BALL_WIDTH):
                ball3.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)


            if x4 < FIELD_LEFT:
                ball4.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)
                
            elif x4 >= (FIELD_RIGHT - BALL_WIDTH):
                ball4.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            if y4 < FIELD_TOP:
                ball4.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            elif y4 >= (FIELD_BOTTOM - BALL_WIDTH):
                ball4.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)


            if x5 < FIELD_LEFT:
                ball5.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)
                
            elif x5 >= (FIELD_RIGHT - BALL_WIDTH):
                ball5.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            if y5 < FIELD_TOP:
                ball5.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            elif y5 >= (FIELD_BOTTOM - BALL_WIDTH):
                ball5.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)


            if x6 < FIELD_LEFT:
                ball6.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)
                
            elif x6 >= (FIELD_RIGHT - BALL_WIDTH):
                ball6.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            if y6 < FIELD_TOP:
                ball6.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            elif y6 >= (FIELD_BOTTOM - BALL_WIDTH):
                ball6.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)


            if x7 < FIELD_LEFT:
                ball7.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)
                
            elif x7 >= (FIELD_RIGHT - BALL_WIDTH):
                ball7.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            if y7 < FIELD_TOP:
                ball7.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            elif y7 >= (FIELD_BOTTOM - BALL_WIDTH):
                ball7.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

        elif len(balls) == 8:
            ball1 = balls[0]
            body1 = ball1.get_body()
            position1 = body1.get_position()
            x1 = position1.get_x()
            y1 = position1.get_y()
            bounce_sound = Sound(BOUNCE_SOUND)
            over_sound = Sound(OVER_SOUND)
            stats = cast.get_first_actor(STATS_GROUP)

            ball2 = balls[1]
            body2 = ball2.get_body()
            position2 = body2.get_position()
            x2 = position2.get_x()
            y2 = position2.get_y()
            bounce_sound = Sound(BOUNCE_SOUND)
            over_sound = Sound(OVER_SOUND)
                    
            ball3 = balls[2]
            body3 = ball3.get_body()
            position3 = body3.get_position()
            x3 = position3.get_x()
            y3 = position3.get_y()
            bounce_sound = Sound(BOUNCE_SOUND)
            over_sound = Sound(OVER_SOUND)

            ball4 = balls[3]
            body4 = ball4.get_body()
            position4 = body4.get_position()
            x4 = position4.get_x()
            y4 = position4.get_y()
            bounce_sound = Sound(BOUNCE_SOUND)
            over_sound = Sound(OVER_SOUND)
                    
            ball5 = balls[4]
            body5 = ball5.get_body()
            position5 = body5.get_position()
            x5 = position5.get_x()
            y5 = position5.get_y()
            bounce_sound = Sound(BOUNCE_SOUND)
            over_sound = Sound(OVER_SOUND)

            ball6 = balls[5]
            body6 = ball6.get_body()
            position6 = body6.get_position()
            x6 = position6.get_x()
            y6 = position6.get_y()
            bounce_sound = Sound(BOUNCE_SOUND)
            over_sound = Sound(OVER_SOUND)
                    
            ball7 = balls[6]
            body7 = ball7.get_body()
            position7 = body7.get_position()
            x7 = position7.get_x()
            y7 = position7.get_y()
            bounce_sound = Sound(BOUNCE_SOUND)
            over_sound = Sound(OVER_SOUND)

            ball8 = balls[7]
            body8 = ball8.get_body()
            position8 = body8.get_position()
            x8 = position8.get_x()
            y8 = position8.get_y()
            bounce_sound = Sound(BOUNCE_SOUND)
            over_sound = Sound(OVER_SOUND)
                    
            if x1 < FIELD_LEFT:
                ball1.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)
                
            elif x1 >= (FIELD_RIGHT - BALL_WIDTH):
                ball1.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            if y1 < FIELD_TOP:
                ball1.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            elif y1 >= (FIELD_BOTTOM - BALL_WIDTH):
                ball1.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)
                # stats = cast.get_first_actor(STATS_GROUP)
                # stats.lose_life()
                
                # if stats.get_lives() > 0:
                #     callback.on_next(TRY_AGAIN) 
                # else:
                #     callback.on_next(GAME_OVER)
                #     self._audio_service.play_sound(over_sound)

            if x2 < FIELD_LEFT:
                ball2.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)
                
            elif x2 >= (FIELD_RIGHT - BALL_WIDTH):
                ball2.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            if y2 < FIELD_TOP:
                ball2.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            elif y2 >= (FIELD_BOTTOM - BALL_WIDTH):
                ball2.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

                

            if x3 < FIELD_LEFT:
                ball3.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)
                
            elif x3 >= (FIELD_RIGHT - BALL_WIDTH):
                ball3.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            if y3 < FIELD_TOP:
                ball3.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            elif y3 >= (FIELD_BOTTOM - BALL_WIDTH):
                ball3.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)


            if x4 < FIELD_LEFT:
                ball4.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)
                
            elif x4 >= (FIELD_RIGHT - BALL_WIDTH):
                ball4.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            if y4 < FIELD_TOP:
                ball4.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            elif y4 >= (FIELD_BOTTOM - BALL_WIDTH):
                ball4.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)


            if x5 < FIELD_LEFT:
                ball5.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)
                
            elif x5 >= (FIELD_RIGHT - BALL_WIDTH):
                ball5.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            if y5 < FIELD_TOP:
                ball5.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            elif y5 >= (FIELD_BOTTOM - BALL_WIDTH):
                ball5.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)


            if x6 < FIELD_LEFT:
                ball6.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)
                
            elif x6 >= (FIELD_RIGHT - BALL_WIDTH):
                ball6.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            if y6 < FIELD_TOP:
                ball6.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            elif y6 >= (FIELD_BOTTOM - BALL_WIDTH):
                ball6.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)


            if x7 < FIELD_LEFT:
                ball7.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)
                
            elif x7 >= (FIELD_RIGHT - BALL_WIDTH):
                ball7.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            if y7 < FIELD_TOP:
                ball7.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            elif y7 >= (FIELD_BOTTOM - BALL_WIDTH):
                ball7.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)


            if x8 < FIELD_LEFT:
                ball8.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)
                
            elif x8 >= (FIELD_RIGHT - BALL_WIDTH):
                ball8.bounce_x()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            if y8 < FIELD_TOP:
                ball8.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

            elif y8 >= (FIELD_BOTTOM - BALL_WIDTH):
                ball8.bounce_y()
                self._audio_service.play_sound(bounce_sound)
                stats.add_points(10)

