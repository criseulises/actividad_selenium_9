
# 🧪 Práctica Automatización de Pruebas con Selenium

## 📌 Universidad Iberoamericana (UNIBE)  
**Asignatura:** Aseguramiento de la Calidad del Software  
**Actividad:** Selenium - 9  
**Estudiante:** Cristian Eulises Sánchez Ramírez (25-0688)  
**Profesor:** OMAR ALEXIS REYES MEDINA  
**Año:** 2025  
**Lugar:** Santo Domingo, República Dominicana

---

## 🧾 Objetivo

Realizar una prueba automatizada utilizando Selenium WebDriver para evaluar la funcionalidad de un sitio web específico. Esta práctica cubre desde la configuración del entorno, identificación de escenarios, diseño, implementación, ejecución y análisis de resultados.

---

## 1. 🖥️ Selección del Proyecto o Sitio Web

Se utilizó el sitio público [http://automationpractice.pl](http://automationpractice.pl), una tienda online de prueba con funcionalidades de:

- Registro/inicio de sesión
- Búsqueda de productos
- Carrito de compras
- Contacto y checkout

Ideal para fines de pruebas automatizadas sin afectar sistemas reales.

---

## 2. ⚙️ Configuración del Entorno

- **Lenguaje:** Python 3.13  
- **Librería:** Selenium 4.17  
- **Navegador:** Google Chrome 135  
- **Driver:** ChromeDriver 135  
- **Editor:** Visual Studio Code  
- **Sistema Operativo:** macOS  
- **Instalación:**  
  ```bash
  pip install selenium
  ```

- Se colocó `chromedriver` en `/usr/local/bin` con permisos de ejecución.

---

## 3. 🔍 Escenarios Automatizados

Se diseñaron **10 pruebas automatizadas**, cubriendo las acciones más comunes en un sitio e-commerce:

1. Inicio de sesión fallido  
2. Inicio de sesión exitoso  
3. Búsqueda de producto  
4. Ir a “Contact us”  
5. Acceder al carrito desde el header  
6. Agregar producto específico al carrito  
7. Verificar productos destacados en home  
8. Navegar a la sección “Women”  
9. Verificar cantidad en el carrito  
10. Cerrar sesión

---

## 4. ✅ Diseño y Detalle de Casos de Prueba

### 🔹 Caso 1: Inicio de sesión fallido
- **Precondición:** Usuario no autenticado
- **Pasos:**
  1. Navegar a página de login
  2. Ingresar email inválido y contraseña errónea
  3. Hacer clic en “Sign in”
- **Datos de entrada:** `failuser@mail.com`, `wrongpass`
- **Resultado esperado:** Mensaje de error visible

### 🔹 Caso 2: Inicio de sesión exitoso
- **Precondición:** Usuario registrado
- **Pasos:**
  1. Ingresar al sitio
  2. Clic en “Sign in”
  3. Ingresar email y contraseña válidos
- **Datos:** `kagidat867@clubemp.com`, `L8vGXdUK6jWcfc`
- **Resultado esperado:** Nombre del usuario visible

### 🔹 Caso 3: Búsqueda de producto
- **Pasos:**
  1. Ingresar “dress” en barra de búsqueda
  2. Presionar Enter
- **Resultado esperado:** Aparecen resultados relevantes

### 🔹 Caso 4: Navegación a “Contact us”
- **Pasos:**
  1. Desde el home, clic en “Contact us”
- **Resultado esperado:** Página de contacto visible

### 🔹 Caso 5: Ir al carrito desde el ícono
- **Pasos:**
  1. Desde cualquier página, clic en ícono de carrito
- **Resultado esperado:** Página del carrito abierta

### 🔹 Caso 6: Agregar “Printed Summer Dress” al carrito
- **Pasos:**
  1. Buscar el producto
  2. Clic en “More”
  3. Seleccionar talla M
  4. Clic en “Add to cart”
- **Resultado esperado:** Mensaje de éxito “Product successfully added”

### 🔹 Caso 7: Ver productos destacados
- **Pasos:**
  1. Cargar la página principal
- **Resultado esperado:** Ver lista de productos con clase `product-container`

### 🔹 Caso 8: Sección “Women”
- **Pasos:**
  1. Clic en el menú “Women”
- **Resultado esperado:** Página de categoría cargada

### 🔹 Caso 9: Verificar cantidad en carrito
- **Pasos:**
  1. Observar el número del ícono del carrito (`ajax_cart_quantity`)
- **Resultado esperado:** Mostrar cantidad esperada

### 🔹 Caso 10: Cerrar sesión
- **Precondición:** Usuario autenticado
- **Pasos:**
  1. Clic en “Sign out”
- **Resultado esperado:** Redirección al login y usuario desconectado

---

## 5. 🧠 Configuración del WebDriver

```python
options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(), options=options)
wait = WebDriverWait(driver, 10)
```

---

## 6. 👨‍💻 Implementación Técnica

- Las pruebas fueron estructuradas en funciones separadas
- Se utilizó `ActionChains` para simular `hover`
- Se creó la función `type_like_human()` para simular escritura realista
- Se utilizó `Select` para seleccionar opciones de listas desplegables

---

## 7. ⏱️ Esperas Utilizadas

- **Explícitas:** `WebDriverWait + expected_conditions`
- Asegura que los elementos estén cargados antes de interactuar

---

## 8. ▶️ Ejecución

Desde terminal con:

```bash
python test_automation_practice.py
```

---

## 9. 📊 Resultados (por consola)

```text
✅ Error mostrado: There is 1 error. Authentication failed.
✅ Usuario autenticado: Example Test
✅ 7 productos encontrados.
✅ Página 'Contact us' abierta
✅ Página de carrito abierta
✅ Producto agregado al carrito exitosamente.
✅ Se muestran 6 productos destacados
✅ Sección 'Women' abierta correctamente
✅ Cantidad actual en carrito: 1
✅ Sesión cerrada exitosamente
```

---

## 10. 📌 Conclusiones

Esta práctica permitió comprender todo el ciclo de automatización: análisis, configuración, codificación, validación y verificación de resultados. Selenium demostró ser una herramienta poderosa para pruebas de interfaz. Se exploraron técnicas como esperas, simulación de usuario y validaciones visuales.

