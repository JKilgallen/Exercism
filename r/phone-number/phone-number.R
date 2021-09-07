parse_phone_number <- function(number_string) {
  number_characters <- strsplit(number_string, "")[[1]]
  phone_number <- ""
  for (i in 1:length(number_characters)) {
    print(number_characters[length(number_characters) - i + 1])
    if (is.numeric(number_characters[length(number_characters) - i + 1]) & length(phone_number) < 10) {
      phone_number <- paste(number_characters[length(number_characters) - i + 1], phone_number)
    }
  }
  phone_number
}
