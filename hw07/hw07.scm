(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cdr (cdr s))))

(define (ordered? s)
  (cond 
    ((null? s)
     #t)
    ((null? (cdr s))
     #t)
    ((or (< (car s) (cadr s)) (= (car s) (cadr s)))
     (ordered? (cdr s)))
    (else
     #f)))

(define (square x) (* x x))

(define (pow base exp) 
    (cond
        ((= exp 0) 1)
        ((= exp 1) base)
        ((even? exp) (square 
                    (pow base (/ exp 2))))
        ((odd? exp) (*
                        (square 
                            (pow base (quotient exp 2)))
                        base))
    )

)

