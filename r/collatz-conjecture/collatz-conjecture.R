collatz_step_counter <- Vectorize(function(num) {
  if(num < 1) {
    stop("The Collatz sequence only terminates for positive numbers.")
  }

  if (num == 1) {
    0
  } else {
    1 + collatz_step_counter(ifelse(num %% 2 == 0, num / 2, 3*num + 1))
  }
})
