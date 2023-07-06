Como resumen podemos decir que Python al igual que casi todos los lenguajes de programación modernos manipula valores, los cuales pertene a cierto tipo o clase

- int, float, str, bool, list, dict, tupla y sets

lo que se pude hacer con estos valores, depende de su tipo.

Ademásde los valores, python, al igual que casi todos los lenguajes modernos, tiene operadores.

- +,-,%,/,*

Tarea: Averiguar qué es y como opera el operador módulo (%)

Observación, no podemos utilizar todos los operadores con todos lostipos de valores. Por ejemplo, no es posible sumar un texto, con un número (int, float), pero curiosamente si es posible multiplicar un texto por un número.


```python
"hola" + 4 # Error
"Hola" * 4 # Funciona
```

Por lo tanto es fundamental y muy necesario ejercitar con los diferentes tipos de valores.

Además tenemos las variables, que permiten asociar un nombre con el valor para luego mediante el nombre utilizar o manipular el valor.

```python
some_var = 42
other_var = "Hola Mundo"
print(some_var)
```
para controlar la ejecución del programa dependiendo del valor de alguna condición, tenemos las estructuras de control como el `if`, `elif` y `else`.

Además Python tiene loops o iteradores para ejecutar varias setencias en cada vuelta o iteración. Python tiene 2 loops el `while` y `for`.

Finalmente mencionar que Python también trae algunas funciones predefinidas para hacer tareas comunes y frecuentes como la función `print()`

- input(), int(), float(), len(), range(), print(), etc.