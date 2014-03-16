class Timer(object):
    """
    The timer should be started when brewing is initiated, and should be used to track times
    and to issue alerts according to a given recipe. It should also be used to record events, like when
    boil starts, hop is added, cooldown, etc.
    """

    pass


class Schedule(object):
    """
    The Schedule should contain a list of events (transitions between states in the brew process). An event needs to
    have a duration method returning the planned/estimated time of the state it initiates.
    when the events should occur.
    """
    def __init__(self, events, *args, **kwargs):
        self.events = events

    def update(self, events, start, stop=None):
        """
        Update schedule for future events
        """
        if stop is not None:
            assert stop < len(self.events)
            self.events[start:stop] = events[:]
        else:
            self.events[start:] = events[:]

    def step(self):
        return self.events.pop()

   def duration(self):
       return sum([event.duration() for event in self.events])


class BrewLog(object):
    """
    The brew log is similar to the Schedule, but it records when transitions actually takes place.
    """

    def __init__(self, schedule):
        self.events = schedule.events[:]
        self.log = []

    def step(self, time):
        self.log.append((self.events.pop(), time))  # Store the entry as a tuple
