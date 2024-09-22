init python:

    import pygame, math

    def dynamic_bar(st, at, d):
        if d.resting:
            return Solid("#5b3bce", xsize=(math.floor(d.BAR_WIDTH*d.sleep_meter)), ysize=d.BAR_HEIGHT), 0
        return Solid("#481ce9", xsize=(math.floor(d.BAR_WIDTH*d.sleep_meter)), ysize=d.BAR_HEIGHT), 0

    def dynamic_button(st, at, d):
        if d.focusing:
            return Solid("#00ff00", xsize=d.BUTTON_SIZE, ysize=d.BUTTON_SIZE), 0
        return Solid("#ff0000", xsize=d.BUTTON_SIZE, ysize=d.BUTTON_SIZE), 0

    def question_text(st, at, d):
        return Text(d.question, size=25), 0

    def input_text(st, at, d):
        return Text(d.text, size=25), 0


    class MinigameDisplayable(renpy.Displayable):

        def __init__(self, question, answer):

            renpy.Displayable.__init__(self)

            self.text = ""
            self.question = question
            self.answer = answer

            # The sizes of some of the images.
            self.BUTTON_SIZE = 64
            self.BUTTON_BORDER = 16

            self.BAR_WIDTH = 480
            self.BAR_HEIGHT = 64
            self.BAR_BORDER = 16

            self.PUNISHMENT = 0.1
            self.SLEEP_RECOVERY = 0.5

            self.sleep_meter = 1

            # Some displayables we use.
            self.button = DynamicDisplayable(dynamic_button, self)
            self.button_back = Solid("#888888", xsize=self.BUTTON_SIZE+self.BUTTON_BORDER, ysize=self.BUTTON_SIZE+self.BUTTON_BORDER)

            self.bar = DynamicDisplayable(dynamic_bar, self)
            self.bar_border = Solid("#888888", xsize=self.BAR_WIDTH+self.BAR_BORDER, ysize=self.BAR_HEIGHT+self.BAR_BORDER)

            
            self.qt = DynamicDisplayable(question_text, self)
            self.tt = DynamicDisplayable(input_text, self)

            # The time of the past render-frame.
            self.oldst = None
            self.modifier = 0.1

            self.focusing = False
            self.resting = False

            # The winner.
            self.result = None

            pygame.key.start_text_input()

        # no idea what these lines do, keep just in case
        # def visit(self):
        #    return [ self.paddle, self.ball ]

        # Recomputes the position of the ball, handles bounces, and
        # draws the screen.
        def render(self, width, height, st, at):

            # The Render object we'll be drawing into.
            r = renpy.Render(width, height)

            # Figure out the time elapsed since the previous frame.
            if self.oldst is None:
                self.oldst = st

            dtime = st - self.oldst
            self.oldst = st

            self.modifier += dtime / 50

            if self.resting:
                self.sleep_meter = min(self.sleep_meter + dtime * self.SLEEP_RECOVERY, 1)
            self.sleep_meter -= dtime * self.modifier

            if self.sleep_meter < 0:
                self.result = "sleep"
                renpy.timeout(0)

            bar_back = renpy.render(self.bar_border, width, height, st, at)
            r.blit(bar_back, ((width-self.BAR_WIDTH)/2, 875))
            
            self.bar.xsize = self.BAR_WIDTH * self.sleep_meter / 100

            bar = renpy.render(self.bar, width, height, st, at)
            r.blit(bar, ((width-self.BAR_WIDTH+self.BAR_BORDER)/2, 875+self.BAR_BORDER/2))
            
            button_back = renpy.render(self.button_back, width, height, st, at)
            r.blit(button_back, ((width-self.BAR_WIDTH+self.BAR_BORDER)/2-self.BUTTON_SIZE-16-self.BUTTON_BORDER*1.5, height*0.15+12-self.BUTTON_SIZE/2))

            button = renpy.render(self.button, width, height, st, at)
            r.blit(button, ((width-self.BAR_WIDTH+self.BAR_BORDER)/2-self.BUTTON_SIZE-self.BUTTON_BORDER-16, height*0.15+12-self.BUTTON_SIZE/2+self.BUTTON_BORDER/2))
            
            if self.sleep_meter > 0.8 and self.focusing:
                qt = renpy.render(self.qt, width, height, st, at)
                r.blit(qt, (width*0.38, height*0.15))

            if self.sleep_meter > 0.25:
                tt = renpy.render(self.tt, width, height, st, at)
                r.blit(tt, (width*0.38, height*0.19))

            # Ask that we be re-rendered ASAP, so we can show the next
            # frame.

            #renpy.render()
            renpy.redraw(self, 0)

            # Return the Render object.
            return r

        # Handles events.
        def event(self, ev, x, y, st):

            # Mousebutton down == start the game by setting stuck to
            # false.
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                if x > (1920-self.BAR_WIDTH)/2 and x < ((1920-self.BAR_WIDTH)/2+self.BAR_WIDTH)+self.BAR_BORDER and y > (875+self.BAR_BORDER/2) and y < (875+self.BAR_BORDER/2) + self.BAR_HEIGHT + self.BAR_BORDER:
                    self.resting = True
                if x > (1920-self.BAR_WIDTH+self.BAR_BORDER)/2-self.BUTTON_SIZE-self.BUTTON_BORDER-16 and x < (1920-self.BAR_WIDTH+self.BAR_BORDER)/2-16 and y > 1080*0.15+12-self.BUTTON_SIZE/2+self.BUTTON_BORDER/2 and y < 1080*0.15+12+self.BUTTON_SIZE/2+self.BUTTON_BORDER/2:
                    self.focusing = True
                
                renpy.restart_interaction()
            elif ev.type == pygame.MOUSEBUTTONUP and ev.button == 1:
                self.resting = False
                self.focusing = False
                renpy.restart_interaction()
            if ev.type == pygame.TEXTINPUT:
                self.text += ev.text
                renpy.restart_interaction()
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_BACKSPACE:
                self.text = self.text[0:-1]
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_RETURN:
                if self.text.rstrip() == self.answer:
                    return "correct"
                else:
                    self.modifier += self.PUNISHMENT

            # Set the position of the player's paddle.

            # If we have a winner, return him or her. Otherwise, ignore
            # the current event.
            if self.result:
                pygame.key.stop_text_input()
                return self.result
            else:
                raise renpy.IgnoreEvent()

screen Minigame(question, answer):

    default Minigame = MinigameDisplayable(question, answer)

    add "minigame"

    add Minigame

    text _("Sleepy Meter"):
        xpos 0.5
        xanchor 0.5
        ypos 0.75
        size 40

    text _("Question:"):
        xpos 0.5
        xanchor 0.5
        ypos 0.1
        size 40

    text _("Focus"):
        xpos 0.345
        xanchor 0.5
        ypos 0.1
        size 20

    #text _("Eileen"):
    #    xpos (1280 - 240)
    #    xanchor 0.5
    #    ypos 25
    #    size 40

    #if pong.stuck:
    #    text _("Click to Begin"):
    #        xalign 0.5
    #        ypos 50
    #        size 40