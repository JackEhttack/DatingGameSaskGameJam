init python:

    import pygame

    class MinigameDisplayable(renpy.Displayable):

        def __init__(self, question, answer):

            renpy.Displayable.__init__(self)

            self.text = ""
            self.question = question
            self.answer = answer

            # The sizes of some of the images.
            self.BUTTON_SIZE = 128
            self.BUTTON_BORDER = 16

            self.BAR_WIDTH = 640
            self.BAR_HEIGHT = 128
            self.BAR_BORDER = 16

            # Some displayables we use.
            self.button = Solid("#ff0000", xsize=self.BUTTON_SIZE, ysize=self.BUTTON_SIZE)
            self.button_back = Solid("#888888", xsize=self.BUTTON_SIZE+self.BUTTON_BORDER, ysize=self.BUTTON_SIZE+self.BUTTON_BORDER)

            self.bar = Solid("#ff0000", xsize=self.BAR_WIDTH, ysize=self.BAR_HEIGHT)
            self.bar_border = Solid("#888888", xsize=self.BAR_WIDTH+self.BAR_BORDER, ysize=self.BAR_HEIGHT+self.BAR_BORDER)

            self.sleep_meter = 100

            # The time of the past render-frame.
            self.oldst = None

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

            """
            # This draws a paddle, and checks for bounces.
            def paddle(px, py, hotside):

                # Render the paddle image. We give it an 800x600 area
                # to render into, knowing that images will render smaller.
                # (This isn't the case with all displayables. Solid, Frame,
                # and Fixed will expand to fill the space allotted.)
                # We also pass in st and at.
                pi = renpy.render(self.paddle, width, height, st, at)

                # renpy.render returns a Render object, which we can
                # blit to the Render we're making.
                r.blit(pi, (int(px), int(py - self.PADDLE_HEIGHT / 2)))

                if py - self.PADDLE_HEIGHT / 2 <= self.by <= py + self.PADDLE_HEIGHT / 2:

                    hit = False

                    if oldbx >= hotside >= self.bx:
                        self.bx = hotside + (hotside - self.bx)
                        self.bdx = -self.bdx
                        hit = True

                    elif oldbx <= hotside <= self.bx:
                        self.bx = hotside - (self.bx - hotside)
                        self.bdx = -self.bdx
                        hit = True

                    if hit:
                        renpy.sound.play("pong_boop.opus", channel=1)
                        self.bspeed *= 1.10

            # Draw the two paddles.
            paddle(self.PADDLE_X, self.playery, self.PADDLE_X + self.PADDLE_WIDTH)
            paddle(width - self.PADDLE_X - self.PADDLE_WIDTH, self.computery, width - self.PADDLE_X - self.PADDLE_WIDTH)

            # Draw the ball.
            ball = renpy.render(self.ball, width, height, st, at)
            r.blit(ball, (int(self.bx - self.BALL_WIDTH / 2),
                            int(self.by - self.BALL_HEIGHT / 2)))

            # Check for a winner.
            if self.bx < -50:
                self.winner = "eileen"

                # Needed to ensure that event is called, noticing
                # the winner.
                renpy.timeout(0)

            elif self.bx > width + 50:
                self.winner = "player"
                renpy.timeout(0)
            """

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
                # Ensure the pong screen updates.
                renpy.restart_interaction()

            if ev.type == pygame.TEXTINPUT:
                print(ev.text)
                renpy.restart_interaction()

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

    text _(question):
        xpos 0.5
        xanchor 0.5
        ypos 0.15
        size 25

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