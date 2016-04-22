import ConfigParser
import paramiko


# ===============test remote file=================
# cf = ConfigParser.ConfigParser()
# cf.optionxform = str
# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect('qa-systest-51.sv.splunk.com', username='eserv', password='eserv')
# sftp = ssh.open_sftp()
# f = sftp.file('/export/home/clustering/splunk_windows/splunk/etc/system/default/savedsearches.conf', 'r')
# print 'file name is:' + f.name
#
# cf.readfp(f)
# print(cf.sections())
# cf.add_section('Test')
# cf.set('Test', 'Asd', '123')
# cf.write(f)
# f.close()
# ssh.close()

# ===============test local file=================
cf2 = ConfigParser.ConfigParser()
cf2.optionxform = str
f = open('/Users/CYu/Code/other code/test.conf', 'r')
cf2.readfp(f)
print(cf2.sections())
# print(cf2.items('TEST'))
cf2.add_section('TEST')
cf2.items('TEST')
# cf2.set('TEST', 'AAA', 'aAa')
cf2.write(open('/Users/CYu/Code/other code/test.conf', 'w'))
