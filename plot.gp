# To use this script run gnuplot and the following set of commands prior:
# ---------------------
# set size square
# set xrange[0:7000]
# set yrange[0:7000]
# ---------------------
# Adjust the ranges to your needs

set view map
i=0
set cbrange[0:2]
while (i < 130 ){
 splot 'pandemic.out' using 2:3:4 index i palette ps 3 pt 3 title sprintf("t = %i", i);system('sleep 0.3')
 i=i+1
}

