#!/usr/bin/env python
"""
```
class AllOBJ:
   pass
```
"""
# ------------------------------------------------------------------------------------------------------------
# from typing import Any, Dict, List, Literal, Optional, Set, Tuple, Union
import random as rdm
import pygame as pym

from space_OBJ_ import (
    # pym,  // default
    SpacialOBJ,
)
# from app_overview_0.simple_pygame_training.space_OBJ_ import SpacialOBJ

# pym.init()

class TryPygame():
    """
    **All games process: the Pygame file (main) in some cases**\n
    ***All needed methods are defined here***\n
    *The fileSystem in some cases, so, for*\n
    **Ex.:**
    ```
    from pyio import TryPygame
    ```
    ```
    from tryGame_ import TryPygame
    trypyg = TryPygame()
    trypyg.run_game()
    ```
    """
    pym.init()  # initialize first
    
    # WINDOW TITLE
    screen_header = pym.display.set_caption(title="Pygame Try n°N Oh !!!", icontitle='07')
    # WINDOW SCREEN
    screen = pym.display.set_mode(size=(621, 621), depth=0)
    # SYSTEM FONT
    font = pym.font.Font(None, size=14)
    # COLOR
    rgb_da_limit = bin_col_lim = 255
    rc_, gc_, bc_, tc_ = 0, 0, 0, 1
    color_ = (rc_, gc_, bc_, 0.9)

    # GRAVITY
    GRAVITY = 9.81  # m/s²
    # TIME
    dt = 0
    t0 = pym.time.get_ticks()
    # delay = pym.time.delay(30000)    # 3000

    clock = pym.time.Clock()    # FOR FPS -> File Per Second

    # IMPORTING OBJECTS
    # 0 -> Static Objects (Not Moving)
    staticObj_ = SpacialOBJ()
    # 1 -> Aleatoire's Moving Objects
    dynamicObj_ = SpacialOBJ(
        surface_=screen,
        targetPosition="CENTER",
        position_OBJc_=pym.Vector2(screen.get_width() / 2, screen.get_height() / 2),
        dt_=dt, v_=50, a_=1,
    )
    # 2 -> Case of Grig
    stepMovObj_ = SpacialOBJ(
        surface_=screen,
        position_OBJc_=pym.Vector2( pym.mouse.get_pos() ),
        dt_=dt, v_=25, a_=2,
    )
    # 3 -> self.Animated Objects
    # __init_ballz__()
    """BALLZ_ = [] # |-> randomObj_
    MIN_BALLZ, MAX_BALLZ = 17, 216
    MIN_SPEED, MAX_SPEED = 21, 74
    for b_ in range( rdm.randint(0, MAX_BALLZ) ):
        BALLZ_.append(
            SpacialOBJ(
                surface_=screen,
                position_OBJc_=pym.Vector2( rdm.uniform(0, screen.get_width()/2), rdm.uniform(0, screen.get_height()/2) ),
                dt_=dt, v_=rdm.uniform(MIN_SPEED, MAX_SPEED),
            )
        )"""
    
    running = True  # MAIN LOOP ->
    switched_obj = True
    llprintObjAct_ = True   # Interactive informations when on Switcing
    
    def __init__(self, ):
        """```def __initialize__(self, running: bool, ):
            self.running = running
            #
        ```"""
        ...
        
    # __initialize__()
    
    def runMainLoop(self, ):
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        while self.running:
            for event in pym.event.get():
                if event.type == pym.QUIT:
                    self.running = False
                elif event.type == pym.KEYDOWN:
                    if event.key == pym.K_ESCAPE:
                        self.running = False
            #
            
            #if self.rgbdv < 255 or self.rgbdv >= 0:
                #self.rgbdv += 4
            #else: self.rgbdv = 0
            # fill the screen with a color to wipe away anything from last frame
            self.screen.fill(color=(self.rc_, self.gc_, self.bc_, 0.8))
            
            # RENDER YOUR GAME HERE
            # -----------------------------------------
            # PERSONALIZED COLORS  ---------------------------------------->
            binCLim = self.rgb_da_limit
            cr_, cg_, cb_ = 0, 0, 0
            # TEXT OF WELCOME ---------------------------------------->
            "Goudy Old Style"
            #
            # "OBJECTS" : -> {
            # ---------------------------------------->
            # STATICS ------->
            grid_n = 5
            for j in range(grid_n):
                for i in range(grid_n):
                    self.staticObj_._draw_(
                        geo_OBJ="RECT",
                        surface_=self.screen,
                        color_=(binCLim/(1+i+j), binCLim/(1+i+j), binCLim/(1+i+j), 0.7),
                        rect_left_top_width_height=(
                            self.screen.get_width() * (i / grid_n),
                            self.screen.get_height() * (j / grid_n),
                            self.screen.get_width() / grid_n,
                            self.screen.get_height() / grid_n
                        )
                    )
            # grid APPROPRIATED ---->
            #
            # DYNAMICS ------->
            self.dynamicObj_._draw_(
                geo_OBJ="CIRCLE",
                surface_=self.screen,
                #
            )
            self.dynamicObj_._move_(
                geo_OBJ="CIRCLE",
                targertPos="UP",
                deltaTime=self.dt
            )   # initial aleatory move
            self.stepMovObj_._draw_(
                geo_OBJ="CIRCLE",
                surface_=self.screen,
            )
            # BALLZ_ = []
            """for b_, ball_ in enumerate(self.BALLZ_):
                ball_._draw_(
                    geo_OBJ="CIRCLE",
                    color_="white",
                    radius_=7,
                )"""
            # }
            # GAME (SYS) EVENT  ---------------------------------------->
            # "ON_KEY_%" : -> { ------->
            switch_keys = pym.key.get_pressed()
            if switch_keys[pym.K_s]:
                self.switched_obj = not(self.switched_obj)
                self.llprintObjAct_ = not(self.llprintObjAct_)
            #
            if self.switched_obj:
                if self.llprintObjAct_:
                    print("Obj. n is now still moving")
                    self.llprintObjAct_ = not(self.llprintObjAct_)
                #
                # "ON_KEY_PRESS"
                keys = pym.key.get_pressed()
                if keys[pym.K_UP]:
                    self.dynamicObj_._move_(
                        geo_OBJ="CIRCLE",
                        targertPos="UP",
                        deltaTime=self.dt
                    )
                    # player_pos.y -= 300 * dt
                if keys[pym.K_DOWN]:
                    self.dynamicObj_._move_(
                        geo_OBJ="CIRCLE",
                        targertPos="DOWN",
                        deltaTime=self.dt
                    )
                    # player_pos.y += 300 * dt
                if keys[pym.K_LEFT]:
                    self.dynamicObj_._move_(
                        geo_OBJ="CIRCLE",
                        targertPos="LEFT",
                        deltaTime=self.dt
                    )
                    # player_pos.x -= 300 * dt
                if keys[pym.K_RIGHT]:
                    self.dynamicObj_._move_(
                        geo_OBJ="CIRCLE",
                        targertPos="RIGHT",
                        deltaTime=self.dt
                    )
                    # player_pos.x += 300 * dt
            else:
                """if self.llprintObjAct_:
                    print("Obj. 2 is now still moving")
                    self.llprintObjAct_ = not(self.llprintObjAct_)"""
                ...
            # }
            # "ON_MOUSE_%" : { ------->
            touch = pym.mouse.get_pressed() # touch = pym.mouse.get_focused() # touch = pym.mouse.get_pressed()
            if touch:
                self.dynamicObj_._draw_(
                    geo_OBJ="CIRCLE",
                    surface_=self.screen,
                    color_="gray",
                    position_OBJc_=pym.Vector2( pym.mouse.get_pos() ),
                    radius_=6
                )
            # MOUSE EVENT ::>
            # 1
            if event.type == pym.MOUSEBUTTONUP:   # elif
                self.stepMovObj_._move_(
                    mouse_position_on_click=pym.mouse.get_pos(),
                    deltaTime=self.dt
                )
            # 2
            """if event.type == pym.MOUSEBUTTONDOWN:
                for b_, ball_ in enumerate(self.BALLZ_):
                    ball_._move_(
                        mouse_position_on_click=pym.mouse.get_pos(),
                        deltaTime=self.dt
                    )"""
            # }
            # pym.mouse.set_cursor()
            
            # TIME DISPLAY & HANDLING ------->
            tc_ = pym.time.get_ticks()
            if tc_ % 1000 == 0:
                print(f" Elapsed time : {(tc_ / 1000):.2f}s ")
            if tc_ == 30000:
                self.running = False
            
            ## flip() the display to put your work on screen
            pym.display.flip()
            pym.display.set_caption(
                f"fps: {round(self.clock.get_fps(), 2)} | ball count: {len([])} |"  # self.BALLZ_
            )
            
            self.clock.tick(60)  ## limits FPS to 60
            
            # limits FPS to 60
            # dt is delta time in seconds since last frame, used for framerate-
            # independent physics.
            self.dt = self.clock.tick(60) / 1000
            #pg.display.update()
        pym.quit()


if __name__ == '__main__':
    yrypyg = TryPygame()
    TryPygame().runMainLoop()
    #
