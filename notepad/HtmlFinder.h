//
// Created by Administrator on 2017/7/10.
//

#ifndef NOTEPAD_HTMLFINDER_H
#define NOTEPAD_HTMLFINDER_H


#include <QtCore/QString>
#include <QtXml/QtXml>
#include <QtWebKitWidgets/QtWebKitWidgets>

class HtmlFinder : public QObject {

Q_OBJECT
public:
    explicit HtmlFinder(QString string);

    ~HtmlFinder();

    QString getText();

    QWebElementCollection findAll(const QString &selectorQuery);

    QWebElement findFirst(const QString &selectorQuery);

private:
    QWebView *view;
    QString text;
    QString url;
    QWebElement element;

    void parse();

public slots:

    void loadFinished(bool);
};


#endif //NOTEPAD_HTMLFINDER_H
