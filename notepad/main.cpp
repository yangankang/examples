#include <QApplication>
#include <QtWidgets/QDialog>
#include <QtWidgets/QDesktopWidget>
#include "MainDialog.h"
#include "HtmlFinder.h"


int main(int argc, char *argv[]) {
    QApplication a(argc, argv);
    MainDialog d;

    d.hide();

    HtmlFinder hf("https://www.w3.org/TR/REC-CSS2/selector.html");

    return a.exec();
}