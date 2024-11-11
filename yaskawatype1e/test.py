from type1e import Type1E


def Type1E_test(plctype, ip_master, port_master, ip_plc, port_plc):
    pyplc = Type1E(plctype)
    pyplc.connect(ip_master, port_master, ip_plc, port_plc)

    # # check batch access to word units
    # pyplc.batchwrite_wordunits("D0000", [0, 0])
    value = pyplc.batchread_wordunits("D0000", 255)
    print(f"Response - [{len(value)}] data: {value}")

    # # check batch access to bit units
    # # odd size test
    # pyplc.batchwrite_bitunits("M220", [0])
    # value = pyplc.batchread_bitunits("M220", 1)
    # print(value)

    # # even size test
    # pyplc.batchwrite_bitunits("M220", [0, 0, 0, 0])
    # value = pyplc.batchread_bitunits("M220", 4)
    # print(value)

    # test random bit access
    # pyplc.randomwrite_bitunits(["M220", "M225", "M230"], [1, 1, 1])
    # pyplc.randomwrite_wordunits(["D0000", "D0004"], [0, 0])
    # value = pyplc.batchread_wordunits("D0000", 6)
    # print(value)
    # pyplc.remote_stop()
    # pyplc.remote_run()


if __name__ == "__main__":
    plctype, ip_master, port_master, ip_plc, port_plc = [
        "F",
        "192.168.1.30",
        8011,
        "192.168.1.1",
        8010,
    ]
    Type1E_test(plctype, ip_master, port_master, ip_plc, port_plc)
