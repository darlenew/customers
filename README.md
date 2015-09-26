# customers
Customer management tool.  Demonstrates loading customer location data from JSON file and calculating Great Circle Distance (Vincenty formula) to find local customers.

# usage
usage: customers.py [-h] [--file JSONFILE] [--origin ORIGIN] [--within WITHIN]

optional arguments:
  -h, --help       show this help message and exit
  --file JSONFILE  path to customer data
  --origin ORIGIN  calculate distance to customers from this point, e.g.
                   53.3381985,-6.2592576
  --within WITHIN  radius to search for customers from the origin
  
# example
Find customers within 100km of the specified lat,long.
```
customers.py --file customers.txt --origin 53.3381985,-6.2592576 --within 100
```
