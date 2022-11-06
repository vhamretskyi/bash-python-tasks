#!/bin/bash

data_time=`date`
echo "current date and time: $data_time"

username=`whoami`
echo "name of current user: $username"

intip=`ifconfig | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1'`
echo "iternal IP address and hostname: $intip, `hostname`"

extip=`dig +short myip.opendns.com @resolver1.opendns.com`
echo "externam IP address: $extip"

linuxdistr=`uname -rs`
echo "name and version of Linux distribution: $linuxdistr "

systuptime=`uptime`
echo "$system uptime: $systuptime"

used=`df -h| grep /dev/disk1s5s1`
echo "information about used and free space in / in GB: $used"

totram=`system_profiler SPHardwareDataType | grep "Memory:"`
freeram=`top -l 1 -s 0 | grep PhysMem`
echo "information about total RAM: $totram"
echo "information about free RAM: $freeram"

cpucores=`sysctl -n hw.ncpu`
cpufreq=`sysctl hw.cpufrequency`
echo "number of CPU cores: $cpucores"
echo "frequency of CPU core: $cpufreq Hz"


