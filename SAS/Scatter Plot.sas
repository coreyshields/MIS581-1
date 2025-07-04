proc sgplot data=combineddata;
    scatter x=amount y=rate / markerattrs=(symbol=CircleFilled);
    reg x=amount y=rate / lineattrs=(color=blue);
    title "Scatter Plot with Regression Line";
run;