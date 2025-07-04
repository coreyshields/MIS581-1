proc reg data=combineddata;
    model Rate = Amount;
    title "Regression Analysis of Median Income and Patient Safety Incident Rate";
run;
quit;