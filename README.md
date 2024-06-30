# maps_nearby_search
We assume that you have used the ‘search nearby’ feature of Google maps to search for restaurants close
to you. (Use it and party with your friends over the upcoming weekend.) How should Google store the
locations of restaurants so that it can answer such queries fast? A na¨ıve idea is use a list and, given a query,
scan the list and return the subset of nearby restaurants. This requires time O(n) on a list of n locations.
How can we speed this up in practice? Note that the list of restaurants remains fairly unchanged over time,
while ‘search nearby’ queries are much more frequent. Therefore, it makes sense to pre-process the list of
restaurants and create an appropriate data structure that enables processing ‘search nearby’ queries much
faster than a brute-force search (assuming the number of “nearby” restaurants is much smaller than the
total number of restaurants, which is typically the case).

Therefore, Implemented 2D-Range Tree Data Structure to handle the queries in O(m + (log n)^2) time where m is 
the number of points returned, while ensuring thedatabase builds in O(n log n) time.
