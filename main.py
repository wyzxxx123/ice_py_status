#!/usr/bin/env python
# **********************************************************************
#
# Copyright (c) 2003-2017 ZeroC, Inc. All rights reserved.
#
# **********************************************************************

from sys import argv
from global_var import server_list
from http_server import RequestThread
import Ice
from IcePy import TCPConnectionInfo

Ice.loadSlice('servoStatus.ice')
Ice.updateModules()

import service

request = RequestThread()
request.start()


class ReportStatusI(service.ReportStatus):
    def report(self, srp, current=None):
        ci = current.con.getInfo()
        ip_address = ""
        if isinstance(ci, TCPConnectionInfo):
            ip_address = str(ci.remoteAddress) + ":" + str(ci.remotePort)

        srp.address = ip_address
        server_list[srp.name] = srp
        print("Hello World!", server_list)


with Ice.initialize(argv) as communicator:
    adapter = communicator.createObjectAdapterWithEndpoints("ReportStatus", "default -h localhost -p 10400")
    adapter.add(ReportStatusI(), Ice.stringToIdentity("svrStatus"))
    adapter.activate()
    communicator.waitForShutdown()


# class Server(Ice.Application):
#     def run(self, args):
#         if len(args) > 1:
#             print(self.appName() + ": too many arguments")
#             return 1
#
#         adapter = self.communicator().createObjectAdapter("ReportStatus")
#         adapter.add(ReportStatusI(), Ice.stringToIdentity("reportStatus"))
#         adapter.activate()
#         self.communicator().waitForShutdown()
#
#         return 0

# stdout.flush()
# app = Server()
# exit(app.main(argv, "config.server"))





# request_server.run()





