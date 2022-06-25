# marching-pythons

This is a basic implementation of marching squares in Python. If you want to learn more about marching squares check out wikipedia: https://en.wikipedia.org/wiki/Marching_squares. My implementation is VERY inefficient, you can see what I mean if you check out the code. It uses pygame to render the shapes and 2d arrays to keep track of the points.

I made this in a total of a couple of hours so it has tons of bugs that I probably won't be fixing. Some tips for using it: To increase the resolution change increment to WINDOW_WIDTH//n where n is some power of 2 less than WINDOW_WIDTH. Write the equation in python syntax, like instead of typing x^2, try x*\*2. For the algorithm to work, it must be an inequality where one side is 0. For example, x-y<=0 gives a diagonal line and x*\*2+y*\*2-100*\*2<=0 gives a circle. Keep in mind that the scale is 1 pixel, so make your graphs big so they're visible.
