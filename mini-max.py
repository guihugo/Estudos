def minimax(arr):
   
   arr.sort() #Ordenação 

   soma = sum(arr)

   max_val = soma-min(arr)

   min_val =soma-max(arr)

   print(max_val,min_val)
   
   
   

minimax([7,69,2,221,8974])
