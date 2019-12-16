#include "InnovationControlStation.h"
#include <iostream>
using namespace std;

InnovationControlStation::InnovationControlStation(QWidget *parent)
	: QMainWindow(parent)
{
	ui.setupUi(this);
	CloseButton = ui.CloseLogin;
	QObject::connect(CloseButton, SIGNAL(clicked()), this, SLOT(close()));

	LoginButton = ui.TryLogin;
	
	QObject::connect(LoginButton, SIGNAL(clicked()), this, SLOT(test()));
}

void InnovationControlStation::test()
{
	ui.PassText->setText(ui.UserText->text());
}