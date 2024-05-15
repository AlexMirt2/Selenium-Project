import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class java_selen {

    public static void main(String[] args) {
        System.setProperty("webdriver.chrome.driver","D:\\Proiect personal\\chromedriver.exe");
        WebDriver driver = new ChromeDriver();
        driver.manage().window().maximize();
        

        // Navigare pe pagina Facebook
        driver.get("https://www.facebook.com");
        System.out.println("Opened Facebook");

        // Introducere email și parolă
         driver.findElement(By.id("email")).sendKeys("your_email@example.com");
        System.out.println("Email entered");
        
         driver.findElement(By.id("pass")).sendKeys("your_password");
        System.out.println("Password entered");

        // Apăsare buton de login
         driver.findElement(By.name("login")).click();

        // Așteptare pentru a permite încărcarea paginii după autentificare
        

        // Verificare dacă autentificarea a fost reușită prin verificarea prezenței butonului de logout
       

        // Închidere browser
        driver.quit();
    }
}
