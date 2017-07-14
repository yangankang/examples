//
// Created by Administrator on 2017/7/10.
//

#include <QtGui/QPainter>
#include <QtWidgets/QSystemTrayIcon>
#include <QtWidgets/QMenu>
#include <QtWidgets/QAction>
#include <QtCore/QCoreApplication>
#include "MainDialog.h"


MainDialog::MainDialog() {
    setWindowTitle("QT窗体");

    setWindowTitle("Hello QT Window");
    resize(500, 300);
    setAttribute(Qt::WA_TranslucentBackground);
    setWindowFlags(Qt::FramelessWindowHint | Qt::Tool | Qt::X11BypassWindowManagerHint | Qt::WindowStaysOnTopHint);

    setSystemTrayIcon();
}

MainDialog::~MainDialog() {

}

void MainDialog::paintEvent(QPaintEvent *) {

    QPainter painter(this);
    painter.fillRect(this->rect(), QColor(50, 50, 50, 255));
}

void MainDialog::setSystemTrayIcon() {

    QSystemTrayIcon *systemTrayIcon = new QSystemTrayIcon(this);
    QMenu *menu = new QMenu();
    QAction *exitAction = new QAction(this);
    exitAction->setText("退出");
    exitAction->setIcon(QIcon(":resource/imgs/exit.png"));
    menu->addAction(exitAction);

    systemTrayIcon->setIcon(QIcon(":resource/imgs/icon.png"));
    systemTrayIcon->setContextMenu(menu);
    systemTrayIcon->setToolTip("小工具");
    systemTrayIcon->show();

    connect(exitAction, &QAction::triggered, this, &MainDialog::exitApp);
    connect(systemTrayIcon, &QSystemTrayIcon::activated, this, &MainDialog::showAndFront);
}

void MainDialog::exitApp() {
    QCoreApplication::exit(1);
}

void MainDialog::showAndFront(QSystemTrayIcon::ActivationReason reason) {
    if (reason == QSystemTrayIcon::DoubleClick) {
        //this->setWindowFlags(this->windowFlags() | Qt::WindowStaysOnTopHint);
        if (this->isHidden()) {
            this->show();
        } else {
            this->hide();
        }
    }
}