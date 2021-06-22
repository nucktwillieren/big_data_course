from psychopy import visual, monitors, event, core
from win32api import GetSystemMetrics

import random
import json

from visual_helpers import create_grid_rects
from event import SequenceMemoryClickEvent, BaseClickEventManager
from base import LinkedNode, Event
from rules import *


class SequenceMemoryMixin:
    def setup(self, win=None):

        self.win_width_px, self.win_height_px = GetSystemMetrics(
            0), GetSystemMetrics(1)

        self.level = 1
        self.retry = 2

        self.grid_rects = create_grid_rects(
            600, 600, 10, 9, -300, -300,
            win=self.win, units="pix", fillColor=[-0.6, -0.088, 0.68]
        )

        self.level_text_posi = (-self.win_width_px/2 +
                                200, self.win_height_px/2 - 100)
        self.retry_text_posi = (-self.win_width_px/2 +
                                400, self.win_height_px/2 - 100)

        self.center_text = visual.TextStim(self.win, text="", pos=(0, 0), color=[
            1, 1, 1], units='pix', ori=0, height=50, wrapWidth=1280)

        self.retry_text = visual.TextStim(self.win, text="", pos=self.retry_text_posi, color=[
            1, 1, 1], units='pix', ori=0, height=50)

        self.level_text = visual.TextStim(self.win, text="", pos=self.level_text_posi, color=[
            1, 1, 1], units='pix', ori=0, height=50)

        self.exit_btn_posi = (self.win_width_px/2 - 100,
                              self.win_height_px/2 - 100)

        self.exit_btn = visual.Rect(self.win, pos=self.exit_btn_posi, units="pix", width=100,
                                    height=50, fillColor=[-0.6, -0.088, 0.68])
        self.exit_annotation = visual.TextStim(self.win, text="exit", pos=self.exit_btn_posi, color=[
            -1, -1, 1], units='pix', ori=0, height=20)

        self.add_obj(self.grid_rects)
        self.add_obj(self.center_text)
        self.add_obj(self.exit_btn)
        self.add_obj(self.exit_annotation)
        self.add_obj(self.retry_text)
        self.add_obj(self.level_text)

        self.click_event = SequenceMemoryClickEvent()
        self.click_event.add_click_handler(
            self.grid_rects, self.rect_flip_handler)
        self.click_event.add_click_handler(
            self.grid_rects, self.is_passed_handler, ["fail", "pass"])
        self.click_event.add_click_handler(
            self.exit_btn, self.exit_handler, "exit")

    def rule(self):
        self.center_text.setText(
            SEQUENCE_TEST_RULE
        )
        self.refresh(self.win)
        core.wait(10)

    def hint(self):
        for i in [i for i in range(1, 4)][::-1]:
            self.show_level(refresh=False)
            self.show_retry(refresh=False)
            self.center_text.setText(f"{i}")
            self.center_text.draw()
            self.win.flip()
            core.wait(1)
        self.center_text.setText("")
        self.center_text.draw()
        self.refresh(self.win)
        core.wait(1)

    def rect_flip_helper(self, rect, time):
        rect.setColor([1, 1, 1])
        self.refresh(self.win)
        core.wait(time)
        rect.setColor([-0.6, -0.088, 0.68])
        self.refresh(self.win)
        core.wait(0.1)

    def rect_reveal(self, rect):
        self.rect_flip_helper(rect, 0.5)

    def exit_handler(self, context):
        Event("exit")

    def rect_flip_handler(self, context):
        self.rect_flip_helper(self.context["rect"], 0.1)

    def is_passed_handler(self, context):
        if self.context["rect"] != self.target.value:
            self.context["mouse_event"] = "fail"
            self.context["level_event"] = "fail"
            return

        self.target = self.target.next

        if self.target == None:
            self.context["mouse_event"] = "pass"
            self.context["level_event"] = "pass"
            self.level += 1
            self.target = self.rects_node_head

    def event_reset(self):
        self.context["mouse_event"] = ""
        self.context["level_event"] = ""

    def reset(self):
        self.event_reset()
        self.clock = core.Clock()
        self.level = 1
        self.rects_node_head = LinkedNode()

    def show_level(self, refresh=True):
        self.level_text.setText(f"level: {self.level}")
        if refresh:
            self.refresh(self.win)

    def show_retry(self, refresh=True):
        self.retry_text.setText(f"retry: {self.retry}")
        if refresh:
            self.refresh(self.win)

    def init(self):
        self.show_level(refresh=False)
        self.show_retry(refresh=False)
        head = cur = self.rects_node_head
        last = LinkedNode()
        while cur != None and cur.value != None and isinstance(cur.value, visual.Rect):
            self.rect_reveal(cur.value)
            last = cur
            if cur.next == None:
                cur.next = LinkedNode()
            cur = cur.next

        random_rect = random.choice(self.grid_rects)
        while random_rect == last.value:
            random_rect = random.choice(self.grid_rects)

        self.rect_reveal(random_rect)
        cur.value = random_rect

        self.target = self.rects_node_head

    def turn(self):
        while self.context["level_event"] != "fail":
            self.init()
            self.click_event.wait(self.context)

        self.center_text.setText(
            F"You Failed(Level {self.level}), Retry: {self.retry} left")
        self.center_text.draw()
        self.win.flip()
        core.wait(3)
        self.center_text.setText("")

        self.retry -= 1
        if self.retry > -1:
            self.hint()

    def feedback(self):
        pass


class ChimpTestMixin:
    def setup(self, win=None):

        self.win_width_px, self.win_height_px = GetSystemMetrics(
            0), GetSystemMetrics(1)

        self.level = 1
        self.retry = 2

        self.grid_rects = create_grid_rects(
            1280, 720, 10, 72, -640, -384,
            win=self.win, units="pix", width=100,
            height=100, fillColor=self.win.color
        )

        self.numbers = self.create_numbers(self.grid_rects)

        self.level_text_posi = (-self.win_width_px/2 +
                                200, self.win_height_px/2 - 100)
        self.retry_text_posi = (-self.win_width_px/2 +
                                400, self.win_height_px/2 - 100)

        self.center_text = visual.TextStim(self.win, text="", pos=(0, 0), color=[
            1, 1, 1], units='pix', ori=0, height=50, wrapWidth=1280)

        self.retry_text = visual.TextStim(self.win, text="", pos=self.retry_text_posi, color=[
            1, 1, 1], units='pix', ori=0, height=50)

        self.level_text = visual.TextStim(self.win, text="", pos=self.level_text_posi, color=[
            1, 1, 1], units='pix', ori=0, height=50)

        self.exit_btn_posi = (self.win_width_px/2 - 100,
                              self.win_height_px/2 - 100)

        self.exit_btn = visual.Rect(self.win, pos=self.exit_btn_posi, units="pix", width=100,
                                    height=50, fillColor=[-0.6, -0.088, 0.68])
        self.exit_annotation = visual.TextStim(self.win, text="exit", pos=self.exit_btn_posi, color=[
            -1, -1, 1], units='pix', ori=0, height=20)

        self.add_obj(self.grid_rects)
        self.add_obj(self.center_text)
        self.add_obj(self.exit_btn)
        self.add_obj(self.exit_annotation)
        self.add_obj(self.retry_text)
        self.add_obj(self.level_text)
        self.add_obj(self.numbers)

        self.garbage = []
        self.target_grids = []

        self.click_event = BaseClickEventManager({}, {})
        self.click_event.add_click_handler(
            self.exit_btn, self.exit_handler, "exit")

    def rule(self):
        self.center_text.setText(
            CHIMP_TEST_RULE
        )
        self.refresh(self.win)
        core.wait(10)

    def hint(self):
        for i in [i for i in range(1, 4)][::-1]:
            self.show_level(refresh=False)
            self.show_retry(refresh=False)
            self.center_text.setText(f"{i}")
            self.center_text.draw()
            self.win.flip()
            core.wait(1)
        self.center_text.setText("")
        self.center_text.draw()

    def rects_flip_helper(self, rects):
        for rect in rects:
            rect.setColor([1, 1, 1])

        self.refresh(self.win)

    def rects_hidden_helper(self, rects):
        for rect in rects:
            rect.setColor(self.win.color)

        self.refresh(self.win)

    def correct_hide(self, rect):
        rect.setColor(self.win.color)
        self.refresh(self.win)

    def fail_reveal(self, rect):
        rect.setColor([-1, -1, -1])
        self.refresh(self.win)

    def rects_reveal(self, rects):
        self.rects_flip_helper(rects)

    def rects_hidden(self, rects):
        self.rects_hidden_helper(rects)

    def exit_handler(self, context):
        Event("exit")

    def is_passed_handler(self, context):
        if self.context["rect"] != self.target_grids[self.cursor]:
            self.fail_reveal(self.context["rect"])
            self.context["mouse_event"] = "fail"
            self.context["level_event"] = "fail"
            return
        else:
            self.correct_hide(self.context["rect"])
            self.cursor += 1

            for index, grid in enumerate(self.target_grids):
                self.numbers[tuple(grid.pos)].setText("")
            self.refresh(self.win)

            if self.context["rect"] not in self.correct_selected:
                self.correct_selected.append(self.context["rect"])

        if len(self.correct_selected) == len(self.target_grids):
            self.context["mouse_event"] = "pass"
            self.context["level_event"] = "pass"
            self.level += 1
            return

    def event_reset(self):
        self.context["mouse_event"] = ""
        self.context["level_event"] = ""

    def reset(self):
        self.event_reset()
        self.clock = core.Clock()
        self.level = 1

    def show_level(self, refresh=True):
        self.level_text.setText(f"level: {self.level}")
        if refresh:
            self.refresh(self.win)

    def show_retry(self, refresh=True):
        self.retry_text.setText(f"retry: {self.retry}")
        if refresh:
            self.refresh(self.win)

    def create_numbers(self, grids):
        numbers = {}
        for grid in grids:
            numbers[tuple(grid.pos)] = visual.TextStim(self.win, text="", pos=grid.pos, color=[
                -1, -1, -1], units='pix', ori=0, height=50)
            numbers[tuple(grid.pos)].draw()

        self.win.flip()
        core.wait(0.2)

        return numbers

    def get_grids_num(self):
        return self.level

    def init(self):
        self.click_event.remove_iter_click_handler(self.target_grids)
        self.rects_hidden(self.grid_rects)
        self.show_level(refresh=False)
        self.show_retry(refresh=False)
        # self.refresh(self.win)
        self.target_grids = random.sample(
            self.grid_rects, k=self.get_grids_num())

        self.click_event.add_click_handler(
            self.target_grids, self.is_passed_handler, wait=["fail", "pass"])

        for index, grid in enumerate(self.target_grids):
            self.numbers[tuple(grid.pos)].setText(str(index+1))

        self.cursor = 0
        self.correct_selected = []
        self.rects_reveal(self.target_grids)
        self.refresh(self.win)

    def turn(self):
        self.reset()

        while self.context["level_event"] != "fail":
            core.wait(0.2)
            self.init()
            self.click_event.wait(self.context)
#
        self.center_text.setText(
            F"You Failed(Level {self.level}), Retry: {self.retry} left")
        self.center_text.draw()
        self.win.flip()
        core.wait(3)
        self.center_text.setText("")

#
        self.retry -= 1
        if self.retry > -1:
            self.hint()

    def feedback(self):
        pass


class VirtualMemoryMixin:
    def setup(self, win=None):

        self.win_width_px, self.win_height_px = GetSystemMetrics(
            0), GetSystemMetrics(1)

        self.level = 1
        self.retry = 2

        self.grid_rects = create_grid_rects(
            600, 600, 10, 9, -300, -300,
            win=self.win, units="pix", width=100,
            height=100, fillColor=[-0.6, -0.088, 0.68]
        )

        self.level_text_posi = (-self.win_width_px/2 +
                                200, self.win_height_px/2 - 100)
        self.retry_text_posi = (-self.win_width_px/2 +
                                400, self.win_height_px/2 - 100)

        self.center_text = visual.TextStim(self.win, text="", pos=(0, 0), color=[
            1, 1, 1], units='pix', ori=0, height=50, wrapWidth=1280)

        self.retry_text = visual.TextStim(self.win, text="", pos=self.retry_text_posi, color=[
            1, 1, 1], units='pix', ori=0, height=50)

        self.level_text = visual.TextStim(self.win, text="", pos=self.level_text_posi, color=[
            1, 1, 1], units='pix', ori=0, height=50)

        self.exit_btn_posi = (self.win_width_px/2 - 100,
                              self.win_height_px/2 - 100)

        self.exit_btn = visual.Rect(self.win, pos=self.exit_btn_posi, units="pix", width=100,
                                    height=50, fillColor=[-0.6, -0.088, 0.68])
        self.exit_annotation = visual.TextStim(self.win, text="exit", pos=self.exit_btn_posi, color=[
            -1, -1, 1], units='pix', ori=0, height=20)

        self.add_obj(self.grid_rects)
        self.add_obj(self.center_text)
        self.add_obj(self.exit_btn)
        self.add_obj(self.exit_annotation)
        self.add_obj(self.retry_text)
        self.add_obj(self.level_text)

        self.click_event = BaseClickEventManager({}, {})
        self.click_event.add_click_handler(
            self.grid_rects, self.is_passed_handler, ["fail", "pass"])
        self.click_event.add_click_handler(
            self.exit_btn, self.exit_handler, "exit")

    def get_new_grids(self, n):
        self.remove_obj(self.grid_rects)
        self.click_event.remove_iter_click_handler(self.grid_rects)
        self.grid_rects = create_grid_rects(
            600, 600, 10, n, -300, -300,
            win=self.win, units="pix", width=100,
            height=100, fillColor=[-0.6, -0.088, 0.68]
        )
        self.click_event.add_click_handler(
            self.grid_rects, self.is_passed_handler, ["fail", "pass"])
        self.add_obj(self.grid_rects)

    def rule(self):
        self.center_text.setText(
            VISUAL_TEST_RULE
        )
        self.refresh(self.win)
        core.wait(10)

    def hint(self):
        for i in [i for i in range(1, 4)][::-1]:
            self.show_level(refresh=False)
            self.show_retry(refresh=False)
            self.center_text.setText(f"{i}")
            self.center_text.draw()
            self.win.flip()
            core.wait(1)
        self.center_text.setText("")
        self.center_text.draw()

    def rects_flip_helper(self, rects, time):
        for rect in rects:
            rect.setColor([1, 1, 1])

        self.refresh(self.win)
        core.wait(time)
        for rect in rects:
            rect.setColor([-0.6, -0.088, 0.68])

        self.refresh(self.win)
        core.wait(0.1)

    def rect_reveal(self, rect):
        self.rect_flip_helper(rect, 0.5)

    def correct_reveal(self, rect):
        rect.setColor([1, 1, 1])
        self.refresh(self.win)

    def fail_reveal(self, rect):
        rect.setColor([-1, -1, -1])
        self.refresh(self.win)

    def rects_reveal(self, rects):
        self.rects_flip_helper(rects, 2)

    def exit_handler(self, context):
        Event("exit")

    def rect_flip_handler(self, context):
        self.rect_flip_helper(self.context["rect"], 0.1)

    def is_passed_handler(self, context):
        if self.context["rect"] not in self.target_grids:
            self.life_count -= 1
            self.fail_reveal(self.context["rect"])
        else:
            self.correct_reveal(self.context["rect"])
            if self.context["rect"] not in self.correct_selected:
                self.correct_selected.append(self.context["rect"])

        if len(self.correct_selected) == len(self.target_grids):
            self.context["mouse_event"] = "pass"
            self.context["level_event"] = "pass"
            self.level += 1
            return

        if self.life_count == 0:
            self.context["mouse_event"] = "fail"
            self.context["level_event"] = "fail"
            return

    def event_reset(self):
        self.context["mouse_event"] = ""
        self.context["level_event"] = ""

    def reset(self):
        self.event_reset()
        self.clock = core.Clock()
        self.level = 1
        self.life_count = 3

    def show_level(self, refresh=True):
        self.level_text.setText(f"level: {self.level}")
        if refresh:
            self.refresh(self.win)

    def show_retry(self, refresh=True):
        self.retry_text.setText(f"retry: {self.retry}")
        if refresh:
            self.refresh(self.win)

    def get_grids_num(self):
        return ((self.level // 3) + 3) ** 2

    def get_answer_num(self):
        return self.level + 2

    def init(self):
        self.show_level(refresh=False)
        self.show_retry(refresh=False)
        self.get_new_grids(self.get_grids_num())
        self.target_grids = random.sample(
            self.grid_rects, k=self.get_answer_num())

        self.correct_selected = []
        self.rects_reveal(self.target_grids)
        self.refresh(self.win)

    def turn(self):
        while self.context["level_event"] != "fail":
            core.wait(0.2)
            self.init()
            self.click_event.wait(self.context)

        self.center_text.setText(
            F"You Failed(Level {self.level}), Retry: {self.retry} left")
        self.center_text.draw()
        self.win.flip()
        core.wait(3)
        self.center_text.setText("")

        self.retry -= 1
        if self.retry > -1:
            self.hint()

    def feedback(self):
        pass
