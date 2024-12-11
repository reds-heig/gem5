from m5.defines import buildEnv
from m5.objects.ClockedObject import ClockedObject
from m5.params import *
from m5.proxy import *
from m5.SimObject import SimObject


class PCIELink(ClockedObject):
    type = "PCIELink"
    cxx_header = "mem/pcie_link.hh"
    cxx_class = "gem5::PCIELink"

    upstreamSlave = SlavePort("upstream slaveport")
    downstreamMaster = MasterPort("downstream masterport for pio requests")
    upstreamMaster = MasterPort("upstream master port for dma requests")
    downstreamSlave = SlavePort("downstream slave port")

    delay = Param.Latency("0us", "packet transmit delay")
    delay_var = Param.Latency("0ns", "packet transmit delay variability")

    # Gen 3 link speed:
    #  Gen 1 2.5 Gbps
    #  Gen 2 5 Gbps
    #  Gen 3 8 Gbps
    # Gen 3 uses 128B/130B encoding so effective speed = 985 MBPS
    speed = Param.NetworkBandwidth("2.5Gbps", "link speed")

    mps = Param.Int("64", "Max Payload Size in Bytes")
    max_queue_size = Param.Int("4", "Size of the replay buffer")

    lanes = Param.Int("1", "Number of lanes on link")  # 1,2,4 ,8 or 16
    debug_flag = Param.Bool(False, "show the debug information")
