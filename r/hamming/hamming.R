# This is a stub function to take two strings
# and calculate the hamming distance

hamming <- function(strand1, strand2) {
  strand1 <- strsplit(strand1, "")[[1]]
  strand2 <- strsplit(strand2, "")[[1]]

  if (length(strand1) != length(strand2)) {
    stop("Hamming distance supported only for strands of equal length")
  } else {
    sum(!(strand1 == strand2))
  }
}
