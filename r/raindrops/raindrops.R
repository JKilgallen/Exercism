raindrops <- function(number) {
  sounds <- c("Pling", "Plang", "Plong")
  vec <- number %% c(3,5,7) == 0
  if (any(vec)) {
    paste(sounds[vec], collapse = "")
  } else {
    toString(number)
  }

}

