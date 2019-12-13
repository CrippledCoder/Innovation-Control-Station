#include "InnovationControlStation.h"
#include <QtWidgets/QApplication>

int main(int argc, char *argv[])
{
	QApplication a(argc, argv);
	InnovationControlStation w;
	w.show();
	return a.exec();
}
