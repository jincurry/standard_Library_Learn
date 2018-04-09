import multiprocessing


class Worker(multiprocessing.Process):
    def run(self):
        print('in {}'.format(self.name))
        return

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = Worker()
        jobs.append(p)
        p.start()
    for job in jobs:
        job.join()
