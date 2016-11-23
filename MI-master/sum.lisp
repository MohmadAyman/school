(defun sum(list)    
    (if (null list)
        0

        (+ 
            (first list) 
            (sum (rest list))
        )   
    )   
)

