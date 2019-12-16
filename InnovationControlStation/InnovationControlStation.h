#pragma once

#include <QtWidgets/QMainWindow>
#include "ui_InnovationControlStation.h"

class InnovationControlStation : public QMainWindow
{
	Q_OBJECT

public:
	InnovationControlStation(QWidget *parent = Q_NULLPTR);
private slots:
	void test();
private:
	Ui::InnovationControlStationClass ui;
	QPushButton *LoginButton;
	QPushButton *CloseButton;
};

