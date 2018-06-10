# AdvancedAHP
To start on AHP basics Please go through : https://en.wikipedia.org/wiki/Analytic_hierarchy_process_%E2%80%93_car_example

Here I would be dealing with enhancements made on AHP to make it more user friendly and more accurate.
# Challanges
1) To fill a pair wise comparision table need to fill nc2 combinations(for 5 criterias - 10 and for 20 criterias - 190). User can fill upto 10 different combinations but it would be difficult to fill for 190 combinations.
2) I would be difficult to fill hundreds of combinations, even if user tries to fill it would cause inconsistency.

# Enhancements

Advanced AHP will solve these issues by asking the user to fill only "n-1" mandatory combinations and atleast 1 non-mandatory combinations instead of all combinations.( So user will be filling 20 combinations rather filling 190)
If non-mandatory fields are empty, AdvacnedAHP system would fill them with appropriate values so that it maintains the Consistency Index as minimum as possible.
If non-mandatory fields are filled with users priorities, systems would check for Consistency Index and also recommends the changes which would make the consistency Index as min as possible.

To run:
Have a AHP_Hierarchy.csv which has tree structure of hirerarchy.
1) run "PairWise_DataGeneration.py" file which generates pair wise comparision table.
2) Fill the pair wise table columns "Priority",	"Intensity".
3) run "Autocorrection_WeightsCalculation" which generates weights for each criteria. 

Use these weights to calculate the Rank order.
