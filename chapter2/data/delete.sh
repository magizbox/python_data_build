max=2015
for i in `seq 1880 $max`
do
  s="yob$i.txt"
  rm -rf $s
  echo "delete $s"
done

