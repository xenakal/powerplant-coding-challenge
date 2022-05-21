# Solution to the [powerplant-coding-challenge](https://github.com/gem-spaas/powerplant-coding-challenge)
## Overview

Given the load, the cost of the underlying energy sources (gas, kerosine) and the Pmin and Pmax of each powerplant, we produce the production-plan for the available powerplants. Specifically, we need to determine which powerplants will be producing energy, and how much they should produce to meet balance and production constraints at minimal costs. This is the unit-commitment problem.


<br>  


## The Model 

There are $n$ available powerplants. 

### **System parameters:**
  * L - Total energy load to meet 
  * $p_i^{max}$ - Maximum power output of powerplant $i$
  * $p_i^{min}$ - Minimum power output of powerplant $i$
  * Z - Total generation cost of the generation units


### **Decision variables:**

 * Status of each unit: $u_i \in \{0,1\} \forall i \in \{1..n\}$
 * Output of each unit: $p_i \in \{0, [p_i^{min}, p_i^{max}]\} \forall i \in \{1..n\}$

### **Objective function:** 
$$ C(p_i, u_i) = \sum_{i=1}^{n}u_i C_i(p_i)$$
where $C_i(x)$ the cost function of powerplant $i$ (linear with regards to $p_i$). 
The goal is to find the production plan that minimises the total cost of energy generation under the total load constraint. Each of the $n$ powerplants also has constraints on the minimum and maximum energy it can produce. 

### **Constraints:** 

  * Load balance:
  $$ \sum_{i=1}^N u_ip_i = L$$
  * Maximum generation:
  $$ p_i \le u_ip_i^{max} \forall i \in {1..n}$$ 
  * Minimum generation:
  $$ p_i \ge u_ip_i^{min} \forall i \in {1..n}$$ 



## Optimisation algorithm 

There are a wide variety of algorithms to solve the unit commitment problem. Modern methods use algorithms such as branch and bounds, lagrangian relaxation, MIP, genetic algorithms and others.  In this project, a simple priority list approach has been employed. This algorithm runs in linear time with respect to the size of the powerplants. Its advantage is its quick execution time ($O(n)$ average complexity, $O(n^2) worst case), when compared to other methods. On the other hand, the algorithm will often not output the optimal solution.   


<br>  


### In practice

We consider three types of powerplants, according to the source of energy they use: 

* Kerosine: $C_{i}^{G}(Q) = \frac{p^{K}}{e_{i}}*Q$ 

* Wind: $C_{i}^{W}(Q) = 0$

* Natural gas: $C_{i}^{G}(Q) = (\frac{p^{G}}{e_{i}} + p_{CO2}*r_{CO2})*Q$

where $e_{i}$ the efficiency of powerplant $i$, $p^{X}$ the price of ressource $X$ (eur/MWh), $p_{CO2}$ the price of CO2 (eur/ton) and $r_{CO2}$ the mass of CO2 generated per MWh (ton/MWh). The powerplants are then ordered according to their full load average cost.

<br>  


## Run server

Navigate to the root project directory in a shell (*production_plan*).
### Docker
```
  docker build -t production-plan .
  docker run -p 8888:8888 production-plan
```
### From source (python 3.9)
  ```
  # TODO set venv & export to run with flask 
  pip install -r requirements.txt
  python .\production-plan.py 
  ```

<br>  


## Websocket 
The application also provides a websocket on port localhost:8888, which broadcasts the incoming POST requests along with the calculated production plan. [simple_client](TODO) is a simple client connecting to the socket.

<br>  


## Run tests
Navigate to the root project directory (*production_plan*) in a shell. 
  ```
  python -m unittest discover
  ```



