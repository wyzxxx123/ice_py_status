import sys, traceback, Ice

Ice.loadSlice('servoStatus.ice')
import service


with Ice.initialize(sys.argv) as communicator:
    hello = service.ReportStatusPrx.checkedCast(
        communicator.stringToProxy('svrStatus:default -h localhost -p 10400'))

    report_file = service.ServerReportProfile()
    report_file.name = "aa"
    hello.report(report_file)

#
# def run(communicator):
#
#     proxy = service.ReportStatusPrx.checkedCast(
#         communicator.stringToProxy('reportStatus:default -h localhost -p 20001'))
#
#     if not proxy:
#         print(args[0] + ": invalid proxy")
#         return 1
#
#     t_struct = service.ServerReportProfile()
#     t_struct.name = "aa";
#
#     proxy.report(t_struct);
#
#
# status = 0
# with Ice.initialize(sys.argv, "config.client") as communicator:
#     if len(sys.argv) > 1:
#         print(sys.argv[0] + ": too many arguments")
#         status = 1
#     else:
#         status = run(communicator)
#
#
# sys.exit(status)
