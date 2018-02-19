from copy import copy

import matplotlib.pyplot as plt

from dataset import generate


def first_come_first_served(jobs=None):
    if jobs is None:
        jobs = []

    jobs = copy(jobs)
    size = len(jobs)
    wait_time = 0.0
    current_time = 0.0

    while len(jobs):
        job_time = jobs.pop(0)
        wait_time += current_time
        current_time += job_time

    return wait_time / size


def shortest_job_first(jobs=None):
    if jobs is None:
        jobs = []

    jobs = copy(jobs)
    jobs.sort()
    size = len(jobs)
    wait_time = 0.0
    current_time = 0.0

    while len(jobs):
        job_time = jobs.pop(0)
        wait_time += current_time
        current_time += job_time

    return wait_time / size


def round_robin(jobs=None, quantum=3):
    if jobs is None:
        jobs = []

    jobs = copy(jobs)
    jobs.sort()
    size = len(jobs)
    wait_time = 0.0
    current_time = 0.0

    last_process_time = [0 for i in range(len(jobs))]
    while len(jobs):
        ended_job_indexs = []
        for i in range(len(jobs)):
            job_time = jobs[i]
            if job_time <= quantum:
                ended_job_indexs.append(i)
                wait_time += current_time - last_process_time[i]
                current_time += job_time
            else:
                current_time += quantum
                jobs[i] -= quantum
                last_process_time[i] = current_time

        ended_job_indexs.sort(reverse=True)
        for i in ended_job_indexs:
            jobs.pop(i)

    return wait_time / size


if __name__ == '__main__':

    rounds = 1000

    results = {'first_come_first_served': [[], [], []],
               'shortest_job_first': [[], [], []],
               'round_robin': [[], [], []]}

    for i in range(rounds):
        jobsets = [generate(100, [(2, 8, 0.7), (20, 30, 0.2), (35, 40, 0.1)]),
                   generate(100, [(2, 8, 0.5), (20, 30, 0.3), (35, 40, 0.2)]),
                   generate(100, [(2, 8, 0.3), (20, 30, 0.3), (35, 40, 0.4)])]

        for j in range(len(jobsets)):
            jobs = jobsets[j]
            results['first_come_first_served'][j].append(first_come_first_served(jobs))
            results['shortest_job_first'][j].append(shortest_job_first(jobs))
            results['round_robin'][j].append(round_robin(jobs))

    print results

    colors = {'first_come_first_served': 'Y',
              'shortest_job_first': 'g',
              'round_robin': 'r'}

    for algorithm in results:
        for i in range(len(results[algorithm])):
            wait_times = results[algorithm][i]
            plt.subplot(221 + i)
            plt.hist(wait_times, label="%s %d" % (algorithm, i), color=colors[algorithm])
            print "%s dataset %d avg wait time = %d" % (algorithm, i, sum(wait_times) / len(wait_times))

    plt.grid(True)
    plt.show()
