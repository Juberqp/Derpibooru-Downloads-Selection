from PyQt5.QtWidgets import *
from PyQt5 import uic
import shutil
import sys
import json
import os

form_class = uic.loadUiType("derpi.ui")[0]

copy = 0

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

#텍스트 박스 지정
        self.lineEdit_1.textChanged.connect(self.lineEdit_01)
        self.lineEdit_2.textChanged.connect(self.lineEdit_02)
        self.lineEdit_3.textChanged.connect(self.lineEdit_03)
        self.lineEdit_4.textChanged.connect(self.lineEdit_04)

#라디오 버튼 지정
        self.radioButton.clicked.connect(self.RadFunction)
        self.radioButton_2.clicked.connect(self.RadFunction)

#일반 버튼 지정
        self.pushButton_1.clicked.connect(self.pushButton_01)

#텍스트 박스 실행
    def lineEdit_01(self):
        print(self.lineEdit_1.text()) #테스트 끝나면 삭제

    def lineEdit_02(self):
        print(self.lineEdit_2.text()) #테스트 끝나면 삭제
        
    def lineEdit_03(self):
        print(self.lineEdit_3.text()) #테스트 끝나면 삭제
        
    def lineEdit_04(self):
        print(self.lineEdit_4.text()) #테스트 끝나면 삭제

#라디오 버튼 실행
    def RadFunction(self):
        if self.radioButton.isChecked():
            print("GroupBox_rad1 Chekced") #테스트 끝나면 삭제
        elif self.radioButton_2.isChecked():
            print("GroupBox_rad2 Checked") #테스트 끝나면 삭제

#일반 버튼 실행
    def pushButton_01(self):        
        white = []
        black = []
        
        if len(self.lineEdit_1.text()) > 0:
            white = self.lineEdit_1.text().split(',')
        if len(self.lineEdit_2.text()) > 0:
            black = self.lineEdit_2.text().split(',')
        
#리스트에 빈 공간, 앞뒤 띄어쓰기 제거
        for i in range(len(white)):
            white[i] = white[i].strip()
        for i in range(len(black)):
            black[i] = black[i].strip()
        
        print(white) #테스트 끝나면 삭제
        print(black) #테스트 끝나면 삭제
        
        print(len(self.lineEdit_1.text())) #테스트 끝나면 삭제
        print(len(self.lineEdit_2.text())) #테스트 끝나면 삭제
                                                        
        #Json 폴더에 들어가서 Json 리스트 확인, 저장
        path = "./Json/"
        json_stone = os.listdir(path)
        json_list = [file for file in json_stone if file.endswith('.json')]
                
        print(json_list) #테스트 끝나면 삭제
                
        #Json 파일에 모든 Json에 들어가서 white와 같은 태그가 있는지 확인
        for i in range(len(json_list)):
            check = 0
            JS = "./Json/"+json_list[i]
            with open(JS, 'r', encoding='UTF8') as file:
                data = json.load(file)
                for j in range(len(white)):
                    for k in range(len(data["tags"])):
                        #print(white[j], data["tags"][k]) #테스트 끝나면 삭제
                        if white[j] == data["tags"][k]:
                            check = check + 1
                            #print('cheak 더하기', check) #테스트 끝나면 삭제
                if len(self.lineEdit_2.text()) > 0:
                    for j in range(len(black)):
                        for k in range(len(data["tags"])):
                            if black[j] == data["tags"][k]:
                                check = 0              
                if check == len(white):
                    print("./Json/"+json_list[i],'가 같습니다.') #테스트 끝나면 삭제
                    if os.path.isdir('./'+self.lineEdit_3.text()) == 0:
                        mkfile = './'+self.lineEdit_3.text()
                        os.mkdir(mkfile)

#파일 확장자 검사               
                    a = ['.gif','.jpg','.png','.temp','.webm']
                    
                    if self.radioButton.isChecked(): 
                        for tg in a:
                            if os.path.isfile('./'+self.lineEdit_4.text()+'/'+json_list[i].strip(".json")+tg):
                                shutil.copy('./'+self.lineEdit_4.text()+'/'+json_list[i].strip(".json")+tg, "./"+self.lineEdit_3.text())
                    elif self.radioButton_2.isChecked():
                        for tg in a:
                            if os.path.isfile('./'+self.lineEdit_4.text()+'/'+json_list[i].strip(".json")+tg):
                                shutil.move('./'+self.lineEdit_4.text()+'/'+json_list[i].strip(".json")+tg, "./"+self.lineEdit_3.text())
                    else:
                        print('아무것도 입력되지 않음')
                            
if __name__ == "__main__":
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()