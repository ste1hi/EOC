import sys
import time
import csv
import datetime
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import QTimer
from alarm import Dialog

class QmyWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__ui = Dialog.Ui_Dialog()
        self.__ui.setupUi(self)
        self.timer = QTimer()
        self.timer.stop()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.do_time_out)
        self.timer.start()
        self.__ui.time_now.setDigitCount(8)
        self.__ui.over_time.setDigitCount(8)
        self.__ui.rest_time.setDigitCount(8)
        self.__ui.finish_class.clicked.connect(self.on_finish_class_clicked)
        self.on_finish_class_clicked()
        self.__ui.rest_time.setSegmentStyle(2)
        self.__ui.over_time.setSegmentStyle(2)
        self.__ui.time_now.setSegmentStyle(2)
        self.__ui.rest_time.setStyleSheet("color:#FFFFFF")
        self.__ui.over_time.setStyleSheet("color:#FFFFFF")
        self.__ui.time_now.setStyleSheet("color:#FFFFFF")

    def do_time_out(self):
        self.time_now = datetime.datetime(time.localtime().tm_year,time.localtime().tm_mon,time.localtime().tm_mday,time.localtime().tm_hour,time.localtime().tm_min,time.localtime().tm_sec)
        i = 0
        if self.over_hour < time.localtime().tm_hour:
            i = 1
        elif self.over_hour == time.localtime().tm_hour:
            if self.over_min < time.localtime().tm_min:
                i = 1
            elif self.over_min == time.localtime().tm_min:
                if self.over_sec < time.localtime().tm_sec:
                    i = 1
            else:
                pass
        else:
            pass

        if i == 1:
            self.rest = (self.time_now - self.over_time).seconds
            self.__ui.label_4.setText("请下课！！")
            self.__ui.rest_time.setSegmentStyle(2)
            self.__ui.rest_time.setStyleSheet("color:#FF0000")
            self.__ui.label_4.setStyleSheet("color:#FF0000")
            self.__ui.now_subject.setStyleSheet("color:#FF0000")
            self.__ui.now_subject.setText("下课")
            self.__ui.label_3.setStyleSheet("color:#FF0000")
            self.__ui.label_3.setText("拖堂时间")
        else:
            self.rest = (self.over_time - self.time_now).seconds
            self.__ui.label_4.setText("不拖堂的您最美")
            self.__ui.label_3.setText("剩余时间")
            self.__ui.label_4.setStyleSheet("color:#FFFFFF")
            self.__ui.now_subject.setStyleSheet("color:#FFFFFF")
            self.__ui.rest_time.setStyleSheet("color:#00FF00")
            self.__ui.label_3.setStyleSheet("color:#00FF00")
        self.hour = self.rest//3600
        self.min = self.rest//60%60
        self.sec = self.rest%60
        if self.sec < 10:
            self.sec = "0" + str(self.sec)
        if self.min < 10:
            self.min = "0" + str(self.min)
        if self.hour < 10:
            self.hour = "0" + str(self.hour)

        self.__ui.rest_time.display(f"{self.hour}:{self.min}:{self.sec}")
        self.__ui.time_now.display(time.ctime().split()[-2])
        i == 0

    def on_finish_class_clicked(self):
        file = time.ctime().split(" ")[0] + ".csv"
        with open(file) as f:
            reader = csv.reader(f)
            i = 0
            while i < 6:
                text = next(reader)
                if int(text[-3]) > time.localtime().tm_hour:
                    self.__ui.over_time.display(f"{text[-3]}:{text[-2]}:{text[-1]}")
                    self.over_time = datetime.datetime(time.localtime().tm_year, time.localtime().tm_mon,
                                                       time.localtime().tm_mday, int(text[-3]), int(text[-2]),
                                                       int(text[-1]))
                    self.over_hour = int(text[-3])
                    self.over_min = int(text[-2])
                    self.over_sec = int(text[-1])
                    self.__ui.now_subject.setText(text[0])
                    break
                elif int(text[-3]) == time.localtime().tm_hour:
                    if int(text[-2]) > time.localtime().tm_min:
                        self.__ui.over_time.display(f"{text[-3]}:{text[-2]}:{text[-1]}")
                        self.over_time = datetime.datetime(time.localtime().tm_year, time.localtime().tm_mon,
                                                           time.localtime().tm_mday, int(text[-3]), int(text[-2]),
                                                           int(text[-1]))
                        self.over_hour = int(text[-3])
                        self.over_min = int(text[-2])
                        self.over_sec = int(text[-1])
                        self.__ui.now_subject.setText(text[0])
                        break
                    elif int(text[-2]) == time.localtime().tm_min:
                        if int(text[-1]) > time.localtime().tm_sec:
                            self.__ui.over_time.display(f"{text[-3]}:{text[-2]}:{text[-1]}")
                            self.over_time = datetime.datetime(time.localtime().tm_year, time.localtime().tm_mon,
                                                               time.localtime().tm_mday, int(text[-3]), int(text[-2]),
                                                               int(text[-1]))
                            self.over_hour = int(text[-3])
                            self.over_min = int(text[-2])
                            self.over_sec = int(text[-1])
                            self.__ui.now_subject.setText(text[0])
                            break
                    else:
                        pass
                else:
                    pass
                i += 1
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QmyWidget()
    form.show()
    sys.exit(app.exec_())
