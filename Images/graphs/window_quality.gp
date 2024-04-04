base_path = 'data/'

set terminal eps enhanced color
set key box top left inside Left samplen 1
set xtics autofreq 1
set yrange [0.7:1]
set ytics 0.02
set size 1,1
set origin 0,0

set ylabel "Metric Value"
set xlabel "Number Of Services"

# Optional: Uncomment for multiplot layout
# set multiplot layout 2,3 rowsfirst scale 1.1,0.9

do for [i=3:7] {
  set output sprintf('quality_plot_bad_n%d.eps', i)
  set label sprintf("%d Nodes", i) at graph 0.5, graph -0.3 center
set yrange [0.7:1]
set ytics 0.02
  plot for [j=1:i] base_path.sprintf('window_quality_performance_pippo.mytable_gamma_bad_n%d_w%d.dat', i, j) using 1:(1-$2) title sprintf('W Size %d', j) with linespoints pointtype (j)
  set output sprintf('quality_plot_bad_percentage_n%d.eps', i)
  set yrange [0:1]
set ytics autofreq
  plot for [j=1:i] base_path.sprintf('window_quality_performance_pippo.mytable_gamma_bad_n%d_w%d.dat', i, j) using 1:3 title sprintf('W Size %d', j) with linespoints pointtype (j)

  unset label
  set output
}

# Optional: Uncomment if using multiplot
# unset multiplot
