from GUI.tradeBot_GUI_back import *

print('---start---\n')
app = QtWidgets.QApplication(sys.argv)
application = BackEnd()
application.show()
sys.exit(app.exec_())