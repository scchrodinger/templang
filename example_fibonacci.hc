f! fibonacci(n):
  ! n < 0:
    ..("Incorrect input")
  !! n == 0:
    rtn! 0
  !! n == 1 or! n == 2:
    rtn! 1
  !.
      rtn! fibonacci(n-1) + fibonacci(n-2)
#this is how you comment it is the same
..(fibonacci(9))
