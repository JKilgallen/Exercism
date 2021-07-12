(import (rnrs))

(define (leap-year? year)
  (if (= (modulo year 4) 0)
    (if (= (modulo year 100) 0)
      (if (= (modulo year 400) 0)
        #t
        #f)
      #t)
    #f))

