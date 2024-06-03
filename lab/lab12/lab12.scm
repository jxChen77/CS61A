(define (substitute s old new)
  (if (null? s)
    s
    (if (list? (car s))
      (cons (substitute (car s) old new) (substitute (cdr s) old new))
      (if (eqv? (car s) old)
        (cons new (substitute (cdr s) old new))
        (cons (car s) (substitute (cdr s) old new))
      )
    )
  )
)



; Feel free to use these helper procedures in your solution
(define (map fn s)
  (if (null? s)
      nil
      (cons (fn (car s)) (map fn (cdr s)))))

(define (filter fn s)
  (cond 
    ((null? s)    nil)
    ((fn (car s)) (cons (car s) (filter fn (cdr s))))
    (else         (filter fn (cdr s)))))

(define (count x s) 
  (if (null? s)
    0
    (if (eq? x (car s))
      (+ 1 (count x (cdr s)))
      (count x (cdr s))
    )
  )
)

(define (unique s) 
  (if (null? s)
    s
    (cons 
      (car s) 
      (unique 
        (filter 
          (lambda (x) (not (eq? x (car s))) )
          (cdr s))
      )
    )
  )
)

(define (tally names)
  (if (null? names)
      '()
      (let 
        ((current-name (car names)))
        (cons (list current-name
                    (length (filter (lambda (x) (eq? x current-name)) names)))
              (tally (filter (lambda (x) (not (eq? x current-name))) (cdr names)))))))