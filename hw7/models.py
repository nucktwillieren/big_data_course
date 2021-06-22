from psychopy import visual, monitors, event, core, sound
from win32api import GetSystemMetrics

import random
import json


class BaseTrial:
    def __init__(self, trial_handler):
        self.trial_handler = trial_handler
        self.object_list = []

    def add_obj(self, obj):
        self.object_list.append(obj)

    def refresh(self, win):
        for obj in self.object_list:
            obj.draw()

        self.win.flip()

    def setup(self, context):
        return context

    def hint(self, context):
        return context

    def init(self, context):
        return context

    def turn(self, context):
        return context

    def run(self, context):
        for trial in self.trial_handler:
            context["trial"] = trial
            context = self.init(context)
            if context["err"] == "exit":
                return context

            context = self.turn(context)
            if context["err"] == "exit":
                return context

        return context

    def start(self):
        context = {"err": ""}

        context = self.setup(context)
        if context["err"] == "exit":
            return context

        context = self.hint(context)
        if context["err"] == "exit":
            return context

        context = self.run(context)
        if context["err"] == "exit":
            return context

        return context


class HighLowMixin:
    def setup(self, context):
        self.clock = core.Clock()
        self.win = visual.Window((GetSystemMetrics(0), GetSystemMetrics(
            1)), units="pix", fullscr=True, color=(1, 1, 1))
        self.win_width_px, self.win_height_px = GetSystemMetrics(
            0), GetSystemMetrics(1)

        self.mouse = event.Mouse()

        self.noun_text = visual.TextStim(self.win, text="", pos=(0, 0), color=[
            -1, -1, 1], units='pix', ori=0, height=50)

        self.high_btn_posi = (-100, -100)

        self.high_btn = visual.Rect(self.win, pos=self.high_btn_posi, units="pix", width=100,
                                    height=50, fillColor=[-1, 1, 1], lineColor=[-1, -1, 1])
        self.high_annotation = visual.TextStim(self.win, text="High", pos=self.high_btn_posi, color=[
            -1, -1, 1], units='pix', ori=0, height=20)

        self.low_btn_posi = (100, -100)

        self.low_btn = visual.Rect(self.win, pos=self.low_btn_posi, units="pix", width=100,
                                   height=50, fillColor=[-1, 1, 1], lineColor=[-1, -1, 1])
        self.low_annotation = visual.TextStim(self.win, text="Low", pos=self.low_btn_posi, color=[
            -1, -1, 1], units='pix', ori=0, height=20)

        self.click_check_posi = (0, -200)

        self.click_check_annotation = visual.TextStim(self.win, text="", pos=self.click_check_posi, color=[
            -1, -1, 1], units='pix', ori=0, height=20)

        self.exit_btn_posi = (0, -300)

        self.exit_btn = visual.Rect(self.win, pos=self.exit_btn_posi, units="pix", width=100,
                                    height=50, fillColor=[-1, 1, 1], lineColor=[-1, -1, 1])
        self.exit_annotation = visual.TextStim(self.win, text="exit", pos=self.exit_btn_posi, color=[
            -1, -1, 1], units='pix', ori=0, height=20)

        self.add_obj(self.noun_text)
        self.add_obj(self.high_btn)
        self.add_obj(self.high_annotation)
        self.add_obj(self.low_btn)
        self.add_obj(self.low_annotation)
        self.add_obj(self.click_check_annotation)
        self.add_obj(self.exit_btn)
        self.add_obj(self.exit_annotation)

        self.refresh(self.win)
        return context

    def hint(self, context):
        for i in range(3):
            self.noun_text.text = str(3-i)
            self.refresh(self.win)
            core.wait(1)

        return context

    def init(self, context):
        self.refresh(self.win)
        core.wait(.1)
        return context

    def turn(self, context):
        trial = context["trial"]
        trial_sound = sound.Sound(
            trial["pitch"], trial["secs"], volume=trial["volume"])
        trial_sound.play()
        start = self.clock.getTime()
        while 1:
            if self.mouse.isPressedIn(self.high_btn):
                self.click_check_annotation.text = "You Click High!"
                self.trial_handler.data.add("RT", self.clock.getTime() - start)
                self.trial_handler.data.add("choice", "high")
                trial_sound.stop()
                return context
            elif self.mouse.isPressedIn(self.low_btn):
                self.click_check_annotation.text = "You Click Low!"
                self.trial_handler.data.add("RT", self.clock.getTime() - start)
                self.trial_handler.data.add("choice", "low")
                trial_sound.stop()
                return context
            elif self.mouse.isPressedIn(self.exit_btn):
                self.win.close()
                context['err'] = "exit"
                return context

            self.refresh(self.win)

        return context


class HighLowTrial(HighLowMixin, BaseTrial):
    pass
