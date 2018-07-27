root@openstack:~/python/install_tomcat# cat depoly_tomcat.py 
#!/bin/env python3

import os
import tarfile
import shutil
import subprocess

def unpackage_tomcat(package,package_dir):
    '''
    :param package:unzip package
    :param package_dir:unzip dir
    :return: unzip and get file
    '''
    print('package',package)
    print('package_dir',package_dir)
    #Remove the extension
    unpackage_dir = os.path.splitext(package)[0]
    unpackage_dir = os.path.splitext(unpackage_dir)[0]
    print(unpackage_dir)
    if os.path.exists(unpackage_dir):
        shutil.rmtree(unpackage_dir)

    if os.path.exists(package_dir):
        shutil.rmtree(package_dir)

    t = tarfile.open(package,'r:gz')
    t.extractall('.')

    shutil.move(unpackage_dir,package_dir)

def create_datadir(data_dir):
    if os.path.exists(data_dir):
        shutil.rmtree(data_dir)
    os.mkdir(data_dir)

def execute_cmd(cmd):
    p = subprocess.Popen(cmd,
                         shell=True,
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    if p.returncode != 0:
        return p.returncode, stderr
    return p.returncode, stdout

def format_tomcat_command(package_dir, data_dir, logfile):
    tomcat = os.path.join(package_dir, 'bin', 'startup.sh')
    tomcat_format = "{0} {1}"
    return tomcat_format.format('sh',tomcat)

def start_tomcat(cmd):
    returncode, out = execute_cmd(cmd)
    if returncode != 0:
        raise SystemExit('execute {0} error :{1}'.format(cmd, out))
    else:
        print("execute command ({0}) successful".format(cmd))


def main():
    package = 'apache-tomcat-8.0.9.tar.gz'
    cur_dir = os.path.abspath('.')
    package_dir = os.path.join(cur_dir,'tomcat')
    data_dir = os.path.join(cur_dir,'tomcat_data')
    logfile = os.path.join(data_dir,'tomcat.log')
    #To determine whether a package
    if not os.path.exists(package):
        raise SystemExit("{0} not found".format(package))

    #unpackage_tomcat(package,package_dir)
    #create_datadir(data_dir)
    start_tomcat(format_tomcat_command(package_dir,data_dir,logfile))

if __name__ == '__main__':
    main()
