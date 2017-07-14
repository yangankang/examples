#include <QApplication>
#include <QtWidgets/QDialog>
#include <QtWidgets/QDesktopWidget>
#include "MainDialog.h"


int main(int argc, char *argv[]) {
    QApplication a(argc, argv);
    MainDialog d;

    d.hide();
    return a.exec();
}