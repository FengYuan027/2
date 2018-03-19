#!/usr/bin/python

IPERF_PATH = 'iperf'
IPERF_PORT = 5001
IPERF_SERVER_DIRECTORY = '~/IperfServer'
IPERF_CLIENT_DIRECTORY = '~/IperfClient'
IPERF_CLIENT_T = 20

def SingleHostIperfTest(net)

    hostName = 'h1'
	
	host = net.getHostByName(hostName)
	
	host.sendCmd('%s -s -p %s > %s/iperf_server_%s_single.txt &' %(IPERF_PATH, IPERF_PORT, IPERF_SERVER_DIRECTORY, hostName))
	
	clientNames = []
	
	for i in range(2, 100, 2)
	
	    clientNames.append('h%s' %i)
		
    BeginIperfTest(net, hostName, clientNames)
	
	host.cmd('kill $!')
	
def TwoHostIperfTest(net)

    hostName1 = 'h1'
	
	hostName2 = 'h100'
	
	host1 = net.getHostByName(hostName1)
	
	host1.sendCmd('%s -s -p %s > %s/iperf_server_%s_two.txt &' %(IPERF_PATH, IPERF_PORT, IPERF_SERVER_DIRECTORY, hostName1))
	
	host2 = net.getHostByName(hostName2)
	
	host2.sendCmd('%s -s -p %s > %s/iperf_server_%s_two.txt &' %(IPERF_PATH, IPERF_PORT, IPERF_SERVER_DIRECTORY, hostName2))
	
	clientNames1 = []
	
	clientNames2 = []
	
	for i in range(3, 99, 2)
	
	    clientNames1.append('h%s' %i)
		
		clientNames2.append('h%s' %i-1)
		
    BeginIperfTest(net, hostName1, clientNames1)
	
	BeginIperfTest(net, hostName2, clientNames2)
	
	host1.cmd('kill $!')
	
	host2.cmd('kill $!')


def BeginIperfTest(net, hostName, clientNames)

    host = net.getHostByName(hostName)
	
	host.sendCmd('%s -s -p %s > %s/iperf_server_%s.txt &' %(IPERF_PATH, IPERF_PORT, IPERF_SERVER_DIRECTORY, hostName))
	
	for clientName in clientNames

	    client = net.getHostByName(clientName)
		
		h.sendCmd('%s -c %s -p %s -t %d -i 1 -yc > %s/iperf_client_%s.txt &' %(IPERF_PATH, hostName, IPERF_PORT, IPERF_CLIENT_T, IPERF_CLIENT_DIRECTORY, clientName))

