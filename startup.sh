#! /bin/bash
#
locust="/home/debian/lushu/stress/bin/locust"
work_dir="/home/debian/lushu/stress/src"
host="http://192.168.2.114:8000"

usage ()
{ 
    echo "Usage: $0 [--stop] [--master|--slave] [--master-host=master-host] [--slave-count=count]" 2>&1;
    exit 1;
}

master_host="127.0.0.1"
mode=""
slave_count=1

while :; do
    case $1 in
        --stop)
            echo "stop locust"
            ps -ef |grep "${locust}"|grep -v grep |awk ' {print $2} '|xargs kill -9
            exit 1;
            ;;
        --master)
            mode="master"
            ;;
        --slave)
            mode="slave"
            ;;
        --master-host=?*)
            master_host=${1#*=}
            ;;
        --slave-count=?*)
            slave_count=${1#*=}
            ;;
        -?*)
            usage
            ;;
        *)
            break
    esac

    shift
done

cd ${work_dir}

echo "start ${mode}"

if [ $mode == "master" ]
then
    nohup ${locust} --master --host=${host} >/dev/null 2>&1 &
elif [ $mode == "slave" ]
then
    for ((loop=0; loop < ${slave_count}; loop++))
    do
        nohup ${locust} --host=${host} --slave --master-host=${master_host} --logfile=locust.log >/dev/null 2>&1 &
    done
else
    nohup ${locust} --host=${host} &
fi
