import os
from pathlib import Path
import lib

# create output directory if required
output_dir = "output"
parent_dir = Path(__file__).parent

if not os.path.exists(output_dir):
    os.mkdir(output_dir)
else:
    for f in os.listdir(output_dir):
        os.remove(os.path.join(output_dir, f))

########################################### nekoray domains ############################################################

file_input = open("ito.txt", 'r')
lines = file_input.readlines()
result = lib.nekoray_domains(lines)
file_output = open(parent_dir / "{0}/nekoray_domains.txt".format(output_dir), 'w')
file_output.write(result)
file_output.close()

########################################### nekoray ips ################################################################


file_input = open("ripe.txt", 'r')
lines = file_input.readlines()
result = lib.nekoray_ips(lines)
file_output = open(parent_dir / "{0}/nekoray_ips.txt".format(output_dir), 'w')
file_output.write(result)
file_output.close()

########################################### v2rayN domains #############################################################

file_input = open("ito.txt", 'r')
lines = file_input.readlines()
result = lib.v2rayN_domains(lines)
file_output = open(parent_dir / "{0}/v2rayN_domains.txt".format(output_dir), 'w')
file_output.write(result)
file_output.close()

########################################### v2rayN ips #################################################################


file_input = open("ripe.txt", 'r')
lines = file_input.readlines()

result = lib.v2rayN_ips(lines)

file_output = open(parent_dir / "{0}/v2rayN_ips.txt".format(output_dir), 'w')
file_output.write(result)
file_output.close()

########################################### Proxifier domains ##########################################################

file_input = open("ito.txt", 'r')
lines = file_input.readlines()
result = lib.proxifier_domains(lines)
file_index = 1
for r in result:
    file_output = open(parent_dir / "{0}/proxifier_domains{1}.txt".format(output_dir, file_index), 'w')
    file_output.write(r)
    file_output.close()
    file_index += 1

########################################### Proxifier ips ##############################################################


file_input = open("ripe.txt", 'r')
lines = file_input.readlines()
result = lib.proxifier_ips(lines)
file_index = 1
for r in result:
    file_output = open(parent_dir / "{0}/proxifier_ips_part{1}.txt".format(output_dir, file_index), 'w')
    file_output.write(r)
    file_output.close()
    file_index += 1
