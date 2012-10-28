set terminal pdf dashed
set output "power_rodin_inadjoint.pdf"
set xlabel "Time [s]"
set ylabel "Relative Core Power [-]"
set title "Rod IN Shape Function - Rod IN Adjoint Weighted"
set grid
plot 'kinetics_power.out' using ($0/50):1 with lines linetype 1 linecolor rgb "red" linewidth 3.0 title "Reference", 'pke_power.out' using ($0/50):1 with lines linetype 1 linecolor rgb "green" linewidth 3.0 title "Classic PK", 'gpke_power.out' using ($0/50):1 with lines linetype 2 linecolor rgb "blue" linewidth 3.0 title "2-grp PK"
q
