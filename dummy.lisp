(clear-all)

(define-model unit2
    
(sgp :v t :show-focus t)

(chunk-type read-letters state)
(chunk-type array letter1 letter2 letter3)

(add-dm 
 (start isa chunk) (attend isa chunk)
 (respond isa chunk) (done isa chunk)
 (goal isa read-letters state start))


(P respond
   =goal>
   ?manual>   
      state       free
==>
   +manual>
      cmd         press-key
      key         a
)
 
(goal-focus goal)
)
