import sys
import requests
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton,QLabel,QPushButton,QVBoxLayout,QLineEdit,QWidget,QHBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


def main():
    class weather_app(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setGeometry(630,300,500,500)
            self.setStyleSheet("background-color:black;"
                               "color:white;")
            self.setWindowTitle("WEATHER APP")
            self.setWindowIcon(QIcon("C:\\Users\\pkush\\Downloads\\4102326_cloud_sun_sunny_weather_icon.png"))
            self.initUI()
            
        def initUI(self):
                self.text=QLabel("CHECK WEATHER ☀️",self)
                self.city=QLabel("Enter city name:",self)
                self.cinput=QLineEdit(self)
                self.central_widget=QWidget()
                self.setCentralWidget(self.central_widget)
                self.vbox=QVBoxLayout()
                self.vbox.addWidget(self.text)
                self.text.setAlignment(Qt.AlignCenter)
                self.vbox.addWidget(self.city)
                self.city.setAlignment(Qt.AlignCenter)
                self.vbox.addWidget(self.cinput)
                self.central_widget.setLayout(self.vbox)
                self.submit=QPushButton("Check",self)
                self.vbox.addWidget(self.submit)
                self.hbox=QHBoxLayout()
                self.hbox.addWidget(self.cinput)
                self.hbox.addWidget(self.submit)
                self.vbox.addLayout(self.hbox)
                self.temp=QLabel(self)
                self.vbox.addWidget(self.temp)
                self.temp.setAlignment(Qt.AlignCenter)
                self.image=QLabel(self)
                self.image.setAlignment(Qt.AlignCenter)
                self.desc=QLabel(self)
                self.vbox.addWidget(self.image)
                self.vbox.addWidget(self.desc)
                self.desc.setAlignment(Qt.AlignCenter)
                self.image.setStyleSheet("""
                                         font-family:Segoe UI Emoji;
                                         font-size:150px;
                                         """)
                self.text.setStyleSheet("""                                        
                                        font-family:Audiowide;
                                        font-size:70px;
                                        color:#9B4DFF                                      
                                        """)
                self.city.setStyleSheet("""
                                        font-family:calibri;
                                        font-size:40px;
                                        color:#00FFFF;
                                        """)
                self.cinput.setStyleSheet("""
                                          font-family:Audiowide;
                                          font-size:20px;
                                          border:2px,solid;
                                          border-color:white;
                                          """)
                self.submit.setStyleSheet("""
                                          background-color:#9B4DFF;
                                          color:black;
                                          font-family:Audiowide;
                                          font-size:20px;
                                          """)
                self.temp.setStyleSheet("""
                                        color:#CBC3E3;
                                        font-size:40px;
                                        font-family:Lato Semibold;""")
    
                
                self.submit.clicked.connect(self.check_weather)
                
        def check_weather(self):
            self.api_key="8b1c4152bee19177c19a758b4d6367d6"
            self.url=f"https://api.openweathermap.org/data/2.5/weather?q={self.cinput.text()}&appid={self.api_key}"
            try:                
                response=requests.get(self.url)
                code=response.status_code
                match code:
                    case 200:
                        data=response.json()
                        print(data)
                        temp_k=data["main"]["temp"]
                        temp_c=temp_k-273.15
                        temp_f=(temp_k*9/5)-459.67
                        self.temp.setText(f"{temp_c:0.2f}°C,{temp_f:0.2f}°F")
                        id=data["weather"][0]["id"]
                        if id>=200 and id<=232:
                            self.image.setText("⛈️")
                        elif id>=300 and id<=321:
                            self.image.setText("🌧️")
                        elif id>=500 and id<=531:
                            self.image.setText("🌧️")
                        elif id>=600 and id<=622:
                            self.image.setText("🌨️")
                        elif id>=700 and id<=781:
                            self.image.setText("🌫️")
                        elif id==800:
                            self.image.setText("☀️")
                        elif id==801:
                            self.image.setText("⛅")
                        elif id==802:
                            self.image.setText("☁️")
                        elif id==803:
                            self.image.setText("☁️")
                        elif id==804:
                            self.image.setText("🌩️")
                        else:
                            self.image.setText("☁️")
                            
                        desc_city1=data["weather"][0]["description"]
                        desc_city1.upper()
                        desc_city2=float(data["main"]["temp_max"])
                        desc_city3=float(data["main"]["temp_min"])
                        desc_city4=float(data["main"]["feels_like"])
                        self.desc.setText(f"{desc_city1}\nMax Temp:{desc_city2-273.15:0.2f}°C\nMin Temp:{desc_city3-273.15:0.2f}°C\nFeels like:{desc_city4-273.15:0.2f}°C")
                        self.desc.setStyleSheet("""
                                                color:#CBC3E3;
                                                font-family:Lato Semibold;
                                                font-size:20px;""")
                    

                    case 400:
                        self.dis_error("Bad request")
                    case 401:
                        self.dis_error("Unauthorised")
                    case 403:
                        self.dis_error("Forbidden")
                    case 404:
                        self.dis_error("Not Found")
                    case 500:
                        self.dis_error("Internal Server")
                    case 502:
                        self.dis_error("Bad Gateway")
                    case 503:                       
                        self.dis_error("Service Unavailable")
                    case _:
                        self.dis_error("HTTP error occured")
                    
            except requests.exceptions.ConnectionError:
                self.dis_error("Check your Connections")
            except requests.exceptions.RequestException:
                self.dis_error("Request Error")
            
        
        def dis_error(self,message):
            self.temp.setText(f"{message}")
            self.image.setText("")
            self.desc.setText("")
        
        


        
    app=QApplication(sys.argv)
    w=weather_app()
    w.show()
    sys.exit(app.exec_())
        
if __name__=="__main__":
    main()