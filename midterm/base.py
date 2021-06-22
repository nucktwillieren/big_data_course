from psychopy import event, visual
from win32api import GetSystemMetrics

import numpy as np
from error import ExitInterupt


class LinkedNode:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next = next_node


class Observer:
    """
    The Subject owns some important state and notifies observers when the state
    changes.
    """

    _state = None
    """
    For the sake of simplicity, the Subject's state, essential to all
    subscribers, is stored in this variable.
    """

    _observers = []
    """
    List of subscribers. In real life, the list of subscribers can be stored
    more comprehensively (categorized by event type, etc.).
    """

    def __init__(self):
        self._observers.append(self)
        self._observables = {}

    def observe(self, event_name, callback):
        self._observables[event_name] = callback


class Event:
    def __init__(self, name, autofire=True, *args, **kwargs):
        self.name = name
        self.args = args
        self.kwargs = kwargs
        if autofire:
            self.fire()

    def fire(self):
        for observer in Observer._observers:
            if self.name in observer._observables:
                observer._observables[self.name](*self.args, **self.kwargs)


class BaseClickEventManager:

    # handlers = {
    #   "rect"(rect_obj): [handler1, handler2, ...]
    #   .
    #   .
    # }
    def __init__(self, click_handlers={}, release_handlers={}):
        self.mouse = event.Mouse()
        self.context = {"mouse_event": None}
        self.wait_list = []

        self.click_handlers = click_handlers
        self.release_handlers = release_handlers

    def _iter_is_pressed(self, iter_obj):
        for rect in iter_obj:
            if self.mouse.isPressedIn(rect):
                return True

    def _is_pressed_in(self, target_rect):
        if isinstance(target_rect, (list, tuple, set)):
            return self._iter_is_pressed(target_rect)

        if isinstance(target_rect, dict):
            return self._iter_is_pressed(target_rect.values())

        return self.mouse.isPressedIn(target_rect)

    def rect_check(self, iter_obj):
        for rect in iter_obj:
            if self._is_pressed_in(rect):
                return rect

    def handle_click(self, context):
        rect = self.rect_check(self.click_handlers.keys())
        if rect:
            self.context["rect"] = rect
            self.context["mouse"] = self.mouse
            for handler in self.click_handlers[rect]:
                handler(self.context)
            print(self.context)

    def handle_release(self, context):
        rect = self.rect_check(self.release_handlers.keys())
        if rect:
            self.context["rect"] = rect
            self.context["mouse"] = self.mouse
            for handler in self.release_handlers[rect]:
                self.context = handler(self.context)

    def trigger(self, context):
        self.mouse.clickReset()
        buttons = self.mouse.getPressed()
        while not np.any(buttons):
            buttons = self.mouse.getPressed()

        self.handle_click(self.context)

        while np.any(buttons):
            buttons = self.mouse.getPressed()

        self.handle_release(self.context)

    def add_iter_handler(self, handler_container, iter_obj, handler):
        for obj in iter_obj:
            if obj not in handler_container:
                handler_container[obj] = []
            handler_container[obj].append(handler)

    def remove_iter_click_handler(self, iter_obj):
        for obj in iter_obj:
            if obj in self.click_handlers:
                del self.click_handlers[obj]

    def add_rect_handler(self, handler_container, target_rect, handler):
        if target_rect not in handler_container:
            handler_container[target_rect] = []
        handler_container[target_rect].append(handler)

    def add_click_handler(self, target_rect, handler, wait=None):
        if wait:
            self.add_wait_status(wait)
        if isinstance(target_rect, list):
            self.add_iter_handler(self.click_handlers, target_rect, handler)
            return

        self.add_rect_handler(self.click_handlers, target_rect, handler)

    def add_release_handler(self, target_rect, handler, wait=None):
        if wait:
            self.add_wait_status(wait)
        if isinstance(target_rect, list):
            self.add_iter_handler(self.release_handlers, target_rect, handler)
            return

        self.add_rect_handler(self.release_handler, target_rect, handler)

    def set_event(self, value):
        self.context["mouse_event"] = value

    def get_event(self):
        return self.context["mouse_event"]

    def add_wait_status(self, value):
        if isinstance(value, (list, set)):
            for status in value:
                self.wait_list.append(status)

            self.wait_list = list(set(self.wait_list))
            return

        self.wait_list.append(value)
        self.wait_list = list(set(self.wait_list))

    def wait(self, context):
        self.context = context
        self.context["mouse_event"] = None
        while self.context["mouse_event"] not in self.wait_list:
            self.trigger(self.context)


class BaseTrial(Observer):
    def __init__(self, trial_handler=None, turns=0, win=None):
        super().__init__()
        if win is None:
            self.win = visual.Window((GetSystemMetrics(0), GetSystemMetrics(
                1)), units="pix", fullscr=True, color=[-0.656, 0.08, 0.672])
        else:
            self.win = win

        self.trial_handler = trial_handler
        self.object_list = []
        self.turns = turns
        self.context = {"err": "", "level_event": ""}

        self.observe("exit", exit)

    def exit(self):
        try:
            self.win.close()
        except:
            pass
        raise ExitInterupt("Exit!")

    def add_obj(self, obj):
        self.object_list.append(obj)

    def remove_obj(self, obj):
        self.object_list.remove(obj)

    def refresh(self, win):
        for obj in self.object_list:
            if isinstance(obj, (list, tuple, set)):
                for t in obj:
                    try:
                        t.draw()
                    except Exception as e:
                        print(self.click_event.click_handlers)
                        print(e)
            elif isinstance(obj, dict):
                for t in obj.values():
                    try:
                        t.draw()
                    except Exception as e:
                        print(self.click_event.click_handlers)
                        print(e)
            else:
                try:
                    obj.draw()
                except Exception as e:
                    print(self.click_event.click_handlers)
                    print(e)
        try:
            self.win.flip()
        except Exception as e:
            print(self.click_event.click_handlers)
            print(e)

    def setup(self):
        pass

    def rule(self):
        pass

    def hint(self):
        pass

    def reset(self):
        pass

    def init(self):
        pass

    def turn(self):
        pass

    def feedback(self):
        pass

    def clean_up(self):
        for obj in self.object_list:
            del obj
        self.object_list = []

    def _run_with_trial_handler(self):
        for trial in self.trial_handler:
            self.context["trial"] = trial
            self.reset()
            self.turn()

    def _run_without_trial_handler(self):
        for i in range(self.turns):
            self.reset()
            self.turn()

    def run(self):
        if self.trial_handler:
            self._run_with_trial_handler()
            return

        if self.turns > 0:
            self._run_without_trial_handler()
            return

    def start(self):
        try:
            self.setup()
            self.rule()
            self.hint()
            self.run()
            self.feedback()
            self.clean_up()
            self.win.close()

        except ExitInterupt as e:
            print(e)
            return context


class Level:
    def __init__(self, trial, context):
        self.trial = trial
        self.context = context

    def run(self):
        pass

    def start(self):
        self.trial.init()
        self.trial.run()
