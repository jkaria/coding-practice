#!/usr/local/bin/python3

import subprocess
import time
import select


def pipe_inputs():
    def capture_timestamp():
        return subprocess.Popen(['date', '+%s'], stdout=subprocess.PIPE)

    def print_captured_timestamp(input_stdin):
        return subprocess.Popen(['xargs', 'echo', 'captured timestamp is'],
                                stdin=input_stdin,
                                stdout=subprocess.PIPE)

    print("Starting pipe_inputs test")
    capture_procs = []
    print_procs   = []
    for _ in range(5):
        c_proc = capture_timestamp()
        capture_procs.append(c_proc)
        p_proc = print_captured_timestamp(c_proc.stdout)
        print_procs.append(p_proc)
    for c_proc in capture_procs:
        c_proc.communicate()
    for p_proc in print_procs:
        out, err = p_proc.communicate()
        print("Output: {}, Error: {}".format(out, err))
    print("Test end.")
    select.select([], [], [], 0.1)


def sleep_in_parallel(time_in_seconds):
    def run_sleep():
        return subprocess.Popen(['sleep', str(time_in_seconds)])

    print("Starting parallel sleep test. Sleep time: {}".format(time_in_seconds))
    start = time.time()
    procs = []
    for _ in range(10):
        procs.append(run_sleep())
    for proc in procs:
        proc.communicate()
    end = time.time()
    print("Test ends. Parallel sleeping test took: {:.2f} seconds to complete".format(end-start))


if __name__ == '__main__':
    print("Testing subprocess concept!")
    sleep_in_parallel(0.2)
    pipe_inputs()
