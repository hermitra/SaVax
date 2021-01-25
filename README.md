# SaVax
Hack Cambridge 2021

Registered healthcare professionals at UK vaccination hubs can simply and quickly input any expiring vaccines into the app which then sends texts alerts to any users that spare vaccines are available. Unvaccinated users of the app are then able to book an appointment, preventing a wasted vaccination and making every shot count!

But why ?

The UK has ordered 100m of Astra Zeneca and 40m of Pfizer doses which get delivered in vials that respectively make up to 10 and 6 shots. However once the vial is opened/diluted, you must use it within the next 6 hours.

Suppose at the end of the day you have one more patient scheduled, so you open a new vial, inject your patient, and are left with spare. 

Making quick computation to estimate the weekly loss, that can be prevented with our app:

- 28.5% of vaccines in circulation are Pfizer, each dose costing £10
- 71.5% of vaccines in circulation are Astra Zeneca, each dose costing £1.60

- 2.5 doses of Pfizer wasted at the end of day on average
- 4.5 doses of Astra Zeneca wasted at the end of day on average

- 1016 vaccinations centers
- assume at least 2 vaccination stations in each centers
- on average 1m vaccination per week

Number of doses lost weekly: (28.5%*2.5 + 71.5%*4.5)*1016*7*2 = 5.6e4
% of doses lost weekly: 5.6e4/1e6= 5.6%

Loss for government weekly: (28.5%*10 + 71.5%*1.6)*5.6e4 = £224k


