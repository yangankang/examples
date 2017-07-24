//
// Created by Administrator on 2017/7/10.
//

#include "HtmlFinder.h"

HtmlFinder::HtmlFinder(QUrl url) {
    this->url = url;
    this->parse();
    this->loadText(this->url);
}

HtmlFinder::HtmlFinder(QString text) {
    this->text = text;
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

QString HtmlFinder::loadText(QUrl url) {
    QNetworkAccessManager *manager = new QNetworkAccessManager(this);
    connect(manager, SIGNAL(finished(QNetworkReply * )),
            this, SLOT(loadFinished(QNetworkReply * )));

    manager->get(QNetworkRequest(url));
}

void HtmlFinder::parse() {
    this->view = new QWebView();

    if (!this->text.isEmpty()) {
        this->view->setHtml(this->text);
        this->element = this->view->page()->mainFrame()->documentElement();
    }

}

void HtmlFinder::loadFinished(QNetworkReply *reply) {
    QByteArray dt = reply->readAll();
    this->text = QString(dt);
    this->element = this->view->page()->mainFrame()->documentElement();
    emit finished(this);
    /*QWebElementCollection ec = this->findAll("h3");
    QList<QWebElement> el = ec.toList();
    for (QWebElement e:el) {
        qDebug() << e.toOuterXml();
    }*/
}