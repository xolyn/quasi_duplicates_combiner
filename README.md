# quasi_duplicates_combiner
A Python program combining similar words in a word bag. 

## parameters:
- `wordlist`: list of strings
- `alpha`: the threshold for "similarity", smaller the stricter
## sample test:
`print(quasi_dup_combiner(["sale","sales","operations","operation","analytics","analitcis","analytic","web"]))`

output:

`['analitics', 'operation', 'sale', 'web']`

**Still updating**
- test edge test
- adopt machine learning algo.
