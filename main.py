import os
from pathlib import Path
import lib

# create output directory if required
output_dir = "output"
parent_dir = Path(__file__).parent

if not os.path.exists(output_dir):
    os.mkdir(output_dir)

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
