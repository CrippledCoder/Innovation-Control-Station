/********************************************************************************
** Form generated from reading UI file 'InnovationControlStation.ui'
**
** Created by: Qt User Interface Compiler version 5.12.6
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_INNOVATIONCONTROLSTATION_H
#define UI_INNOVATIONCONTROLSTATION_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_InnovationControlStationClass
{
public:
    QWidget *centralWidget;
    QPushButton *pushButton;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *InnovationControlStationClass)
    {
        if (InnovationControlStationClass->objectName().isEmpty())
            InnovationControlStationClass->setObjectName(QString::fromUtf8("InnovationControlStationClass"));
        InnovationControlStationClass->resize(600, 400);
        centralWidget = new QWidget(InnovationControlStationClass);
        centralWidget->setObjectName(QString::fromUtf8("centralWidget"));
        pushButton = new QPushButton(centralWidget);
        pushButton->setObjectName(QString::fromUtf8("pushButton"));
        pushButton->setGeometry(QRect(230, 220, 80, 22));
        InnovationControlStationClass->setCentralWidget(centralWidget);
        mainToolBar = new QToolBar(InnovationControlStationClass);
        mainToolBar->setObjectName(QString::fromUtf8("mainToolBar"));
        InnovationControlStationClass->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(InnovationControlStationClass);
        statusBar->setObjectName(QString::fromUtf8("statusBar"));
        InnovationControlStationClass->setStatusBar(statusBar);

        retranslateUi(InnovationControlStationClass);

        QMetaObject::connectSlotsByName(InnovationControlStationClass);
    } // setupUi

    void retranslateUi(QMainWindow *InnovationControlStationClass)
    {
        InnovationControlStationClass->setWindowTitle(QApplication::translate("InnovationControlStationClass", "InnovationControlStation", nullptr));
        pushButton->setText(QApplication::translate("InnovationControlStationClass", "PushButton", nullptr));
    } // retranslateUi

};

namespace Ui {
    class InnovationControlStationClass: public Ui_InnovationControlStationClass {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_INNOVATIONCONTROLSTATION_H
