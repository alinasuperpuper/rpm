class StepTracker:
    def __init__(self):
        self.steps = 0

    def track_steps(self, steps):
        self.steps += steps

    def get_steps(self):
        return self.steps


class HeartRateMonitor:
    def __init__(self):
        self.heart_rate = 70

    def set_heart_rate(self, heart_rate):
        self.heart_rate = heart_rate

    def get_heart_rate(self):
        return self.heart_rate


class SleepTracker:
    def __init__(self):
        self.sleep_hours = 0

    def track_sleep(self, hours):
        self.sleep_hours += hours

    def get_sleep_hours(self):
        return self.sleep_hours


class FitnessTrackerFacade:
    def __init__(self):
        self.step_tracker = StepTracker()
        self.heart_rate_monitor = HeartRateMonitor()
        self.sleep_tracker = SleepTracker()

    def track_steps(self, steps):
        self.step_tracker.track_steps(steps)

    def set_heart_rate(self, heart_rate):
        self.heart_rate_monitor.set_heart_rate(heart_rate)

    def track_sleep(self, hours):
        self.sleep_tracker.track_sleep(hours)

    def get_health_report(self):
        return {
            'steps': self.step_tracker.get_steps(),
            'heart_rate': self.heart_rate_monitor.get_heart_rate(),
            'sleep_hours': self.sleep_tracker.get_sleep_hours()
        }


fitness_tracker = FitnessTrackerFacade()


fitness_tracker.track_steps(5000)
fitness_tracker.set_heart_rate(75)
fitness_tracker.track_sleep(7)


health_report = fitness_tracker.get_health_report()


print(f'шагов: {health_report["steps"]}')
print(f'сердечный ритм: {health_report["heart_rate"]} ударов в минуту')
print(f'сон: {health_report["sleep_hours"]}ч')
