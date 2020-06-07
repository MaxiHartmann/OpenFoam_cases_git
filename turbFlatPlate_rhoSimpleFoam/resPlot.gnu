set logscale y
set title "Residuals"
set ylabel 'Residuals'
set xlabel 'Iteration'
filename="logS"
plot "< cat logS | grep 'Solving for Ux' | cut -d' ' -f9 | tr -d ','"title 'Ux' with lines,\
     "< cat logS | grep 'Solving for Uy' | cut -d' ' -f9 | tr -d ','"title 'Uy' with lines,\
     "< cat logS | grep 'Solving for p' | cut -d' ' -f9 | tr -d ','"title 'p' with lines,\
     "< cat logS | grep 'Solving for k' | cut -d' ' -f9 | tr -d ','"title 'k' with lines,\
	 "< cat logS | grep 'Solving for omega' | cut -d' ' -f9 | tr -d ','"title 'omega' with lines,\
	 "< cat logS | grep 'Solving for e' | cut -d' ' -f9 | tr -d ','"title 'e' with lines
pause -1 



# Template-lines:
# plot "< cat logS | grep 'Solving for Ux' | cut -d' ' -f9 | tr -d ','"title 'Ux' with lines,\
#     "< cat logS | grep 'Solving for Uy' | cut -d' ' -f9 | tr -d ','"title 'Uy' with lines,\
#     "< cat logS | grep 'Solving for Uz' | cut -d' ' -f9 | tr -d ','"title 'Uz' with lines,\
#     "< cat logS | grep 'Solving for p' | cut -d' ' -f9 | tr -d ','"title 'p' with lines,\
#     "< cat logS | grep 'Solving for k' | cut -d' ' -f9 | tr -d ','"title 'k' with lines,\
#     "< cat logS | grep 'Solving for epsilon' | cut -d' ' -f9 | tr -d ','"title 'epsilon' with lines,\
#     "< cat logS | grep 'Solving for omega' | cut -d' ' -f9 | tr -d ','"title 'omega' with lines,\
