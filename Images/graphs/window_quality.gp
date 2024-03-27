set ylabel "Metric Value"
set xlabel "Number Of Servicess"
base_path = ''

set key box top left inside Left samplen 1
set xtics autofreq 1

set size 1,1
set origin 0,0
set multiplot layout 2,3 rowsfirst scale 1.1,0.9

do for [i=3:10] {
  set xlabel sprintf("N. of Services", i)
  set label sprintf("%d Nodes", i) at graph 0.5, graph -0.3 center
  plot for [j=1:i] base_path.sprintf('window_quality_performance_pippo.mytable_gamma_vbad_n%d_w%d.dat', i, j) u 1:2 t sprintf('W Size %d', j) w lp pt (j+5)
  unset label

}
unset multiplot

set terminal postscript eps enhanced
set output 'window_quality.eps'
replot

unset output