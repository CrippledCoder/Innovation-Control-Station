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
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_InnovationControlStationClass
{
public:
    QWidget *centralWidget;
    QWidget *verticalLayoutWidget;
    QVBoxLayout *verticalLayout;
    QSpacerItem *verticalSpacer;
    QVBoxLayout *verticalLayout_2;
    QHBoxLayout *horizontalLayout;
    QSpacerItem *horizontalSpacer_3;
    QLabel *label_2;
    QLineEdit *UserText;
    QSpacerItem *horizontalSpacer_4;
    QHBoxLayout *horizontalLayout_3;
    QSpacerItem *horizontalSpacer;
    QLabel *label;
    QLineEdit *PassText;
    QSpacerItem *horizontalSpacer_2;
    QHBoxLayout *horizontalLayout_2;
    QSpacerItem *horizontalSpacer_5;
    QPushButton *TryLogin;
    QPushButton *CloseLogin;
    QSpacerItem *horizontalSpacer_6;
    QSpacerItem *verticalSpacer_2;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *InnovationControlStationClass)
    {
        if (InnovationControlStationClass->objectName().isEmpty())
            InnovationControlStationClass->setObjectName(QString::fromUtf8("InnovationControlStationClass"));
        InnovationControlStationClass->resize(1085, 792);
        centralWidget = new QWidget(InnovationControlStationClass);
        centralWidget->setObjectName(QString::fromUtf8("centralWidget"));
        verticalLayoutWidget = new QWidget(centralWidget);
        verticalLayoutWidget->setObjectName(QString::fromUtf8("verticalLayoutWidget"));
        verticalLayoutWidget->setGeometry(QRect(0, 0, 1081, 771));
        verticalLayout = new QVBoxLayout(verticalLayoutWidget);
        verticalLayout->setSpacing(6);
        verticalLayout->setContentsMargins(11, 11, 11, 11);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        verticalLayout->setContentsMargins(0, 0, 0, 0);
        verticalSpacer = new QSpacerItem(20, 200, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout->addItem(verticalSpacer);

        verticalLayout_2 = new QVBoxLayout();
        verticalLayout_2->setSpacing(6);
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setSpacing(6);
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        horizontalSpacer_3 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout->addItem(horizontalSpacer_3);

        label_2 = new QLabel(verticalLayoutWidget);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        QSizePolicy sizePolicy(QSizePolicy::Fixed, QSizePolicy::Fixed);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(label_2->sizePolicy().hasHeightForWidth());
        label_2->setSizePolicy(sizePolicy);
        label_2->setMaximumSize(QSize(100, 100));
        QFont font;
        font.setPointSize(13);
        label_2->setFont(font);

        horizontalLayout->addWidget(label_2);

        UserText = new QLineEdit(verticalLayoutWidget);
        UserText->setObjectName(QString::fromUtf8("UserText"));

        horizontalLayout->addWidget(UserText);

        horizontalSpacer_4 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout->addItem(horizontalSpacer_4);


        verticalLayout_2->addLayout(horizontalLayout);

        horizontalLayout_3 = new QHBoxLayout();
        horizontalLayout_3->setSpacing(6);
        horizontalLayout_3->setObjectName(QString::fromUtf8("horizontalLayout_3"));
        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_3->addItem(horizontalSpacer);

        label = new QLabel(verticalLayoutWidget);
        label->setObjectName(QString::fromUtf8("label"));
        sizePolicy.setHeightForWidth(label->sizePolicy().hasHeightForWidth());
        label->setSizePolicy(sizePolicy);
        label->setMaximumSize(QSize(100, 100));
        label->setFont(font);

        horizontalLayout_3->addWidget(label);

        PassText = new QLineEdit(verticalLayoutWidget);
        PassText->setObjectName(QString::fromUtf8("PassText"));

        horizontalLayout_3->addWidget(PassText);

        horizontalSpacer_2 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_3->addItem(horizontalSpacer_2);


        verticalLayout_2->addLayout(horizontalLayout_3);


        verticalLayout->addLayout(verticalLayout_2);

        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setSpacing(6);
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        horizontalLayout_2->setSizeConstraint(QLayout::SetDefaultConstraint);
        horizontalSpacer_5 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_2->addItem(horizontalSpacer_5);

        TryLogin = new QPushButton(verticalLayoutWidget);
        TryLogin->setObjectName(QString::fromUtf8("TryLogin"));
        QSizePolicy sizePolicy1(QSizePolicy::Fixed, QSizePolicy::Fixed);
        sizePolicy1.setHorizontalStretch(50);
        sizePolicy1.setVerticalStretch(30);
        sizePolicy1.setHeightForWidth(TryLogin->sizePolicy().hasHeightForWidth());
        TryLogin->setSizePolicy(sizePolicy1);
        TryLogin->setMinimumSize(QSize(100, 30));
        QPalette palette;
        QBrush brush(QColor(197, 255, 194, 255));
        brush.setStyle(Qt::SolidPattern);
        palette.setBrush(QPalette::Active, QPalette::Button, brush);
        palette.setBrush(QPalette::Inactive, QPalette::Button, brush);
        palette.setBrush(QPalette::Disabled, QPalette::Button, brush);
        TryLogin->setPalette(palette);
        TryLogin->setFont(font);

        horizontalLayout_2->addWidget(TryLogin);

        CloseLogin = new QPushButton(verticalLayoutWidget);
        CloseLogin->setObjectName(QString::fromUtf8("CloseLogin"));
        QSizePolicy sizePolicy2(QSizePolicy::Fixed, QSizePolicy::Fixed);
        sizePolicy2.setHorizontalStretch(50);
        sizePolicy2.setVerticalStretch(50);
        sizePolicy2.setHeightForWidth(CloseLogin->sizePolicy().hasHeightForWidth());
        CloseLogin->setSizePolicy(sizePolicy2);
        CloseLogin->setMinimumSize(QSize(100, 30));
        CloseLogin->setFont(font);

        horizontalLayout_2->addWidget(CloseLogin);

        horizontalSpacer_6 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_2->addItem(horizontalSpacer_6);


        verticalLayout->addLayout(horizontalLayout_2);

        verticalSpacer_2 = new QSpacerItem(20, 200, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout->addItem(verticalSpacer_2);

        InnovationControlStationClass->setCentralWidget(centralWidget);
        statusBar = new QStatusBar(InnovationControlStationClass);
        statusBar->setObjectName(QString::fromUtf8("statusBar"));
        InnovationControlStationClass->setStatusBar(statusBar);

        retranslateUi(InnovationControlStationClass);

        QMetaObject::connectSlotsByName(InnovationControlStationClass);
    } // setupUi

    void retranslateUi(QMainWindow *InnovationControlStationClass)
    {
        InnovationControlStationClass->setWindowTitle(QApplication::translate("InnovationControlStationClass", "InnovationControlStation", nullptr));
        label_2->setText(QApplication::translate("InnovationControlStationClass", "Username:", nullptr));
        label->setText(QApplication::translate("InnovationControlStationClass", "Password:", nullptr));
        TryLogin->setText(QApplication::translate("InnovationControlStationClass", "Login", nullptr));
        CloseLogin->setText(QApplication::translate("InnovationControlStationClass", "Close", nullptr));
    } // retranslateUi

};

namespace Ui {
    class InnovationControlStationClass: public Ui_InnovationControlStationClass {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_INNOVATIONCONTROLSTATION_H
