# Colour
A simple function for decorating strings with colour in python.

Works in Linux and Mac terminals, and has been tested for Windows 10 command prompt.

## Install
No installation needed, just check out the repository  
'git clone git@github.com:SimenHellesund/colour.git'

## Usage examples
The function `colour` takes three input arguments, `fg`, `bg` and `bold`, in the form of strings.
`fg` selects the text colour, while `bg` selects the background colour. 
Supported colours are black("k), red("r"), green("g"), yellow("y"), blue("b"), purple("p"), cyan("c") and white("w").
Turning on the ´bold´ flag, with the value "1", makes the text bold.

`colour("string")` returns black text on red backogrund  
`colour("string", fg="w", bg="k")` returns white text on black (invisible) background  
`colour("string", fg="b", bg="g", bold="1")` returns bold blue text on green background   
