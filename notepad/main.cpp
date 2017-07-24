#include <QApplication>
#include <QtWidgets/QDialog>
#include <QtWidgets/QDesktopWidget>
#include "MainDialog.h"
#include "HtmlFinder.h"


int main(int argc, char *argv[]) {
    QApplication a(argc, argv);
    MainDialog d;

    d.hide();

    HtmlFinder *hf = new HtmlFinder(QUrl("http://blog.csdn.net/apple1985507"));

    return a.exec();
}