# uncompyle6 version 2.11.3
# Python bytecode 3.5 (3350)
# Decompiled from: Python 3.5.2 |Anaconda 4.1.1 (64-bit)| (default, Jul  5 2016, 11:41:13) [MSC v.1900 64 bit (AMD64)]
# Embedded file name: StatisticsReporter.py
import paramiko
import base64
import os
import getpass
import sys
from datetime import datetime
from datetime import timedelta
from operator import itemgetter
import collections
from itertools import groupby
from tkinter import *
import tkinter as tk
import tkinter.scrolledtext as tkst

def __init__(self, parent):
    self.output = Text(self)
    self.output.pack()
    sys.stdout = self
    self.pack()


def is_empty(any_structure):
    if any_structure:
        return False
    return True


def printTable(myDict, colList=None):
    print('started')
    if not colList:
        colList = list(myDict[0].keys() if myDict else [])
    myList = [
     colList]
    for item in myDict:
        myList.append([str(item[col] or '') for col in colList])

    colSize = [max(map(len, col)) for col in zip(*)]
    myList.insert(1, ['-' * i for i in colSize])
    return myList


def serverConnectionEstablish(serverName, ssh):
    userName = 'ctmuser'
    decodedPassword = base64.b64decode(b'YzBudHJvbC1t')
    decodedPassword = decodedPassword.decode('ascii')
    try:
        ssh.connect(serverName, username=userName, password=decodedPassword)
    except paramiko.ssh_exception:
        raise Exception('Failed To login! Please check the password again')

    return ssh


def statisticsPuller(ssh, jobNameTosearchFor):
    commandToExucute = 'ctmruninf -list "*" -jobname '
    os.system('cls')
    commandToExucute = commandToExucute + '"*' + jobNameTosearchFor + '*"'
    try:
        stdin, stdout, stderr = ssh.exec_command(commandToExucute)
        myList = stdout.read().splitlines()[2:-2]
        if is_empty(myList):
            return 'No Data Found... :-('
        notFoundDataForJob = False
    except paramiko.SSHException:
        raise Exception('Failed to execute the command!')

    results = []
    for line in myList:
        line = line.decode('ascii').split()
        endDate = datetime.strptime(line[0], '%Y%m%d%H%M%S')
        runTime = round(float(line[-1]))
        delta = timedelta(seconds=runTime)
        startDate = endDate - delta
        m, s = divmod(runTime, 60)
        h, m = divmod(m, 60)
        runTime = '%d:%02d:%02d' % (h, m, s)
        jobName = line[1]
        memName = line[5]
        dict = collections.OrderedDict([
         (
          'Job Name', jobName),
         (
          'Mem Name', memName),
         (
          'Start Time', startDate),
         (
          'End Time', endDate),
         (
          'Elapsed Minutes', runTime)])
        results.append(dict)

    sortedResults = sorted(results, key=itemgetter('Job Name', 'Mem Name'))
    groups = []
    uniquekeys = []
    for k, g in groupby(sortedResults, key=itemgetter('Job Name', 'Mem Name')):
        groups.append(list(g))
        uniquekeys.append(k)

    if len(uniquekeys) > 1:
        print('There are ' + str(len(uniquekeys)) + ' Jobs :  ')
        for key in uniquekeys:
            print(key[0] + ' ||| ' + key[1])

        print('\n\n\n+++++++++++++++++++++++++++++')
    return printTable(sortedResults)


def main(serverName, jobNameTosearchFor):
    print('************************\nThis is Statistics Reporter, no need to order a job for statistics :)\n************************\n')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        sshConnection = serverConnectionEstablish(serverName, ssh)
    except:
        quit()

    try:
        return statisticsPuller(sshConnection, jobNameTosearchFor)
    except:
        quit()
# okay decompiling M:\Scripts\Python\CTM-Utils.exe_extracted\out00-PYZ.pyz_extracted\StatisticsReporter.pyc
