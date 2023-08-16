
i=0

while true; do

  echo "test4.counter.any" $i $(date +%s) | nc -N localhost 2003
  echo -n "."

  echo "test4.counter.avg" $i $(date +%s) | nc -N localhost 2003
  echo -n "."

  echo "test4.counter.max" $i $(date +%s) | nc -N localhost 2003
  echo -n "."
  
  echo "test4.counter.min" $i $(date +%s) | nc -N localhost 2003
  echo -n "."
  
  echo "test4.counter.miss" $i $(date +%s) | nc -N localhost 2003
  echo -n "."

  echo "test4.counter.sum" $i $(date +%s) | nc -N localhost 2003
  echo -n "."

  sleep 60
  let "i=i+1"
  echo -n "-"
done
