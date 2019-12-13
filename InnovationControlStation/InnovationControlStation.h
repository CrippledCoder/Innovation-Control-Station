#pragma once

#include <QtWidgets/QMainWindow>
#include "ui_InnovationControlStation.h"

class InnovationControlStation : public QMainWindow
{
	Q_OBJECT

public:
	InnovationControlStation(QWidget *parent = Q_NULLPTR);

private:
	Ui::InnovationControlStationClass ui;
};
