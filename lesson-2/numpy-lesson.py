import numpy as np

np.set_printoptions(precision=2)
# array  =np.array([[[1,2,3,4],[0,9,7,3] ,[5,6,7,8]],
#                   [[1,2,3,4],[0,9,7,3] ,[5,6,7,8]],
#                   [[1,2,3,4],[0,9,7,3] ,[5,6,7,8]]])
# array = np.array([[1,2,3,4],
#                   [5,6,7,8],
#                   [9,10,11,12],
#                   [13,14,15,16]])
# array =np.array([1,2,3,4])
# array[len(array)-1], array[-1] || array[len(array)-2], array[-2]

# array = array*2
# print(array)
# print(type(array))
# print("boyut ->" ,array.ndim)
# print("kaça kaç ->", array.shape ,"<-eleman sayısı")
# print(array[0,0,0])  #=== [0][0][0]
# print(array[0])
# ten = array[0,0,1]+  array[0,0,2] + array[1,2,0] # array[0,0,1]+  array[0,0,2] + array[1,2,1] ||array[0,0,0] +array[2,1,1]
# print(array[len(array)-2], array[-2])
# print(array[2:,2:])
# print(array[2:,:])
# print(array[:,2:])
# print(array ** 3)
# print(array +1)
# print(array -1)
# print(array *3)
# print((array /3))
# print(np.pi* array**2)
# array =np.array([1,2,3,4])
# array1 =np.array([5,6,7,8])

# print(array+array1)
# print(array-array1)
# print(array*array1)
# print(array/array1)
# print(array**array1)

# scores = np.array([100,93,84,55,58,76,63])

# scores[scores <60] = 0
# print(scores)


# array1= np.array([[1,2,3,4,7,8,9,10,11,12],
#                    [1,2,3,4,7,8,9,10,11,12]])
# array2= np.array([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9],[9,10],[10,11]])

# print(np.sum(array1))
# print(np.mean(array1))
# print(np.std(array1))
# print(np.var(array1))
# print(np.min(array1))
# print(np.max(array1))
# print(np.argmin(array1))
# print(np.argmax(array1))

# print(array2)
# print(array2.reshape(2,10))
# print(np.sum(array1 ,axis=0))
# array3= array2.reshape(2,10)

# print(array3)

# print(array1)
# print(array3*array1)
# print(array1.shape ,"a1->a2" ,array2.T.shape)

# print(array1 * array2.T)

# ages = np.array([[21,23,44,55,66,77,11],
#                  [18,13,17,22,28,24,40]])

# teenagers = ages[ages<18]
# adults = ages[(ages>=18) & (ages <=55)]
# seniors = ages[ages>=65]

# adults = np.where(ages >=18,ages ,0)
# print(adults)

rng = np.random.default_rng()  # rng= np.random.default_rng(seed=1) aynı döndürür

# print(rng.integers(0,9 ,size=(2,3)))

array = np.array(
    [
        1,
        2,
        3,
        4,
        5,
        6,
    ]
)
# rng.shuffle(array)
# print(array)

array = np.array(["🍩", "🍕", "🌮", "🍪", "🍌"])
fruit = rng.choice(array, size=(4, 4))
print(fruit)
# np.random.seed(seed=1)
# print(np.random.uniform(-99,99,size=(2,2)))
