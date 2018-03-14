import functools
import queue
import threading


@functools.total_ordering
class Job:
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description
        print('New Job:', description)
        return

    def __eq__(self, other):
        try:
            return self.priority == other.priority
        except AttributeError:
            return NotImplemented

    def __lt__(self, other):
        try:
            return self.priority <= other.priority
        except AttributeError:
            return NotImplemented


q = queue.PriorityQueue()
q.put(Job(3, 'Mid-level Job'))
q.put(Job(10, 'Low_level Job'))
q.put(Job(1, 'Important Job'))


def process_job(que):
    while True:
        next_job = que.get()
        print('Processing Job:', next_job.description)
        que.task_done()


workers = [
    threading.Thread(target=process_job, args=(q,)),
    threading.Thread(target=process_job, args=(q,)),
]
for w in workers:
    w.setDaemon(True)
    w.start()

q.join()
