# maximum_product_subset
A Python program to find the maximum product of a subset from a list of comma-separated integers including positive, negative, and zero values.
# Maximum Product Subset

This project finds the maximum product that can be obtained from a subset of given integers.

## 🚀 Features
- Handles positive, negative, and zero values
- Uses greedy logic for optimal result
- Works with comma-separated input

## 📥 Input
- Comma-separated integers (e.g., -1,2,-3,4,0)

## 📤 Output
- Maximum product of a subset

## 🧠 Logic
- Multiply all non-zero numbers
- Count negative numbers
- If odd negatives → remove the smallest negative
- Handle edge cases (only zeros or single negative)
