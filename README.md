# Finding_Nearest_CostFactor
Python Script to solve the nearest neighbour problem.

I was tasked with catagorizing a list of 800 buildings with a regional cost factor. 

This factor corrects the pricing of building assets to better reflect costs in their respective region.

I used cost factors from the RS Means database, which is an industry recognized source for obtaining price estimates for construction.

This cost factors list only had regional factors for major cities and some rural towns. 

The way proposed to me to tackle this problem was using 3 digit zip codes. 

Not all the buildings in my list corresponded with these factors by 3 digit zip code.

Also 3 digit zip codes are not the most accurate as some zip regions may be very large and have multiple factors within them.

I instead decided to solve this problem using a nearest neighbour approach.

My solutions included a regular brute force using building long/lat coordinates, finding distances to all cost 
factors and returning the shortest distance. Solution did not need to be optimize as with my list of ~400 factors I was able to 
specify a cost factor for all 800 buildings in less then a second.

I also tried implementing the sklearn nearest neighbour methods, but got strange results and scrapped the data.

