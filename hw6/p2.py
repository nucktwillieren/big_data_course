from psychopy import visual, monitors, event, core
from win32api import GetSystemMetrics

import random
import json


class Noun:
    def __init__(self, noun_type, name):
        self.noun_type = noun_type
        self.name = name


class NounManager:
    def __init__(self):
        self._dict = {}

    def add(self, noun_type, name):
        self._dict[name] = Noun(noun_type, name)

    def get_random(self):
        return random.choice(list(self._dict.values()))

    def get_type(self, noun_type):
        return [noun for noun in self._dict.values() if noun.noun_type == noun_type]

    def get(self, name):
        try:
            return self._dict[name]
        except KeyError:
            return

    def remove(self, name):
        try:
            self._dict.pop(name)
        except KeyError:
            return

    def is_type(self, name, noun_type):
        try:
            return self.get(name).noun_type == noun_type
        except KeyError:
            return


class BaseTrial:
    def __init__(self, turns, preloaded_data):
        self.turns = turns
        self.preloaded_data = preloaded_data
        self.object_list = []

    def add_obj(self, obj):
        self.object_list.append(obj)

    def refresh(self, win):
        for obj in self.object_list:
            obj.draw()

        self.win.flip()

    def preload(self, context):
        return context

    def setup(self, context):
        return context

    def hint(self, context):
        return context

    def init(self, context):
        return context

    def turn(self, context):
        return context

    def save_turn(self, context):
        return context

    def save_all(self, context):
        return context

    def analyze(self, context):
        return context

    def save_analysis(self, context):
        return context

    def run(self, context):
        for i in range(self.turns):
            context = self.init(context)
            if context["err"] == "exit":
                return context

            context = self.turn(context)
            if context["err"] == "exit":
                return context

            context = self.save_turn(context)
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

        context = self.save_all(context)
        if context["err"] == "exit":
            return context

        context = self.analyze(context)
        if context["err"] == "exit":
            return context

        context = self.save_analysis(context)
        if context["err"] == "exit":
            return context

        return context


class JsonSaveAllMixin:
    def save_turn(self, context):
        if "final_result" not in context:
            context["final_result"] = []
        context["final_result"].append(context["result"])
        return context

    def save_all(self, context):
        data = context["final_result"]
        with open("data.json", "w") as w:
            json.dump(data, w, indent=4)

        return context


class SuccssRateAnalyzeMixin:
    def analyze(self, context):
        super().analyze(context)
        total_count = len(context["final_result"])
        success_count = 0
        for result in context["final_result"]:
            if result["success"]:
                success_count += 1
        context["analysis"] = {
            "success_rate":  success_count / total_count
        }

        return context

    def save_analysis(self, context):
        data = context["analysis"]
        with open("success_rate_analysis.json", "w") as w:
            json.dump(data, w, indent=4)

        return context


class AnimalFruitMixin:
    def setup(self, context):
        self.clock = core.Clock()
        self.win = visual.Window((GetSystemMetrics(0), GetSystemMetrics(
            1)), units="pix", fullscr=True, color=(1, 1, 1))
        self.win_width_px, self.win_height_px = GetSystemMetrics(
            0), GetSystemMetrics(1)

        self.mouse = event.Mouse()

        self.noun_text = visual.TextStim(self.win, text="", pos=(0, 0), color=[
            -1, -1, 1], units='pix', ori=0, height=50)

        self.animal_btn_posi = (-100, -100)

        self.animal_btn = visual.Rect(self.win, pos=self.animal_btn_posi, units="pix", width=100,
                                      height=50, fillColor=[-1, 1, 1], lineColor=[-1, -1, 1])
        self.animal_annotation = visual.TextStim(self.win, text="Animal", pos=self.animal_btn_posi, color=[
            -1, -1, 1], units='pix', ori=0, height=20)

        self.fruit_btn_posi = (100, -100)

        self.fruit_btn = visual.Rect(self.win, pos=self.fruit_btn_posi, units="pix", width=100,
                                     height=50, fillColor=[-1, 1, 1], lineColor=[-1, -1, 1])
        self.fruit_annotation = visual.TextStim(self.win, text="fruit", pos=self.fruit_btn_posi, color=[
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
        self.add_obj(self.animal_btn)
        self.add_obj(self.animal_annotation)
        self.add_obj(self.fruit_btn)
        self.add_obj(self.fruit_annotation)
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
        noun = self.preloaded_data.get_random()
        self.noun_text.text = noun.name
        self.refresh(self.win)
        core.wait(.1)
        context["noun"] = noun
        return context

    def turn(self, context):
        noun = context["noun"]
        start = self.clock.getTime()
        while 1:
            if self.mouse.isPressedIn(self.animal_btn):
                self.click_check_annotation.text = "You Click Animal!"
                context['result'] = {
                    "success": self.preloaded_data.is_type(noun.name, "a"),
                    "target_name": noun.name,
                    "target_type": noun.noun_type,
                    "user_click_type": "animal",
                    "reaction_time": self.clock.getTime() - start,
                }
                return context
            elif self.mouse.isPressedIn(self.fruit_btn):
                self.click_check_annotation.text = "You Click Fruit!"
                context['result'] = {
                    "success": self.preloaded_data.is_type(noun.name, "f"),
                    "target_name": noun.name,
                    "target_type": noun.noun_type,
                    "user_click_type": "fruit",
                    "reaction_time": self.clock.getTime() - start,
                }
                return context
            elif self.mouse.isPressedIn(self.exit_btn):
                self.win.close()
                context['err'] = "exit"
                return context

            self.refresh(self.win)

        return context


class AnimalFruitTrial(AnimalFruitMixin, JsonSaveAllMixin, SuccssRateAnalyzeMixin, BaseTrial):
    pass


def main():
    manager = NounManager()
    # f for fruit
    # a for animal
    manager.add("f", "apple")
    manager.add("f", "banana")
    manager.add("f", "cherry")
    manager.add("f", "dragonfruit")
    manager.add("f", "elderberry")
    manager.add("a", "ant")
    manager.add("a", "bear")
    manager.add("a", "cow")
    manager.add("a", "dog")
    manager.add("a", "eagle")

    trial = AnimalFruitTrial(10, manager)
    trial.start()


if __name__ == '__main__':
    main()
