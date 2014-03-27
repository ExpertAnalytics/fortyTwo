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
    def __init__(self, tasks, *args, **kwargs):
        self.tasks = tasks

    def update(self, tasks, start, stop=None):
        """
        Update schedule for future events
        """
        if stop is not None:
            assert stop < len(self.tasks)
            self.tasks[start:stop] = tasks[:]
        else:
            self.tasks[start:] = tasks[:]

    def step(self):
        return self.tasks.pop(0)  # Pop first entry in the event list

    def duration(self):
       return sum([task.duration() for task in self.tasks])


class Log(object):
    """
    A log is similar to a Schedule, but it records when transitions actually takes place.
    """

    def __init__(self, schedule):
        self.schedule = schedule
        self.log = []

    def record(self, time):
        self.log.append((self.schedule.step(), time))  # Store the entry as a tuple
