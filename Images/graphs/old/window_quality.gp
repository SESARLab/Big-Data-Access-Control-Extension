base_path = 'data/'
file_base = 'window_quality_performance_n7_s9_50_89'
set terminal png enhanced
set key box top left inside Left samplen 1
set xtics autofreq 1
# set yrange [0.85:1]
set ytics 0.02
set size 1,1
set origin 0,0

set ylabel "Metric Value"
set xlabel "Number Of Services"

# Optional: Uncomment for multiplot layout
# set multiplot layout 2,3 rowsfirst scale 1.1,0.9

do for [i=3:7] {
  set output sprintf('%s_n%d.png', file_base,i)
  set label sprintf("%d Vert", i) at graph 0.5, graph -0.3 center
  plot for [j=1:i] base_path.sprintf('%s_n%d_w%d.dat',file_base, i, j) using 1:2 title sprintf('W Size %d', j) with linespoints pointtype (j)

  unset label
  set output
}

# Optional: Uncomment if using multiplot
# unset multiplot
