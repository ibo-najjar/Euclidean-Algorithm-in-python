# Euclidean-Algorithm-in-python
for input:
> 457896342434 32415312
> output:
```
457896342434 32415312
32415312 30060434
30060434 2354878
2354878 1801898
1801898 552980
552980 142958
142958 124106
124106 18852
18852 10994
10994 7858
7858 3136
3136 1586
1586 1550
1550 36
36 2
greatest common factor of 457896342434 and 32415312 using the Euclidean algorithm is 
2
execution time 0.00012339999999966267
greatest common factor of 457896342434 and 32415312 using the GCD function is 
2
execution time 1.71445310000000006312

Process finished with exit code 0
```
as we can see for large number the euclidean algorithm is way faster
but for smaller number inputs:
for input:
> 74 22
> output:
```
74 22
22 8
8 6
6 2
greatest common factor of 74 and 22 using the Euclidean algorithm is 
2
execution time 0.00004029999999843881 seconds
greatest common factor of 74 and 22 using the GCD function is 
2
execution time 0.00000530000000154018 seconds

Process finished with exit code 0
```
the normal function beats the euclidean function this time
## another scenario where the GCD is the worst case for the normal algorithm which is 1, here it took the normal function more than 7 whole seconds to find the GCD while it took the Eucildean algortihm 0.00015589999999932047 seconds
```
913421643566 134623453
134623453 1514961
1514961 1306885
1306885 208076
208076 58429
58429 32789
32789 25640
25640 7149
7149 4193
4193 2956
2956 1237
1237 482
482 273
273 209
209 64
64 17
17 13
13 4
4 1
greatest common factor of 913421643566 and 134623453 using the Euclidean algorithm is 
1
execution time 0.00015589999999932047 seconds
greatest common factor of 913421643566 and 134623453 using the GCD function is 
1
execution time 7.08772000000000090836 seconds

Process finished with exit code 0
```
