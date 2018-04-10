#!/usr/bin/env python
# -*- coding: utf-8 -*-
import schedule
import time


def task(n):
    print 'task-{0} start'.format(n)
    schedule.every(10).seconds.do(task, n + 1)
    print 'task-{0} end'.format(n)
    return schedule.CancelJob


def main():
    schedule.every(10).seconds.do(task, 1)
    while 1:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    main()
