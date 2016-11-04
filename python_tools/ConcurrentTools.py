import sys
import threading
import multiprocessing
import time
import signal
from multiprocessing import Manager
from urllib.request import urlopen

do_count = 0
is_running = True


class WorkThread(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url
        self.isSuccess = True

    def run(self):
        try:
            response = urlopen(self.url)
        except OSError:
            self.isSuccess = False
        pass

    def get_result(self):
        return self.isSuccess


class JobProcess(multiprocessing.Process):
    def __init__(self, thread_count, url, extime):
        multiprocessing.Process.__init__(self)
        self.thread_count = thread_count
        self.url = url
        if extime < 0:
            extime = 0
        self.extime = extime
        """这里用于产生一个共享变量List否则两个变量始终是0"""
        self.success = Manager().list()
        self.failure = Manager().list()

    def run(self):

        time.sleep(self.extime)

        works = []

        for i in range(self.thread_count):
            """这里的args非常的恶心传参(url)则会报错(url,)这样才会成功"""
            works.append(WorkThread(self.url))

        for w in works:
            w.start()
            w.join()
            if w.get_result():
                self.success.append(w.get_result())
            else:
                self.failure.append(w.get_result())
        pass

    def get_success_count(self):
        return len(self.success)

    def get_failure_count(self):
        return len(self.failure)


def exec_thread(count, process_count, thread_count, interval_time, url):
    global do_count, is_running
    if do_count >= count:
        sys.exit(0)
    else:
        do_count += 1

    if process_count <= 0 or thread_count <= 0:
        print("警告:执行进程数或者线程数为零")
        sys.exit(0)

    ctime, diff_time, jobs = time.time(), process_count * 0.5, []
    for i in range(process_count):
        job = JobProcess(thread_count, url, diff_time)
        job.start()
        jobs.append(job)
        diff_time = diff_time - (time.time() - ctime)

    success = 0
    failure = 0

    for j in jobs:
        j.join()
        success += j.get_success_count()
        failure += j.get_failure_count()

    print("执行结果| ", "耗时=" + str(time.time() - ctime) + " | ", "进程数=" + str(process_count) + " | ",
          "每个进程的线程数=" + str(thread_count) + " | ", "成功数=" + str(success) + " | ", "失败数=" + str(failure))

    if is_running:
        next_timer = threading.Timer(interval_time, exec_thread,
                                     [count, process_count, thread_count, interval_time, url])
        next_timer.start()


def quit_pro(signum, frame):
    global is_running
    is_running = False


helpStr = "argv[0] #执行的次数\r\n" + \
          "argv[1] #进程数\r\n" + \
          "argv[2] #线程数\r\n" + \
          "argv[3] #间隔时间s\r\n" + \
          "argv[4] #访问的url\r\n"

argv = sys.argv
if __name__ == "__main__":
    try:
        if len(argv) != 6:
            print("参数错误,传参格式如下:\r\n" + helpStr)
            print(argv)
            sys.exit(-1)

        signal.signal(signal.SIGINT, quit_pro)
        signal.signal(signal.SIGTERM, quit_pro)

        c = int(argv[1])
        pc = int(argv[2])
        tc = int(argv[3])
        s = int(argv[4])
        url = str(argv[5])

        timer = threading.Timer(0, exec_thread, [c, pc, tc, s, url])
        timer.start()
    except Exception:
        raise
