# 
**Hexlet tests and linter status:**
[![Actions Status](https://github.com/lawyer-arch/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/lawyer-arch/python-project-49/actions)

##
**Code Climate**
[![Maintainability](https://api.codeclimate.com/v1/badges/8c4e05702f45473b807e/maintainability)](https://codeclimate.com/github/lawyer-arch/python-project-49/maintainability)


#
**Description**  

Hexlet Code is a collection of 5 math-related games designed to challenge and improve your arithmetic skills. The games include:

1. Checking if a number is prime
2. Inserting a number into an arithmetic progression
3. Providing the result of a calculation (multiplication, addition, subtraction)
4. Answering if a number is even
5. Finding the greatest common divisor of two numbers  

##
*Installation*  

### To install the games, ensure you have Poetry installed on your machine, then run the following commands:  
        make install

###
*Games*  
* __To start playing, you can run the following commands:__  
    ** To play "Check if a number is prime":  
        make brain-prime

* __To insert a number into an arithmetic progression:__  
        make brain-progression

* __To provide the result of a calculation:__  
        make brain-calc

* __To answer if a number is even:__  
        make brain-even

* __To find the greatest common divisor of two numbers:__  
        make brain-gcd

_After installing the package using pip install --user, all commands can be executed without poetry run (simply brain-calc, not poetry run brain-calc)._  
    Asciinema records

### 
*Entry via link:* [brain_even](https://asciinema.org/a/ujyQb9lh1AnuJx3OkTP1os05e), [brain_calc](https://asciinema.org/a/2tnprLRVIA0UWjDucFlVbdPYa), [brain_gcd]( https://asciinema.org/a/cT0ANeM7AlN2k7WYvntRqglwc), [brain_progression](https://asciinema.org/a/DUEsVYJU3vqpVswBXXbz3JTbs), [brain_prime](https://asciinema.org/a/eCTMlc7aPAu8idQOqR2t3kFUO)


## Установка зависимостей

Before installing dependencies, make sure you have `uv` installed. If you don't have it, install it with:

```sh
`pipx install uv` or `pip install uv`
```

More information about `uv` can be found in the [official repository](https://github.com/astral-sh/uv).

After installing uv run:

```sh
`uv sync`
```
