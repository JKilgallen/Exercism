# this is a stub function that takes a natural_number
# and should return the difference-of-squares as described
# in the README.md
difference_of_squares <- function(natural_number) {
  sum_of_squares <- 0
  square_of_sum <- 0
  for (i in 1:natural_number) {
    square_of_sum <- square_of_sum + i
    sum_of_squares <- sum_of_squares + i^2
  }
  square_of_sum <- square_of_sum^2
  square_of_sum - sum_of_squares
}
