set logscale y
set title "Residuals"
set ylabel 'Residuals'
set xlabel 'Iteration'
plot "< cat log.simpleFoam | grep 'Solving for Ux' | cut -d' ' -f9 | tr -d ','"title 'Ux' with lines,\
     "< cat log.simpleFoam | grep 'Solving for Uy' | cut -d' ' -f9 | tr -d ','"title 'Uy' with lines,\
     "< cat log.simpleFoam | grep 'Solving for p' | cut -d' ' -f9 | tr -d ','"title 'p' with lines,\
     "< cat log.simpleFoam | grep 'Solving for nuTilda' | cut -d' ' -f9 | tr -d ','"title 'nuTilda' with lines
pause -1 

set term png size 800,600
set output "resPlot.png"
replot
set term x11

# Template-lines:
# plot "< cat log.simpleFoam | grep 'Solving for Ux' | cut -d' ' -f9 | tr -d ','"title 'Ux' with lines,\
#     "< cat log.simpleFoam | grep 'Solving for Uy' | cut -d' ' -f9 | tr -d ','"title 'Uy' with lines,\
#     "< cat log.simpleFoam | grep 'Solving for Uz' | cut -d' ' -f9 | tr -d ','"title 'Uz' with lines,\
#     "< cat log.simpleFoam | grep 'Solving for p' | cut -d' ' -f9 | tr -d ','"title 'p' with lines,\
#     "< cat log.simpleFoam | grep 'Solving for k' | cut -d' ' -f9 | tr -d ','"title 'k' with lines,\
#     "< cat log.simpleFoam | grep 'Solving for epsilon' | cut -d' ' -f9 | tr -d ','"title 'epsilon' with lines,\
#     "< cat log.simpleFoam | grep 'Solving for omega' | cut -d' ' -f9 | tr -d ','"title 'omega' with lines,\
