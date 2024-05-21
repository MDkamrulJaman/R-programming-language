# -*- coding: utf-8 -*-
"""R_programing _practice.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14loMJRozxEfCMFP_ASo_6TpkzApWIYrr
"""

# show output with print() or without

"Hello world"

print("hello world")

# variable

name <- "jaman"
age <- 23

# without print
name
age

# with paste
paste("my name is ", name )

# with print
print(age)


# multiple variable

var1 <- var2 <- var3 <- "Md"

var1
var2
var3


str <-"My name is Md Jaman. I love all the programming language such as c, c++, python, Java, Js, R to practice."

cat(str)

# data types

# numeric
x <- 10.5
class(x)

y <- 20
class(y)

# integer
i <- 1000L
class(i)

# complex (ib + a)
c <- 9i + 3
class(c)


# complex (a + ib)

cx <- 3 + 5i
class(cx)



# character or string
char <- "R is exciting"
class(char)

# logical/boolean
logic <- TRUE
class(logic)


# convert data_types

complex_to_integer =  as.integer(c)
complex_to_integer

integer_to_numeric = as.numeric(i)
integer_to_numeric

integer_to_complex = as.complex(i)
integer_to_complex

"""#Math and Logical Operators

"""

3+6+9
3-6-9
3*3
9/3
max(3,6,9,11)

min(3,6,9,11)

sqrt(81)

abs(-6)

ceiling(1.4)

floor(1.4)

# logical operators

5 == 5
5 != 3
5  > 3
3  < 5
5 >= 3
3 <= 5

# and
5 >= 3 & 3 <= 2

# or
5 >= 6 | 3 <= 5

"""# Conditions with user_input"""

# if- else if- else

num_1 = readline(prompt = "Enter the num1:");
num_1 = as.integer(num_1)


num_2 = readline(prompt = "Enter num2:");
num_2 = as.integer(num_2)


if(num_1 > num_2){

    print("num1 is greather than num2")

# nested if condition

     if (num_1 > 20 & num_2 < 20) {

    print("num1 above 20!")

  } else {

    print("num2 below 20.")
  }


 }else if(num_1 == num_2){

           print("a and b is equal")

      }else {

             print("num2 is greather than num1")

            }

"""#Loops"""

for(x in 1:10){
  print(x)
}

# for loop with list

fruits <- list("apple", "banana","orange", "mango")

for(fruits_name in fruits){

# next

   if (fruits_name == "banana") {
    next

   }

# break

  if(fruits_name == "mango"){
    break
  }

  print(fruits_name)
}


# for loop with vector

    dice <- c(1,2,3,4,5,6)

    for(element in dice){

       print(element)

    }

dice <- 1:6

for(x in dice) {

  if (x == 3) {

    print(paste("dice ", x, "got it"))

  } else {

    print(paste("dice ", x, "not this"))

  }
}


# nested loop

fruits_taste <- list("yummy","yellow","tasty")
fruit <- list("juice","banana","mango")


for(x in fruit){

for( y in fruits_taste){

#print with paste
  print(paste(x,y))
}

}

"""# Function"""

jaman <- function(name, age){

paste("My name and age is: ", name , age)
# paste("my age is:", age)

}


jaman("Md Jaman", 23)

# nested function

 outter_function <- function(x){

inner_function <- function(y){

a <- x + y
return (a)

}

}



value <- outter_function(3)

print(value(5))

# recursion


tri_recursion <- function(k) {
  if (k > 0) {
    result <- k + tri_recursion(k - 1)
    print(result)
  } else {
    result = 0
    return(result)
  }
}

output <- tri_recursion(6)

paste("the total result is", output)

plot(1:10, main="My Graph", xlab="The x-axis", ylab="The y axis")


plot(1:10, type="l", lwd=5, lty=3)

x <- c(5,7,8,7,2,2,9,4,11,12,9,6)
y <- c(99,86,87,88,111,103,87,94,78,77,85,86)

plot(x, y, main="Observation of Cars", xlab="Car age", ylab="Car speed")

mylabel <- c("Apples", "Bananas", "Cherries", "Dates")

colors <- c("blue", "yellow", "green", "black")

# pie chart
pie(x, label = mylabel, main = "Pie Chart", col = colors)

# explanation box
legend("bottomright", mylabel, fill = colors)

x <- c("A", "B", "C", "D")
y <- c(2, 4, 6, 8)

barplot(y, names.arg = x, width = c(1,2,3,4),col = "blue")