module service
{
	//服务状态: 未知、初始化中、正常服务中、长时间未响应、已经停服
	enum    ServerStatus { ssNone=0, ssIniting, ssServicing, ssNoReplay, ssStop };
        
        struct ServerReportProfile
        {            
            string          name;               //服务名称
            string          address;            //服务地址 ip+port
            string          interfaceAddress;   //服务能力地址
            ServerStatus     status;             //服务状态
            int             currentQueneSize;   //服务主队列队列长度, 不存在填0
            int             currentListSize;    //服务主序列容器长度, 不存在填0
            int             currentMapSize;     //服务主关联容器长度, 不存在填0
        };
        		
	interface ReportStatus
	{
		idempotent void report(ServerReportProfile srp );	//主动报告自己状态
	};
}
