//
// Created by Administrator on 2017/7/10.
//

#ifndef NOTEPAD_HTMLFINDER_H
#define NOTEPAD_HTMLFINDER_H


#include <QtCore/QString>
#include <QtXml/QtXml>

class HtmlFinder {

public:
    explicit HtmlFinder(QString string);

    ~HtmlFinder();

    QString getText();

    HtmlFinder finder(QString path);

private:
    QString text;
    QDomDocument document;

    void parse();
};


#endif //NOTEPAD_HTMLFINDER_H
