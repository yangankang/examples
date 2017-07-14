//
// Created by Administrator on 2017/7/10.
//

#include "HtmlFinder.h"

HtmlFinder::HtmlFinder(QString string) {
    this->text = string;

    this->document.setContent(this->text);
    this->parse();
}

HtmlFinder::~HtmlFinder() {

}

HtmlFinder HtmlFinder::finder(QString path) {

}

QString HtmlFinder::getText() {
    return this->text;
}

void HtmlFinder::parse() {
    QDomElement root = document.documentElement();
    QDomNode node = root.firstChild();

}