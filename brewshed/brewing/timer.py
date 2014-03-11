class Timer(object):
    """
    The timer should be started when brewing is initiated, and should be used to track times
    and to issue alerts according to a given recipe. It should also be used to record events, like when
    boil starts, hop is added, cooldown, etc.
    """

    pass


class Schedule(object):
    """
    The Schedule should contain a list of events (transitions between states in the brew process), and times
    when the events should occur.
    """
    def __init__(self, recipe, *args, **kwargs):
        self.recipe = recipe
        self.events = recipe.events
        self.current_step = 0

    def update(self, recipe):
        """
        Update schedule for future events
        """
        assert self.recipe is not None, "Cannot update Scheduler"
        self.events[self.current_step:] = Schedule(recipe).events[self.current_step:]

    def next(self):
        self.current_step += 1
        return self.current_step

    def prev(self):
        if self.current_step > 0:
            self.current_step -= 1
        return self.current_step


class BrewLog(object):
    """
    The brew log is similar to the Schedule, but it records when transitions actually takes place.
    """

    def __init__(self, schedule):
        self.events = schedule.events[:]
        self.log = []

    def step(self, time):
        self.log.append((self.events.pop(), time))  # Store the entry as a tuple
