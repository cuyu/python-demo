'''_
@author: Curtis Yu
@contact: cuyu@splunk.com
@since: 7/18/16
'''
import time

_BASE = time.time()
def simple_task(name):
    print name + ' start at {0}'.format(str(round(time.time() - _BASE)))
    time.sleep(1)
    # print name


class Task(object):
    def __init__(self, task_func, schedule_interval, *task_args):
        self.task_func = task_func
        self.schedule_interval = schedule_interval
        self.task_args = task_args
        self.next_run_time = None

    def schedule_next_run(self, time):
        self.next_run_time = time

    def run(self):
        return self.task_func(*self.task_args)

    def __lt__(self, other):
        return self.next_run_time < other.next_run_time


class Scheduler(object):
    """
    Assume all the tasks are running asynchronously.
    """
    def __init__(self):
        self.tasks = []

    def add_task(self, task_func, schedule_interval, *task_args):
        self.tasks.append(Task(task_func, schedule_interval, *task_args))

    def run_tasks(self):
        start_time = time.time()
        for task in self.tasks:
            task.schedule_next_run(start_time + task.schedule_interval)
            task.run()

        while True:
            for task in self.tasks:
                if task.next_run_time <= start_time:
                    task.schedule_next_run(task.next_run_time + task.schedule_interval)
                    task.run()

            fastest_task = min(self.tasks)
            now = time.time()
            # print 'sleep {0}s'.format(round(max(fastest_task.next_run_time - now, 0)))
            time.sleep(max(fastest_task.next_run_time - now, 0))
            start_time = time.time()


if __name__ == '__main__':
    scheduler = Scheduler()
    scheduler.add_task(simple_task, 5, *('a',))
    scheduler.add_task(simple_task, 8, *('b',))
    scheduler.add_task(simple_task, 10, *('c',))
    scheduler.run_tasks()
