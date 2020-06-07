set logscale y
set title "Residuals"
set ylabel 'Residuals'
set xlabel 'Iteration'
filename="logS"
plot "< cat logS | grep 'Solving for Ux' | cut -d' ' -f9 | tr -d ','"title 'Ux' with lines,\
     "< cat logS | grep 'Solving for Uy' | cut -d' ' -f9 | tr -d ','"title 'Uy' with lines,\
     "< cat logS | grep 'Solving for p' | cut -d' ' -f9 | tr -d ','"title 'p' with lines,\
     "< cat logS | grep 'Solving for nuTilda' | cut -d' ' -f9 | tr -d ','"title 'nuTilda' with lines,\

pause -1
