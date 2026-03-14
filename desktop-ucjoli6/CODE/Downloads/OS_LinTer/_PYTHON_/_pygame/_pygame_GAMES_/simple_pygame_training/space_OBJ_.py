import pygame as pym
import math
# import tryGame_

class SpacialOBJ:
    # sModel = None   # stop | its going to be an encapsulation
    # surface_ = None
    #position_OBJc_ = None

    def __main__representation__(self,  cat: bool = False, ):
        """
        ```
        # -------------------------------------------------------------------------------
        # Path Equation of all Obj
        # ---------------------------
        #
        # "Uniform Movement" :
        # {
        #   "By Illustrating":
        #   {
        #   <remark> I always see </remark>
        #   -------------------------------
        #                      . .x_ .                   
        #                   .    |      .                
        # ________________.______|___      .        |   
        #    |          .        |           .      | g[v]
        # Vy |------/--x Vv      |             .    |           ^------x a[v]
        #    |      \ *|         |               .  *       ay  |    * |
        #    |       * |         |  Hmax           .            |  *   |
        #    |      *  |         |                  .           |o------>
        #    |     *   |         |                   .              ax <-- { sometimes or always,
        #    |    *    |         |                    .                       ax can be equals to 0 }
        #    |   *     |         |                     .              ^
        #    |  *      |         |                      .             |___ { so, a[v]=ay (approximatively)
        #    | *\      |         |                       .              => a[v] = g[v] (basically) }
        # ___|o_/______|_________|________________________.________________________________
        #    |       Vx                                    . <- X_target                             
        # -1 |1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28|
        # ------------------------------------
        # With,
        # - (V[d] * sin(θ))² / 2*g
        #
        # ----------------------------------------------- THOUGH ->
        #  "In Programming":
        #  {
        #    <remark> I always see </remark>
        #    >-------------------------------<
        #    d[x,y] = V[x,y] * dt  {Programmation; ...}
        #  } ->
        # ----------------------------------------------- BUT ->
        #
        #  "Mathematically":
        #  {
        #    <remark> We gonna know that: </remark>
        #    (Eq): y = ax² + bx + c
        #  } ->
        # ----------------------------------------------- SO ->
        #
        #  "Physically":
        #  {
        #   ># 1rst_ly : Newton's Law
        #    --------
        #   Based on Newtom laws, we know this:
        #   F[v] = P[v], ( with F[v] = m * a[v] => a[v] = F[v] / m; and P[v] = m * g[v] )
        #   <=> m * a[v] = m * g[v]
        #   <=> a[v] = g[v]
        #   <=> a = -g    (a = ay by axes projections)
        #    --------
        #
        #   ># 2nd_ly : Composante of all vectors
        #    -------
        #     { As we know,
        #       - d[x,y] = V[x,y] * dt + d[x0,y0]
        #       - dt = t - t0
        #     } -> [ sometimes, we work (keep on), (x0, y0, t0) = (0, 0, 0) ]
        #    -------
        #
        #   ># 3rd_ly : Development
        #    -------
        #   {
        #   > Formula of physics metrics:
        #    -------
        #   * Acceleration :
        #   V[y] = a[y] * dt + V[oy]
        #   V[x] = a[x] * dt + V[ox]
        #   * Speed :
        #   y = V[y] * dt + y0 = V[d]sin($\\alpha$[deg]) * dt + y0
        #   x = V[x] * dt + x0 = V[d]cos($\\alpha$[deg]) * dt + x0
        #   }
        #    -------
        #   {
        # dt = x / V[d]cos($\\alpha$[deg])
        # =>
        #       V[d]sin($\\alpha$[deg])
        # y = --------------------------- * (x - x0) + y0
        #       V[d]cos($\\alpha$[deg])
        # =>
        # y = tan($\\alpha$[deg]) * (x - x0) + y0
        #    -------
        # With, (x0, y0, t0) = (0, 0, 0), we have,
        # y = tan($\\alpha$[deg]) * x
        #    -------
        #   }
        # -------------------------------------------------
        #  } ->
        # }
        # ------------------------------------------------------------------------------
        #
        # ------------------------------------------------------------------------------
        # ->    END
        ```
        """
        pass

    def __init__(self,
                 surface_: pym.Surface = None,
                 targetPosition: str = None,
                 position_OBJc_: pym.Vector2|int|float = None,  # m
                 dt_: float = 0.01, # s
                 v_: float = 200,  # m/s
                 a_: float = 10.01,  # m/s²
                 g_: float = 9.81,  # m/s²
                 ):  # screen: pym.display.set_mode, #
        #self.sModel_ = pym.draw.rect(surface=surface_, color=(0,0,177), width=12)
        # self.sModel = self.sModel_  #
        self.surface_ = surface_    # Ambiguité
        self.targetPos_ = targetPosition # Facultative
        #self.position_OBJc_ = position_OBJc_
        self.position_sOBJ_ = position_OBJc_# or pym.Vector2(surface_.get_width() / 2, surface_.get_height() / 2)   #
        self.t0, self.t = 0, 12
        self.dt = (self.t - self.t0) or dt_ # Optional
        self.speed = v_
        self.acceleration = a_
        self.gravity = g_   # Optional  -< General  Environment
    #
    
    # encapsulation methods
    # ----------------------------------------------------------------------
    def getObjPosition_(self, ):
        return self.position_sOBJ_
    def getObjPosition_X(self, ):
        return self.position_sOBJ_.x
    def getObjPosition_Y(self, ):
        return self.position_sOBJ_.y
    """def getSquaredModel_(self, ):
    if surface, so, position calculated, and no need position;
        return self.sModel_"""
    #

    # main methods
    # ----------------------------------------------------------------------
    def _draw_(self,
               geo_OBJ: str = "CIRCLE",
               # Objects Parameters
               surface_: pym.Surface = None,    # pym.display.set_mode(size=(640, 480))
               color_: pym.Color = "green",
               # Rect parameters
               rect_left_top_width_height: tuple[float, float, float, float] = (0, 0, 0, 0),
               border_thickness: int = 1,
               # Polygon parameters
               # Circle parameters
               position_OBJc_: pym.Vector2|int|float = None,
               radius_: float = 21,
               # else
               ):
        """
        **geo_OBJ**
         type: str\n
         value: `"RECT"` || `"POLYGON"` || `"CIRCLE"` || `"ELLIPSE"` || `"ARC"` || `"LINE"` || `"LINES"` || `"AALINE"` || `"AALINES"`  (refering to `pygame.draw` module)
        **screen**
         type: `Surface` (pygame)\n
        """
        if geo_OBJ == "RECT":
            pym.draw.rect(surface=surface_, color=color_, rect=pym.Rect(rect_left_top_width_height), width=border_thickness)
        elif geo_OBJ == "POLYGON":
            pym.draw.polygon(surface=surface_, color=color_, )
        elif geo_OBJ == "CIRCLE":
            if not surface_:
                surface_ = self.surface_
            if not position_OBJc_:
                position_OBJc_ = self.position_sOBJ_
            pym.draw.circle(surface=surface_, color=color_, center=position_OBJc_, radius=radius_, )
        elif geo_OBJ == "ELLIPSE":
            pym.draw.ellipse(surface=surface_, color=color_, )
        elif geo_OBJ == "ARC":
            pym.draw.arc(surface=surface_, color=color_, )
        elif geo_OBJ == "LINE":
            pym.draw.line(surface=surface_, color=color_, )
        elif geo_OBJ == "LINES":
            pym.draw.lines(surface=surface_, color=color_, )
        elif geo_OBJ == "AALINE":
            pym.draw.aaline(surface=surface_, color=color_, )
        elif geo_OBJ == "AALINES":
            pym.draw.aalines(surface=surface_, color=color_, )
        """else:   # to busy & slow
            print(f"Geometric Object not present in 'pygame.draw' module. ")"""
        #
    
    def _move_(self,
               geo_OBJ: str = None,
               targertPos: str = None,
               mouse_position_on_click: tuple[int, int] = None,
               deltaTime: float = None,
               ):
        """```if not deltaTime:
            deltaTime = self.dt
        ```"""
        dt = deltaTime
        # MOUSE MOVEMENT
        if mouse_position_on_click:
            """self.speed = mouse_position_on_click / dt
            self.position_sOBJ_ = self.speed * dt"""
            self.position_sOBJ_.x = mouse_position_on_click[0]# * dt
            self.position_sOBJ_.y = mouse_position_on_click[1]# * dt
        # KEY MOVEMENT
        if geo_OBJ == "RECT": pass
        elif geo_OBJ == "POLYGON": pass
        #
        elif geo_OBJ == "CIRCLE":
            if targertPos == "UP":
                teta_ = 30
                tetaV_ = self.speed * math.cos(teta_)
                self.position_sOBJ_.x += tetaV_ * dt
                #self.position_sOBJ_.y += - ((self.gravity / 2) * pow(dt, 2)) + (self.speed/3)*math.sin(30) * dt
                self.position_sOBJ_.y += - ((self.gravity / (2 * pow(tetaV_, 2))) * pow(self.position_sOBJ_.x, 2)) + math.tan(teta_) * self.position_sOBJ_.x
            elif targertPos == "DOWN":
                self.position_sOBJ_.y += self.speed * dt
            elif targertPos == "LEFT":
                self.position_sOBJ_.x -= self.speed * dt
            elif targertPos == "RIGHT":
                self.position_sOBJ_.x += self.speed * dt
            """else:
                print("User were pressing other(s) key(s)")"""
        elif geo_OBJ == "ELLIPSE": pass
        elif geo_OBJ == "ARC":  pass
        elif geo_OBJ == "LINE": pass
        elif geo_OBJ == "LINES": pass
        elif geo_OBJ == "AALINE": pass
        elif geo_OBJ == "AALINES": pass
        """else:    # to busy
            print(f"Geometric Object not present in 'pygame.draw' module. ")"""
        #

if __name__ == "__main__":
    sqrobj = SpacialOBJ()

