
set ylabel "Computation Time (ms)"
set xlabel "No. of services"

set key box top left inside Left samplen 1
#set logscale y 2
#set xrange [0:9]
#set xtics ('10' 0, '50' 1, '100' 2, '200' 3, '500' 4, '1000' 5, '2000' 6, '5000' 7, '10000' 8, '20000' 9)

plot 'exhaustive_performance.dat' u 1:2  t '2 Nodes' w lp pt 9 , 'exhaustive_performance.dat' u 1:3  t '3 Nodes' w lp pt 7, 'exhaustive_performance.dat' u 1:4  t '4 Nodes' w lp pt 6,  'exhaustive_performance.dat' u 1:5  t '5 Nodes' w lp pt 5, 'exhaustive_performance.dat' u 1:6  t '6 Nodes' w lp pt 4
set terminal postscript eps enhanced
set output 'window_performance.eps'

replot

unset output