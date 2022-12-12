from tld import get_tld

nekoray_domains = set()
nekoray_ips = set()


def read_domains(file_name):
    file = open(file_name, 'r')

    while True:

        # Get next line from file
        line = file.readline()

        # if line is empty
        # end of file is reached
        if not line:
            break

        if "_" in line:
            continue

        d = line.strip()

        if not d.isascii():
            continue

        print(d)
        res = get_tld(d, as_object=True, fix_protocol=True, fail_silently=True)
        if res is not None:
            out = "domain:{0}\n".format(res.fld)
            nekoray_domains.add(out)

    file.close()


def read_ips(file_name):
    file = open(file_name, 'r')

    while True:

        # Get next line from file
        line = file.readline()

        # if line is empty
        # end of file is reached
        if not line:
            break

        if "_" in line:
            continue

        d = line.strip()
        print(d)
        out = "{0}\n".format(d)
        nekoray_ips.add(out)

    file.close()


read_domains("ito.txt")
# read_domains("my-domains.txt")

file_output = open('nekoray_domains.txt', 'w')
file_output.writelines(nekoray_domains)
file_output.close()

read_ips("ripe.txt")
# read_ips("my-ips.txt")

file_output = open('nekoray_ips.txt', 'w')
file_output.writelines(nekoray_ips)
file_output.close()
