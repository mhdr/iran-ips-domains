from tld import get_tld
import ipaddress


def nekoray_domains(data: list):
    output = ""
    data_set = set()

    for d in data:

        dd = d.strip()

        if "_" in dd:
            continue

        if not dd.isascii():
            continue

        res = get_tld(dd, as_object=True, fix_protocol=True, fail_silently=True)

        if res is not None:
            data_set.add(res.fld)

    sorted_data = sorted(data_set)
    for d in sorted_data:
        output += "domain:{0}\n".format(d)

    output = output.rstrip("\n")
    return output


def nekoray_ips(data: list):
    output = ""
    sorted_data = sorted(data)
    for d in sorted_data:
        dd = d.strip()
        output += "{0}\n".format(dd)

    output = output.rstrip("\n")
    return output


def v2rayN_domains(data: list):
    output = ""
    data_set = set()

    for d in data:

        dd = d.strip()

        if "_" in dd:
            continue

        if not dd.isascii():
            continue

        res = get_tld(dd, as_object=True, fix_protocol=True, fail_silently=True)

        if res is not None:
            data_set.add(res.fld)

    sorted_data = sorted(data_set)
    for d in sorted_data:
        output += "domain:{0},\n".format(d)

    output = output.rstrip(",\n")
    return output


def v2rayN_ips(data: list, data2: list):
    output = ""
    data_all = data + data2

    sorted_data = sorted(list(set(data_all)))
    for d in sorted_data:
        dd = d.strip()
        output += "{0},\n".format(dd)

    output = output.rstrip(",\n")
    return output


def proxifier_domains(data: list):
    output_list = []
    output = ""
    data_set = set()

    for d in data:

        dd = d.strip()

        if "_" in dd:
            continue

        if not dd.isascii():
            continue

        res = get_tld(dd, as_object=True, fix_protocol=True, fail_silently=True)

        if res is not None:
            data_set.add(res.fld)

    sorted_data = sorted(data_set)
    for d in sorted_data:
        new = "*.{0};".format(d)
        if len(output) + len(new) >= 32768:
            output_list.append(output)
            output = ""

        output += new

    if len(output) > 0:
        output_list.append(output)

    return output_list


def proxifier_ips(data: list):
    output_list = []
    output = ""
    sorted_data = sorted(data)
    for d in sorted_data:
        dd = d.strip()
        net = ipaddress.ip_network(dd)
        ip_range = "{0}-{1}".format(net[0], net[-1])
        new = "{0};".format(ip_range)
        if len(output) + len(new) >= 32768:
            output_list.append(output)
            output = ""

        output += new

    if len(output) > 0:
        output_list.append(output)

    return output_list
