from tld import get_tld


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


def v2rayN_ips(data: list):
    output = ""
    sorted_data = sorted(data)
    for d in sorted_data:
        dd = d.strip()
        output += "{0},\n".format(dd)

    output = output.rstrip(",\n")
    return output
