//
// Created by Administrator on 2017/7/10.
//

#include "HtmlFinder.h"

HtmlFinder::HtmlFinder(QString string) {
    this->url = string;
    this->parse();
}

HtmlFinder::~HtmlFinder() {
    delete this->view;
}

QWebElementCollection HtmlFinder::findAll(const QString &selectorQuery) {
    return this->element.findAll(selectorQuery);
}

QWebElement HtmlFinder::findFirst(const QString &selectorQuery) {
    return this->element.findFirst(selectorQuery);
}

QString HtmlFinder::getText() {
    return this->text;
}

void HtmlFinder::parse() {
    this->view = new QWebView();
    this->view->load(QUrl(this->url));
    connect(this->view, &QWebView::loadFinished, this, &HtmlFinder::loadFinished);

}

void HtmlFinder::loadFinished(bool) {
    this->text = this->view->page()->mainFrame()->toHtml();
    this->element = this->view->page()->mainFrame()->documentElement();
    QWebElementCollection ec = this->findAll("h3");
    QList<QWebElement> el = ec.toList();
    for (QWebElement e:el) {
        qDebug() << e.toOuterXml();
    }
}