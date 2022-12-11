from tld import get_tld

domains = set()
ips = set()


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
            domains.add(out)

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
        ips.add(out)

    file.close()


read_domains("domains.txt")
read_domains("ito.txt")
read_domains("my-domains.txt")

file_output = open('iran_domains.txt', 'w')
file_output.writelines(domains)
file_output.close()

read_ips("firewall.txt")
read_ips("my-ips.txt")

file_output = open('iran_ips.txt', 'w')
file_output.writelines(ips)
file_output.close()
