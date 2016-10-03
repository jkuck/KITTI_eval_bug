#!/bin/bash

echo "Results from the current evaluation script run on ground truth with don't cares:"
python current_evaluate_tracking.py test_eval_on_ground_truth

echo ""
echo "------------------------------------------------------------------------------------"
echo "Results from the proposed evaluation script run on ground truth with don't cares:"
python proposed_evaluate_tracking.py test_eval_on_ground_truth

echo "Proposed change:"
diff proposed_evaluate_tracking.py current_evaluate_tracking.py
