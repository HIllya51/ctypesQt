#include<Windows.h>
#include<QApplication>
#include<QFont>
#include<QWidget>
#include<QPushButton>
#include<QDir>
#include<thread>
#include<queue>
#include<mutex>
#include<Shlwapi.h>
#include<filesystem>
int main(){
    int _=0;
    QApplication app(_, nullptr);
    app.setFont(QFont("MS Shell Dlg 2", 10));
    QWidget qw(NULL);
    //QPushButton qp(&qw);
    QPushButton qp("xxx", &qw);
    qw.show();
    app.exec();
}