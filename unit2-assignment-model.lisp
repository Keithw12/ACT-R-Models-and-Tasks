(clear-all)

(define-model unit2
    
(sgp :v t :show-focus t)

(chunk-type read-letters state)
(chunk-type array letter1 letter2 letter3)

(add-dm 
 (start isa chunk) (attend isa chunk)
 (respond isa chunk) (done isa chunk)
 (goal isa read-letters state start))

(P find-unattended-letter1
	=goal>
		ISA		read-letters
		state	start
==>
	+visual-location>
		:attended	nil
	=goal>
		state	find-location
)

(P attend-letter1
	=goal>
		ISA		read-letters
		state	find-location
	=visual-location>
	?visual>
		state	free
==>
	+visual>
		cmd			move-attention
		screen-pos	=visual-location
	=goal>
		state	attend
)

(P encode-leter1
	=goal>
		ISA		read-letters
		state	attend
	=visual>
		value	=letter
	?imaginal>
		state	free
==>
	=goal>
		state	letter2Start
	+imaginal>
		ISA		array
		letter1	=letter
		letter2 nil
		letter3 nil
)

(P find-unattended-letter2
   =goal>
      ISA         read-letters
      state       letter2Start
 ==>
   +visual-location>
      :attended    nil
   =goal>
      state       findLetter2
)

(P attend-letter2
   =goal>
      ISA         read-letters
      state       findLetter2
   =visual-location>
   ?visual>
      state       free
==>
   +visual>
      cmd         move-attention
      screen-pos  =visual-location
   =goal>
      state       attendLetter2
)

(P encode-letter2
   =goal>
      ISA         read-letters
      state       attendLetter2
   =visual>
      value       =letter
   ?imaginal>
      state       free
	=imaginal>
		isa		  array
		letter1	  =letter1
==>
   =goal>
      state       letter3Start
   +imaginal>
      isa         array
	  letter1	   =letter1
      letter2      =letter
)

(P find-unattended-letter3
   =goal>
      ISA         read-letters
      state       letter3Start
 ==>
   +visual-location>
      :attended    nil
   =goal>
      state       findLetter3
)

(P attend-letter3
   =goal>
      ISA         read-letters
      state       findLetter3
   =visual-location>
   ?visual>
      state       free
==>
   +visual>
      cmd         move-attention
      screen-pos  =visual-location
   =goal>
      state       attendLetter3
)

(P encode-letter3
   =goal>
      ISA         read-letters
      state       attendLetter3
   =visual>
      value       =letter
   ?imaginal>
      state       free
	=imaginal>
		isa		  array
		letter1	  =letter1
		letter2	  =letter2
==>
   =goal>
      state       respond
   +imaginal>
      isa         array
	  letter1	  =letter1
	  letter2	  =letter2
      letter3      =letter
)

(P respond1
   =goal>
      ISA         read-letters
      state       respond
   =imaginal>
      isa         array
      letter1     =letter1
	  letter2	  =letter1
	  letter3	  =letter3
   ?manual>   
      state       free
	
==>
   =goal>
      state       done
   +manual>
      cmd         press-key
      key         =letter3
)

(P respond2
   =goal>
      ISA         read-letters
      state       respond
   =imaginal>
      isa         array
      letter2     =letter2
	  letter3	  =letter2
	  letter1	  =letter1
   ?manual>   
      state       free
==>
   =goal>
      state       done
   +manual>
      cmd         press-key
      key         =letter1
)

(P respond3
   =goal>
      ISA         read-letters
      state       respond
   =imaginal>
      isa         array
      letter1     =letter1
	  letter3	  =letter1
	  letter2	  =letter2
   ?manual>   
      state       free
==>
   =goal>
      state       done
   +manual>
      cmd         press-key
      key         =letter2
)
 
(goal-focus goal)
)
