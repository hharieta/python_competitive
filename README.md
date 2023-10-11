# Ejercicios de programación competitiva

## fast I/O

fast i/o c++:

```cpp
#define optimize cin.tie(nullptr); cout.tie(nullptr);ios::sync_with_stdio(0);
int main(){
    optimize // use for optimize inputs outputs
    
    return 0;
}
```

fast i/o python:

```python
from sys import stdin, stdout

stdin.readline()   # use for fast input
stdout.write()    # use for fast output
```

##  Algoritmo de Euclides

$$
mcd(x, y) = \{ 
\begin{matrix} 
x : y=0 \cr 
mcd(y, x \mod y) : y > 0 \cr 
\end{matrix}
$$

$$
When\ a \ne 0\, there\ are\ two\ solutions\ to\ (ax^2 + bx + c = 0)\ and\ they\ are\ 
 x = {-b \pm \sqrt{b^2-4ac} \over 2a}
$$

$$
\begin{matrix}
mcd(x, y) = \{
\begin{matrix}
x : y=0 \cr 
mcd(y, x \mod y) : y > 0 \cr 
\end{matrix}
\end{matrix}
$$





