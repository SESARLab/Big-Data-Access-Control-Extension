base_path = 'data/'
file_bases = 'window_quality_performance_diff_qual_n7_s7_50_80 window_quality_performance_diff_qual_n7_s7_20_100 window_quality_performance_diff_perce_n7_s7_50_89 window_quality_performance_diff_perce_n7_s7_20_100'

set terminal postscript eps color enhanced
set key box top left inside Left samplen 1 spacing 1.15
set key enhanced
set key font ",24"
set xtics autofreq 1 font ",26"
set ytics autofreq 0.04 font ",26"
set yrange [0.60:1]
set size 1.2,1.2
set origin 0,0
set border 3
set ylabel "Metric Value" font ",28" offset -2
set xlabel "Number Of Services" font ",28" offset -1
set tics nomirror
set key bottom right
set key enhanced
set lmargin 15
do for [file in file_bases] {
    do for [i=3:7] {
        set output sprintf('%s_n%d.eps', file, i)
        plot for [j=1:i] base_path.sprintf('%s_n%d_w%d.dat', file, i, j) using 1:2 title sprintf('W Size %d', j) with linespoints pointtype (j) pointsize 3
        set output
    }
}
