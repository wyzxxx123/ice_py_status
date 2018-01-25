import Ice

Ice.loadSlice('servoStatus.ice')
Ice.updateModules()

import service

report_file = service.ServerReportProfile()
report_file.name = "test"

global server_list
server_list = {"test": report_file}