base_path = 'data/'
file_base = 'window_quality_performance_diff_qual_n7_s7_50_80'
#file_base = 'window_quality_performance_diff_qual_n7_s7_20_100'
#file_base = 'window_quality_performance_diff_perce_n7_s7_50_89'
#file_base = 'window_quality_performance_diff_perce_n7_s7_20_100'
# set terminal png enhanced
set terminal postscript eps color enhanced
set key box top left inside Left samplen 1
set xtics autofreq 1 font ",20"
set ytics autofreq 0.04 font ",20"
set yrange [0.84:1]
#set ytics 0.02
set size 1,1
set origin 0,0
set border 3
set ylabel "Metric Value" font ",22"
set xlabel "Number Of Services" font ",22"
# set grid
set tics nomirror
set key bottom right
set key enhanced
#set key outside


# Optional: Uncomment for multiplot layout
# set multiplot layout 2,3 rowsfirst scale 1.1,0.9

do for [i=3:7] {
  set output sprintf('%s_n%d.eps', file_base,i)
  set label sprintf("%d Vert", i) at graph 0.5, graph -0.3 center
  plot for [j=1:i] base_path.sprintf('%s_n%d_w%d.dat',file_base, i, j) using 1:2 title sprintf('  W Size %d', j) with linespoints pointtype (j)
  set output
  unset label
}

# Optional: Uncomment if using multiplot
# unset multiplot

