## Errores a corregir

### Error 1 — Tres métodos con el mismo nombre (`persona.py`)

**Dónde:** líneas 14, 21 y 27.

**Qué está pasando:** dentro de la clase `Persona` hay tres métodos que se llaman igual (`set_socios`). Uno pretende modificar el tipo de identificación, otro la identificación y otro la nacionalidad. En Python, cuando dos o más métodos de una clase tienen el mismo nombre, **el último reemplaza a todos los anteriores**: los otros dos métodos dejan de existir sin dar ningún aviso.

**Cómo darte cuenta:** probá modificar la identificación de una persona con su setter y después leela con el getter. Vas a ver que no cambia lo que esperabas: siempre termina cambiando la nacionalidad, porque ese es el único método que sobrevive.

**Qué tenés que hacer:** darle a cada setter un nombre propio según el atributo que modifica (el nombre debe decir qué atributo cambia), y de paso corregir los nombres de los parámetros para que también describan lo que reciben.

---

### Error 2 — Un `print()` adentro del cuerpo de la clase (`clubCategoria.py` y `admin.py`)

**Dónde:** línea 14 de `clubCategoria.py` y línea 45 de `admin.py`.

**Qué está pasando:** hay una línea con `print("------...")` escrita directamente dentro de la clase, pero **fuera de cualquier método**. Todo lo que está a nivel de clase se ejecuta una sola vez, cuando Python define la clase, antes incluso de que exista cualquier objeto. Ese print no depende de ningún objeto, no puede usar `self`, y se muestra aunque nunca crees un socio ni llames a ningún método.

**Cómo darte cuenta:** al ejecutar el archivo aparecen los guiones antes de cualquier salida de las pruebas, aunque todavía no se haya creado ningún objeto.

**Qué tenés que hacer:** eliminar esa línea. Si era un separador visual, tiene que ir en la parte de pruebas del final del archivo, nunca adentro de la clase.

---

### Error 3 — Eliminar elementos mientras se recorre la lista (`clubCategoria.py`)

**Dónde:** método `eliminar_socio`, líneas 20-24.

**Qué está pasando:** el método recorre la lista de socios con un `for` y, cuando encuentra coincidencia, hace `remove()` sobre **la misma lista que está recorriendo**. Al eliminar un elemento, los que están después se corren un lugar hacia atrás, pero el contador interno del `for` ya avanzó: el resultado es que **se saltean socios**.

**Cómo darte cuenta:** registrá dos socios con exactamente el mismo nombre y llamá una sola vez a `eliminar_socio`. Fijate cuántos quedan: uno de los duplicados sobrevive aunque debería haberse borrado. Además, si buscás un nombre que no existe, el método no dice nada (falla en silencio).

**Qué tenés que hacer:** reescribir el método para que no elimine mientras sigue recorriendo (pista: cortar apenas encuentre y elimine al socio) y agregar un mensaje informativo cuando el nombre no se encuentre en la lista.

---

### Error 4 — División por cero en `porcentaje_activos` (`clubCategoria.py`)

**Dónde:** método `porcentaje_activos`, líneas 44-53.

**Qué está pasando:** el porcentaje se calcula dividiendo por `len(self.__socios)`. Si la categoría todavía no registró ningún socio, esa cantidad es cero y el programa explota con:

```
ZeroDivisionError: division by zero
```

**Cómo darte cuenta:** creá una categoría nueva sin registrar socios y llamá directamente a `porcentaje_activos()`.

**Qué tenés que hacer:** controlar antes de dividir qué pasa si la lista está vacía e informarlo. De paso, redondear el resultado a dos decimales: hoy imprime cosas como `66.66666666666667 %`.

---

### Error 5 — Métodos que no validan si el dato existe (varios archivos)

**Dónde:**
- `eliminar_actividad` (`clubCategoria.py`, líneas 40-42)
- `eliminar_club` (`socio.py`, líneas 30-32)
- `buscar_socio` (`clubCategoria.py`, líneas 26-29)
- `pagar_cuota` (`socio.py`, líneas 60-65)

**Qué está pasando:** son cuatro variantes del mismo problema: operan sobre un dato sin verificar primero que esté en la lista.

- Si llamás a `eliminar_actividad` o `eliminar_club` con algo que no está en la lista, el programa rompe con `ValueError`.
- Si buscás un socio inexistente con `buscar_socio`, no aparece ningún mensaje.
- Si pagás una cuota con un número que no existe, o una cuota que ya estaba pagada, tampoco pasa nada ni se informa.

**Cómo darte cuenta:** probá cada uno de esos métodos con un valor que NO esté cargado y observá qué pasa: a veces crash, a veces silencio absoluto. Un usuario nunca debería quedarse sin respuesta.

**Qué tenés que hacer:** validar antes de actuar: verificar si el elemento está en la lista, y mostrar un mensaje claro tanto cuando la operación sale bien como cuando el dato no existe. En el caso de `pagar_cuota`, distinguir además entre "no existe esa cuota" y "ya estaba pagada".

---

### Error 6 — Nombre de clase que no corresponde (`clubCategoria.py`)

**Dónde:** línea 3.

**Qué está pasando:** la clase del archivo se llama `Clublosavengers`. La consigna pide una clase **Club Categoria**, y el archivo ya se llama así: el nombre actual no describe lo que la clase representa.

**Qué tenés que hacer:** renombrar la clase a `ClubCategoria` (y actualizar todos los lugares donde se usa para crear objetos).

---

### Error 7 — Listas de socios desconectadas (integración del proyecto) — EL MÁS IMPORTANTE

**Dónde:** `admin.py` (línea 9, `self.socios = []`) y `clubCategoria.py` (lista privada `__socios`).

**Qué está pasando:** un proyecto tiene que funcionar como un solo sistema conectado, y acá hay **dos listas de socios paralelas que no se comunican**:

1. La lista principal es `__socios` de `ClubCategoria`: ahí deberían estar TODOS los socios del club.
2. Pero `Administrador` creó su propia lista (`self.socios`) y agrega ahí sus socios, que **nunca llegan a la categoría del club**.
3. Encima usan formatos distintos: la categoría guarda diccionarios (`{"nombre": ..., "activo": ...}`) y el administrador guarda objetos `Socio`. Son dos representaciones diferentes del mismo concepto viviendo en el mismo proyecto.

**Consecuencia concreta:** si el administrador registra un socio, ese socio no aparece en el club; si la categoría suspende a alguien, el administrador no se entera. Cada módulo vive en su burbuja.

**Cómo darte cuenta:** creá la categoría y el administrador en la misma prueba, cargá un socio desde el administrador y fijate si aparece en la lista de socios de la categoría. Hoy no aparece.

**Qué tenés que hacer:**
- Dejar `__socios` de `ClubCategoria` como **única** lista de socios de todo el proyecto.
- Hacer que `Administrador` deje de tener su propia lista y trabaje sobre la del club/categoría (por ejemplo, recibiendo la categoría o usando los métodos de registro/eliminación que ella ya tiene).
- Que en esa única lista se guarden objetos `Socio` reales en lugar de diccionarios, y que `Socio` tenga nombre para poder buscarlo y listar correctamente.

---

### Error 8 — `Socio` no hereda de `Persona` (`socio.py`)

**Dónde:** línea 3.

**Qué está pasando:** hoy la clase está definida como `class Socio:` suelta, sin relación con `Persona`, aunque conceptualmente **un socio ES una persona**. Por eso `Socio` no tiene nombre, ni edad, ni identificación, y no puede usar los métodos que ya escribieron en `Persona` (saber si es mayor de edad, verificar la identificación). Es código que ya existe y se está desperdiciando.

**Pista clave:** `Administrador` ya hereda de `Socio`. Si hacen que `Socio` herede de `Persona`, queda completa la cadena `Persona → Socio → Administrador`, y todo el proyecto queda conectado.

**Qué tenés que hacer:** hacer que `Socio` herede de `Persona`, completar su constructor con los datos de persona (nombre completo, edad, tipo y número de identificación, nacionalidad) llamando al constructor de la clase padre, y revisar qué atributos o métodos quedaron duplicados entre las dos clases.

**Prueba para comprobar:** crear un socio y poder consultar su nombre y usar `es_mayor_de_edad()` directamente desde él. Hoy eso no existe.

---

## Mejoras opcionales (desafíos)

Si ya corregiste todo lo anterior, probá con estas mejoras:

- [ ] Corregir el typo `fecha_incripcion` → `fecha_inscripcion` (aparece en varios archivos).
- [ ] Evitar registrar dos veces el mismo socio o la misma actividad.
- [ ] Hacer que `buscar_socio` devuelva el socio encontrado (además de mostrarlo) para poder usarlo después.
- [ ] Corregir el mensaje de cuotas vencidas: dice "hace X dia", debería ser "días".
- [ ] Validar en `verificar_identificacion` también espacios en blanco y valores nulos.

