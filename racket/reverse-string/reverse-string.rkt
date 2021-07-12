#lang racket
(provide my-reverse)

(define (my-reverse s)
    (list->string (aux (string->list s))))

(define (aux xs)
  (if (null? xs)
    xs
    (append (aux (cdr xs)) (list (car xs)))))

