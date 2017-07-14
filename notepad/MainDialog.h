//
// Created by Administrator on 2017/7/10.
//

#ifndef NOTEPAD_MAINWINDOW_H
#define NOTEPAD_MAINWINDOW_H


#include <QtWidgets/QDialog>
#include <QtWidgets/QSystemTrayIcon>

class MainDialog : public QDialog {

Q_OBJECT
public:
    explicit MainDialog();

    ~MainDialog();

    void paintEvent(QPaintEvent *);

    void setSystemTrayIcon();

public slots:

    void exitApp();

    void showAndFront(QSystemTrayIcon::ActivationReason reason);
};


#endif //NOTEPAD_MAINWINDOW_H
