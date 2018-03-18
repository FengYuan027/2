#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel


class MyTopo(Topo):
    "Homework topology"

    def __init__(self):

        Topo.__init__(self)

        self.totalCost = 0
        self.hostId = 1
        self.switchId = 1

        self.addTierThreeSwitches(100, 2)
        #self.addTierTwoSwitches(2)

        print "Total cost: %s" % self.totalCost


    def addTierThreeSwitches(self, numberOfNodes, numberOfPartition):

        tier2switches = []
        tier3switches = []

        for i in range(numberOfPartition):

            tier2switch = self.addTierTwoSwitches(numberOfNodes/numberOfPartition)
            tier2switches.append(tier2switch)

        for i in range(0, len(tier2switches), 2):
            
            if (i + 1 == len(tier2switches)):
                tier3switches.append(tier2switches[i])
            else:
                tier3switch = self.addSwitchWithCost()
                self.addTopLink(tier2switches[i], tier3switch)
                self.addTopLink(tier2switches[i+1], tier3switch)
                tier3switches.append(tier3switch)

        for i in range(1, len(tier3switches)):

            self.addTopLink(tier3switches[i-1], tier3switches[i])



    def addTierTwoSwitches(self, numberOfNodes):

        tier2switch1 = self.addSwitchWithCost()
        
        tier1switch1 = self.addTierOneSwitch(numberOfNodes/2)
        tier1switch2 = self.addTierOneSwitch(numberOfNodes/2)

        self.addSwitchToSwitchLink(tier2switch1, tier1switch1)
        self.addSwitchToSwitchLink(tier2switch1, tier1switch2)

        return tier2switch1


    def addTierOneSwitch(self, numberOfNodes):

        switch = self.addSwitchWithCost()

        self.addHostGroup(numberOfNodes, switch)

        return switch


    def addHostGroup(self, numberOfNodes, switch):

        for i in range(numberOfNodes):

            host = self.addHostWithId()

            self.addHostToSwitchLink(host, switch)


    def addTopLink(self, switch1, switch2):

        self.addHundredMLink(switch1, switch2)


    def addSwitchToSwitchLink(self, switch1, switch2):

        self.addHundredMLink(switch1, switch2)


    def addHostToSwitchLink(self, host, switch):

        self.addHundredMLink(host, switch)


    def addHostWithId(self):

        host = self.addHost('h%s' % self.hostId)

        self.hostId+=1

        return host


    def addSwitchWithCost(self):

        self.totalCost += 300

        switch = self.addSwitch('s%s' % self.switchId)

        self.switchId+=1

        return switch


    def addTenGLink(self, node1, node2):

        self.totalCost += 200

        self.addLink(node1, node2, **dict(bw=100))


    def addOneGLink(self, node1, node2):

        self.totalCost += 15

        self.addLink(node1, node2, **dict(bw=100))


    def addHundredMLink(self, node1, node2):

        self.totalCost += 1

        self.addLink(node1, node2, bw=100)


topos = { 'mytopo': ( lambda: MyTopo() ) }
