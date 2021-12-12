# You live 4 miles from university. The bus drives at 25mph but spends 2 minutes at each
#
# of the 10 stops on the way. How long will the bus journey take? Alternatively, you could
#
# run to university. You jog the first mile at 7mph; then run the next two at15mph; before
#
# jogging the last at 7mph again. Will this be quicker or slower than the bus?

  Distance=4
  speed = 25
  T1 = ((Distance/speed)*60)
  #since the bus spend two mins and each ten steps , so 2*10
  T2 = 20
  total = T1 = T2
  print("total time taken by bus is {}").format(total)
  j1 = (1/7*60)
  j2 = (1/15*60)
  j3 = (1/7*60)
  Total = j1+j2+j3
  print("the total jogging time").format(Total)
  if total>Total:
      print("jogging is slower than bus")
  else:
      print("jogging is faster than bus")
