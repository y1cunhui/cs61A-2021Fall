(define (split-at lst n) 
    (cond
        ((null? lst) (cons lst nil))
        ((= n 0) (cons nil lst))
        (else (cons
                (cons (car lst) (car (split-at (cdr lst) (- n 1))))
                (cdr (split-at (cdr lst) (- n 1))))))
    
)

(define (compose-all funcs)
    (if 
        (null? funcs)
        (lambda (x) x)
        (lambda (x) ((compose-all (cdr funcs)) ((car funcs) x))))
    )

(cdr (split-at '(1 2 3 4 6) 3))