# NaiveBayes
Naive bayes classification algorithm in python


### Example
```
$ python3 main.py data.csv "hire" "age:<30" "gpa:>3" "projects:>10" "certificates:>10" "languages:1" "soldiery:Tescilli"
P(no|<30,>3,>10,>10,1,Tescilli) = 6.858121104071436e-05
P(yes|<30,>3,>10,>10,1,Tescilli) = 0.00038277959993521216
The classified class is 'yes'
$ # The second value is bigger than the first value, so classification for those conditions is "yes"
```
