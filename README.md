# NaiveBayes

### Example
```
$ python3 main.py data.csv trained_data.csv yes "0:<30" "1:>3" "2:>10" "3:>10" "4:3" "5:Yapıldı"
P(yes|<30,>3,>10,>10,3,Yapıldı) = 0.031637396694214864

$ python3 main.py data.csv trained_data.csv no "0:<30" "1:>3" "2:>10" "3:>10" "4:3" "5:Yapıldı"
P(no|<30,>3,>10,>10,3,Yapıldı) = 0.005165289256198346

$ # The first value is bigger than the second value, so classification for those conditions are "yes"

```
