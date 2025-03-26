from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time

# Configuración base
options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(), options=options)
wait = WebDriverWait(driver, 10)

def type_like_human(element, text, delay=0.05):
    for char in text:
        element.send_keys(char)
        time.sleep(delay)

# 1. Inicio de sesión fallido
def test_login_fail():
    print("\n🔍 Test 1: Inicio de sesión fallido")
    driver.get("http://automationpractice.pl/index.php")
    time.sleep(1)
    try:
        logout_btn = driver.find_element(By.CLASS_NAME, "logout")
        logout_btn.click()
        print("🔄 Cerrando sesión antes del intento fallido")
        time.sleep(2)
    except Exception as e:
        print(f"ℹ️ Ya estás deslogueado: {e}")

    driver.get("http://automationpractice.pl/index.php?controller=authentication")
    time.sleep(2)

    email = driver.find_element(By.ID, "email")
    type_like_human(email, "failuser@mail.com")

    passwd = driver.find_element(By.ID, "passwd")
    type_like_human(passwd, "wrongpass")

    driver.find_element(By.ID, "SubmitLogin").click()
    time.sleep(2)

    error = driver.find_element(By.XPATH, "//div[@class='alert alert-danger']")
    print("✅ Error mostrado:", error.text)

# 2. Inicio de sesión exitoso
def test_login_success():
    print("\n🔍 Test 2: Inicio de sesión exitoso")
    driver.get("http://automationpractice.pl/index.php")
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, "login").click()
    time.sleep(1)

    email = driver.find_element(By.ID, "email")
    type_like_human(email, "kagidat867@clubemp.com")

    passwd = driver.find_element(By.ID, "passwd")
    type_like_human(passwd, "L8vGXdUK6jWcfc")

    driver.find_element(By.ID, "SubmitLogin").click()
    time.sleep(2)
    try:
        username = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "account")))
        print("✅ Usuario autenticado:", username.text)
    except Exception as e:
        print(f"❌ Fallo en autenticación: {e}")

# 3. Búsqueda de producto
def test_search_product():
    print("\n🔍 Test 3: Búsqueda de producto")
    driver.get("http://automationpractice.pl/index.php")
    time.sleep(2)
    search = driver.find_element(By.ID, "search_query_top")
    type_like_human(search, "dress", delay=0.1)
    search.send_keys(Keys.RETURN)
    time.sleep(2)
    results = driver.find_elements(By.CLASS_NAME, "product-container")
    print(f"✅ {len(results)} productos encontrados.")

# 4. Ir a “Contact us”
def test_navigate_contact_us():
    print("\n🔍 Test 4: Navegación a 'Contact us'")
    driver.get("http://automationpractice.pl/index.php")
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Contact us").click()
    time.sleep(2)
    print("✅ Página 'Contact us' abierta")

# 5. Navegar al carrito desde ícono
def test_open_cart():
    print("\n🔍 Test 5: Abrir carrito desde el header")
    driver.get("http://automationpractice.pl/index.php")
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, "shopping_cart").click()
    time.sleep(2)
    print("✅ Página de carrito abierta")

def test_add_to_cart():
    print("\n🔍 Test 6: Agregar Printed Summer Dress al carrito")
    driver.get("http://automationpractice.pl/index.php")
    
    # Buscar producto
    search = driver.find_element(By.ID, "search_query_top")
    type_like_human(search, "Printed Summer Dress")
    search.send_keys(Keys.RETURN)
    time.sleep(2)

    # Hover sobre el producto para mostrar el botón "More"
    product = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-container")))
    actions = ActionChains(driver)
    actions.move_to_element(product).perform()
    time.sleep(1)

    # Clic en "More"
    more_button = product.find_element(By.CLASS_NAME, "lnk_view")
    more_button.click()
    time.sleep(2)

    # Seleccionar talla M
    print("👗 Seleccionando talla M")
    size_select = Select(driver.find_element(By.ID, "group_1"))
    size_select.select_by_visible_text("M")
    time.sleep(1)

    # Clic en Add to cart
    print("🛒 Agregando al carrito...")
    add_button = driver.find_element(By.ID, "add_to_cart")
    add_button.find_element(By.TAG_NAME, "button").click()
    time.sleep(3)

    # Confirmar mensaje de éxito
    try:
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "layer_cart_product")))
        print("✅ Producto agregado al carrito exitosamente.")
    except Exception as e:
        print(f"❌ No se pudo verificar que el producto fue agregado: {e}")

# 7. Verificar productos destacados
def test_home_featured():
    print("\n🔍 Test 7: Productos destacados en el home")
    driver.get("http://automationpractice.pl/index.php")
    time.sleep(2)
    featured = driver.find_elements(By.CLASS_NAME, "product-container")
    print(f"✅ Se muestran {len(featured)} productos destacados")

# 8. Navegar a la sección Women
def test_navigate_women_section():
    print("\n🔍 Test 8: Navegación a sección 'Women'")
    driver.get("http://automationpractice.pl/index.php")
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Women").click()
    time.sleep(2)
    print("✅ Sección 'Women' abierta correctamente")

# 9. Verificar cantidad de producto en carrito
def test_check_cart_quantity():
    print("\n🔍 Test 9: Verificar cantidad en carrito")
    driver.get("http://automationpractice.pl/index.php")
    cart = driver.find_element(By.CLASS_NAME, "ajax_cart_quantity")
    print("✅ Cantidad actual en carrito:", cart.text)

# 10. Cerrar sesión
def test_logout():
    print("\n🔍 Test 10: Cerrar sesión")
    try:
        logout_link = driver.find_element(By.CLASS_NAME, "logout")
        logout_link.click()
        time.sleep(2)
        print("✅ Sesión cerrada exitosamente")
    except Exception as e:
        print(f"⚠️ No se encontró el botón de cerrar sesión (¿ya cerrado?): {e}")

# Ejecutar todas las pruebas
test_login_fail()
time.sleep(1)
test_login_success()
time.sleep(1)
test_search_product()
time.sleep(1)
test_navigate_contact_us()
time.sleep(1)
test_open_cart()
time.sleep(1)
test_add_to_cart()
time.sleep(1)
test_home_featured()
time.sleep(1)
test_navigate_women_section()
time.sleep(1)
test_check_cart_quantity()
time.sleep(1)
test_logout()

# Cerrar navegador
driver.quit()