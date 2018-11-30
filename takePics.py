# coding=utf-8
import cv2
import sys
import time
import datetime
import os

if __name__ == '__main__':
    dir = "observation/"
    if not os.path.exists(dir):
        os.mkdir(dir)
    print "save path:", dir

    start_time = int(time.time())
    if sys.argv.__len__() == 2:
        interval = int(sys.argv[1])
    else:
        interval = 10
    print "start time:", datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
    shot_time = start_time + interval

    while True:
        now_time = int(time.time())
        if now_time == shot_time:
            # windows下特定参数CAP_DSHOW，否则windows会报警告(但也可以运行)，但在Linux下不需要此参数，否则没有数据
            cap = cv2.VideoCapture(0 + cv2.CAP_DSHOW)
            ret, frame = cap.read()
            save_str = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d-%H-%M-%S')
            print "shot time:", save_str
            cv2.imwrite(dir + save_str + ".jpg", frame)
            shot_time = now_time + interval
            cap.release()
