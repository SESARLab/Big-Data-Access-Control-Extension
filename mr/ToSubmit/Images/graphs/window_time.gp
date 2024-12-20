base_path = 'data/'
file_base = 'window_time_performance_n7_s7_20_100'
file_base = 'window_time_performance_qualitative_n7_s7_50_80'

# set terminal png enhancedà
set terminal postscript eps color enhanced
set key box top left inside Left samplen 1 spacing 1.15
set key enhanced
set key font ",16"

set xtics autofreq 1
set ytics autofreq
# set yrange [0.85:1]

set yrange [*:150000000]
set size 1,1
set origin 0,0
set border 3
set ylabel "Execution Time (ms)"
set xlabel "Number Of Services"
set logscale y


# set grid
set tics nomirror

set tics font ",18"
#set key outside


# Optional: Uncomment for multiplot layout
# set multiplot layout 2,3 rowsfirst scale 1.1,0.9

do for [i=3:7] {

  set output sprintf('%s_n%d.eps', file_base,i)
  set label sprintf("%d Vert", i) at graph 0.5, graph -0.3 center
  # plot for [j=1:i] base_path.sprintf('%s_n%d_w%d.dat',file_base, i, j) using 1:2 title sprintf('  W Size %d', j) with linespoints pointtype (j)
    plot for [j=1:i] base_path.sprintf('%s_n%d_w%d.dat',file_base, i, j) using 1:2 \
      title (j == 1 ? 'W Size 1 - Baseline' : sprintf('W Size %d', j)) \
      with linespoints pointtype (j)
  # set output
  unset label
}



# Optional: Uncomment if using multiplot
# unset multiplot

