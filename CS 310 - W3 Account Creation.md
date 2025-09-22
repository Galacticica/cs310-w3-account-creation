# CS310 - W3 Account Creation
By Reagan Zierke

## How did you invoke the `useradd` command-line tool?
I used the ```subprocess``` and ```sys``` libraries to be able to interact with the terminal.

## How do you pass flags to the `useradd` command?
I created a ```cmd``` variable that is a list and added each flag or parameter that needs to be passed as a seperate element of the list.
Then I can append to the list if I have more flags to add.